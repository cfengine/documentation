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
#   IMAGE_NAME              tag for the build image (default: cfengine-docs-hugo)
#   SKIP_PUBLISH=1          skip the _publish.sh step (just build)

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
IMAGE_NAME="${IMAGE_NAME:-cfengine-docs-hugo}"

# repo_name url default_branch
REPOS=(
    "core            git@github.com:cfengine/core.git              master"
    "nova            git@github.com:cfengine/nova.git              master"
    "enterprise      git@github.com:cfengine/enterprise.git        master"
    "masterfiles     git@github.com:cfengine/masterfiles.git       master"
    "nt-docs         git@github.com:northerntechhq/nt-docs.git     main"
)

# 1. Clone (or update) the sibling repos under tmp/cache/, then export a
#    clean working copy (no .git) to tmp/work/. We mount the .git-free
#    copy because the container does `chmod -R` over each repo, and on
#    macOS Docker bind mounts can't chmod git pack files written by the
#    host user.
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
echo "==> Syncing documentation source to $DOC_WORK"
mkdir -p "$DOC_WORK"
rsync -a --delete \
    --exclude='/tmp/' \
    --exclude='/.git/' \
    "$SCRIPT_DIR/" "$DOC_WORK/"

# 2. Build the docker image (only if it's not already built).
if ! "$DOCKER" image inspect "$IMAGE_NAME" >/dev/null 2>&1; then
    echo "==> Building docker image $IMAGE_NAME"
    "$DOCKER" build --tag "$IMAGE_NAME" "$SCRIPT_DIR/generator/build"
else
    echo "==> Reusing docker image $IMAGE_NAME (delete it to rebuild)"
fi

# 3. Run the build inside the container.
# main.sh expects /nt/{documentation,core,nova,enterprise,masterfiles,nt-docs}.
# We bind-mount this checkout as /nt/documentation and each tmp/<repo> as
# its sibling, so nothing outside this directory is touched.
echo "==> Running documentation build in container"
RUN_FLAGS=(
    --rm
    -v "$DOC_WORK:/nt/documentation"
)
for entry in "${REPOS[@]}"; do
    # shellcheck disable=SC2086
    set -- $entry
    RUN_FLAGS+=(-v "$WORK_DIR/$1:/nt/$1")
done

"$DOCKER" run "${RUN_FLAGS[@]}" "$IMAGE_NAME" \
    bash -x documentation/generator/build/main.sh \
        "$BRANCH" "$PACKAGE_JOB" "$PACKAGE_UPLOAD_DIRECTORY" \
        "$PACKAGE_BUILD" "$LTS_VERSION"

# 4. Optionally package the result (mirrors the Jenkins pipeline).
if [ -z "${SKIP_PUBLISH:-}" ]; then
    echo "==> Packaging output"
    "$DOCKER" run "${RUN_FLAGS[@]}" "$IMAGE_NAME" \
        bash -x documentation/generator/_scripts/_publish.sh "$BRANCH"
fi

echo "==> Done. Generated site is in: $DOC_WORK/generator/_site"
echo "    Tarballs (if packaged) are in: $DOC_WORK/output/"
