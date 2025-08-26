#!/bin/bash

set -ex
trap "echo FAILURE" ERR

image_name=docs-revamp-22
if ! buildah inspect "$image_name" >/dev/null 2>&1; then
  buildah build-using-dockerfile -t "$image_name" documentation/generator/build
fi

# Current path must have the following repos cloned:
# * core (used for changelog, examples)
# * nova (used for changelog)
# * enterprise (used for changelog)
# * masterfiles (used to document masterfies)
# * documentation (this repo)

# The PACKAGE* vars are not needed for fast-build jobs as they use cf-remote --version $BRANCH install
# We still require them to have a value but by current convention (until cf-remote --version testing-pr-build-number works) we set them to cf-remote in documentation/Jenkinsfile
true "${PACKAGE_JOB?undefined}"
true "${PACKAGE_UPLOAD_DIRECTORY?undefined}"
true "${PACKAGE_BUILD?undefined}"

# figure out BRANCH from jenkins environment variables
if [ -n "$PR_BASE" ]; then
  # PR_BASE comes from documentation/Jenkinsfile and ${pullRequest.base}
  BRANCH="$PR_BASE"
elif [ -n "$BRANCH_NAME" ]; then
  # jenkins, for pull requests this will be e.g. PR-<number> so not used
  # for non-pull reqeusts this will be master, 3.24.x, etc
  BRANCH="$BRANCH_NAME"
fi

c=$(buildah from -v "$PWD":/nt "$image_name")
trap 'buildah run "$c" bash -c "sudo chown -R root:root /nt; sudo chmod -R a+rwX /nt"; buildah rm "$c" >/dev/null' EXIT
buildah run "$c" bash -x documentation/generator/build/main.sh "$BRANCH" "$PACKAGE_JOB" "$PACKAGE_UPLOAD_DIRECTORY" "$PACKAGE_BUILD"
buildah run "$c" bash -x documentation/generator/_scripts/_publish.sh "$BRANCH"
