#!/bin/bash

set -ex
trap "echo FAILURE" ERR

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

# The whole build runs in the Dockerfile stages (pre-process, Hugo, post-process) with the
# current path as build context. The tarballs end up in ./output for the Jenkins publish step.
# No --layers: each build starts fresh, so results are never stale and no cached copies of the workspace pile up on the host.
buildah build-using-dockerfile \
  --file documentation/generator/build/Dockerfile \
  --ignorefile documentation/generator/build/Dockerfile.dockerignore \
  --build-arg BRANCH="$BRANCH" \
  --build-arg PACKAGE_JOB="$PACKAGE_JOB" \
  --build-arg PACKAGE_UPLOAD_DIRECTORY="$PACKAGE_UPLOAD_DIRECTORY" \
  --build-arg PACKAGE_BUILD="$PACKAGE_BUILD" \
  --build-arg LTS_VERSION="$LTS_VERSION" \
  --output type=local,dest=output \
  .
