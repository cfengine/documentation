#!/usr/bin/env bash
#
# Build the CFEngine documentation locally in a Docker container.
#
# Self-contained: clones the sibling repos that the build expects
# (core, nova, enterprise, masterfiles, nt-docs) into ./tmp/ and runs
# the existing Docker-based pipeline against them, without requiring
# anything outside this directory.
#
# Override via env vars if needed:
#   BRANCH                  branch name to build for (default: master)
#   PACKAGE_JOB             cf-remote or a buildcache job (default: cf-remote)
#   PACKAGE_UPLOAD_DIRECTORY  (default: n/a — unused with cf-remote)
#   PACKAGE_BUILD             (default: n/a — unused with cf-remote)
#   LTS_VERSION               (default: empty)
#   DOCKER                  docker binary to use (default: docker)
#   SKIP_SERVE=1            don't start the serve container (site + search)
#   SERVE_ONLY=1            skip the build; just (re)start the serve container
#                           against the previously built site
#   SITE_PORT               host port for the served site (default: 8000)
#   SERVE_IMAGE             tag for the serve image (default: cfengine-docs-serve)
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

TMP_DIR="$SCRIPT_DIR/tmp"
CACHE_DIR="$TMP_DIR/cache"   # persistent clones with .git
WORK_DIR="$TMP_DIR/work"     # clean working copies (.git stripped) — what we mount
DOC_WORK="$WORK_DIR/documentation"
mkdir -p "$CACHE_DIR" "$WORK_DIR"

BRANCH="${BRANCH:-master}"
PACKAGE_JOB="${PACKAGE_JOB:-cf-remote}"
PACKAGE_UPLOAD_DIRECTORY="${PACKAGE_UPLOAD_DIRECTORY:-n/a}"
PACKAGE_BUILD="${PACKAGE_BUILD:-n/a}"
LTS_VERSION="${LTS_VERSION:-}"
DOCKER="${DOCKER:-docker}"
SITE_PORT="${SITE_PORT:-8000}"
SERVE_IMAGE="${SERVE_IMAGE:-cfengine-docs-serve}"
SERVE_CONTAINER="cfengine-docs-serve"

# repo_name url default_branch
REPOS=(
    "core            git@github.com:cfengine/core.git              master"
    "nova            git@github.com:cfengine/nova.git              master"
    "enterprise      git@github.com:cfengine/enterprise.git        master"
    "masterfiles     git@github.com:cfengine/masterfiles.git       master"
    "nt-docs         git@github.com:northerntechhq/nt-docs.git     main"
    "infra           git@github.com:NorthernTechHQ/infra.git       master"
)

# Serve the built site plus a working search in one Docker container
serve_site() {
    local site_dir="$DOC_WORK/generator/_site"
    local server_js="$WORK_DIR/infra/services/docs-cfengine-com/search-server/server.js"
    local flex_pkg="$WORK_DIR/nt-docs/scripts/search/index/package.json"
    local label="$BRANCH"
    [ -n "$LTS_VERSION" ] && label="lts"

    if [ ! -f "$server_js" ] || [ ! -d "$site_dir/assets/searchIndex" ]; then
        echo "error: no built site (or no infra checkout) under tmp/; run a full build first" >&2
        return 1
    fi

    echo "==> Building serve image $SERVE_IMAGE"
    "$DOCKER" build --tag "$SERVE_IMAGE" "$SCRIPT_DIR/generator/serve"

    echo "==> Starting serve container $SERVE_CONTAINER on port $SITE_PORT"
    "$DOCKER" rm -f "$SERVE_CONTAINER" >/dev/null 2>&1 || true
    "$DOCKER" run -d --name "$SERVE_CONTAINER" \
        -p "$SITE_PORT:8000" \
        -e DOCS_PATH=/docs \
        -v "$site_dir:/site:ro" \
        -v "$site_dir:/docs/$label:ro" \
        -v "$server_js:/search/server.js:ro" \
        "$SERVE_IMAGE" >/dev/null

    local query_url="http://127.0.0.1:$SITE_PORT/docs/search/$label/?searchQuery=cfengine"
    for _ in $(seq 1 15); do
        if curl -fsS --max-time 60 "$query_url" >/dev/null 2>&1; then
            echo "    search is up: $query_url"
            return 0
        fi
        sleep 1
    done
    echo "    search did not respond; check: $DOCKER logs $SERVE_CONTAINER" >&2
    return 1
}

# Block until Ctrl-C, then stop and remove the serve container.
wait_serve() {
    echo "    Press Ctrl-C to stop it."
    trap '"$DOCKER" rm -f "$SERVE_CONTAINER" >/dev/null 2>&1 || true
          echo "==> Stopped $SERVE_CONTAINER"; exit 0' INT TERM
    # docker wait runs in the background so the interruptible `wait`
    # builtin blocks instead — a trapped signal fires immediately.
    "$DOCKER" wait "$SERVE_CONTAINER" >/dev/null 2>&1 &
    wait $! || true
}

# start the serve container against an existing build, no rebuild.
if [ -n "${SERVE_ONLY:-}" ]; then
    serve_site
    echo "==> Open http://127.0.0.1:$SITE_PORT/"
    wait_serve
    exit 0
fi

# 1. Clone (or update) the sibling repos under tmp/cache/, then export a
#    clean working copy (no .git) to tmp/work/, which is the docker build
#    context.
echo "==> Preparing sibling repos under $TMP_DIR"
for entry in "${REPOS[@]}"; do
    # shellcheck disable=SC2086
    set -- $entry
    name="$1"; url="$2"; default_branch="$3"
    cache="$CACHE_DIR/$name"
    work="$WORK_DIR/$name"

    if [ -d "$cache/.git" ]; then
        echo "  - $name: fetching latest"
        git -C "$cache" fetch --quiet --tags origin
    else
        echo "  - $name: cloning $url"
        git clone --quiet "$url" "$cache"
    fi

    if git -C "$cache" rev-parse --verify --quiet "origin/$BRANCH" >/dev/null; then
        git -C "$cache" checkout --quiet -B "$BRANCH" "origin/$BRANCH"
    else
        echo "    branch '$BRANCH' not found in $name; using '$default_branch'"
        git -C "$cache" checkout --quiet -B "$default_branch" "origin/$default_branch"
    fi

    # Export a clean snapshot for the container. Using `git archive` so
    # we get exactly what's tracked, without .git or untracked junk.
    rm -rf "$work"
    mkdir -p "$work"
    git -C "$cache" archive --format=tar HEAD | tar -x -C "$work"
done

# 1b. Sync the documentation source itself into tmp/work/documentation.
# The build mutates files in place (sed on config.toml, cfdoc_preprocess.py
# rewriting markdown, etc.), so we must NOT bind-mount the user's checkout
# directly. Use rsync with --delete to keep the copy in sync (including
# uncommitted/untracked changes) without dragging tmp/ or .git into it.
# cfdoc_log.markdown is a build artifact written into content/ by cfdoc_qa.py
# (it's gitignored). If a previous run left it behind, the link checker
# re-parses its log entries — which themselves contain literal
# [foo#foo][foo#foo] markdown — and reports hundreds of bogus "unresolved
# reference" errors. We must clear it from both sides: --exclude keeps the
# host's copy from being synced in, and the explicit rm removes any copy a
# previous in-container build wrote into the work tree (rsync --delete will
# NOT remove an --exclude'd path, so the exclude alone is not enough).
echo "==> Syncing documentation source to $DOC_WORK"
mkdir -p "$DOC_WORK"
rsync -a --delete \
    --exclude='/tmp/' \
    --exclude='/.git/' \
    --exclude='/content/cfdoc_log.markdown' \
    "$SCRIPT_DIR/" "$DOC_WORK/"
rm -f "$DOC_WORK/content/cfdoc_log.markdown"

# 2. Run the build (the generator/build/Dockerfile stages), the tarballs are exported to output/.
echo "==> Building documentation"
"$DOCKER" build \
    --file "$DOC_WORK/generator/build/Dockerfile" \
    --build-arg BRANCH="$BRANCH" \
    --build-arg PACKAGE_JOB="$PACKAGE_JOB" \
    --build-arg PACKAGE_UPLOAD_DIRECTORY="$PACKAGE_UPLOAD_DIRECTORY" \
    --build-arg PACKAGE_BUILD="$PACKAGE_BUILD" \
    --build-arg LTS_VERSION="$LTS_VERSION" \
    --output "type=local,dest=$DOC_WORK/output" \
    "$WORK_DIR"

# 3. Unpack the site from packed-for-shipping.tar.gz (what production deploys).
tar -xzf "$DOC_WORK/output/packed-for-shipping.tar.gz" -C "$DOC_WORK/generator"

# 4. Serve the site with a working search (see serve_site above).
if [ -z "${SKIP_SERVE:-}" ]; then
    serve_site
fi

echo "==> Done. Generated site is in: $DOC_WORK/generator/_site"
echo "    Tarballs are in: $DOC_WORK/output/"
if [ -z "${SKIP_SERVE:-}" ]; then
    echo "    Documentation is served at:"
    echo "    http://127.0.0.1:$SITE_PORT/"
    wait_serve
else
    echo "    Start a webserver (no search):"
    echo "    python3 -m http.server --directory $DOC_WORK/generator/_site/"
    echo "    And then open in your browser:"
    echo "    http://127.0.0.1:8000/"
fi
