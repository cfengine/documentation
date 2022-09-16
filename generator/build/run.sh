#!/bin/bash

set -ex
trap "echo FAILURE" ERR

if ! buildah inspect docs-revamp-22 >/dev/null 2>&1; then
  buildah build-using-dockerfile --security-opt seccomp=unconfined -t docs-revamp-22 documentation/generator/build
fi

# current path must have the following repos cloned:
# * core (used for changelog, examples)
# * nova (used for changelog)
# * enterprise (used for changelog)
# * masterfiles (used to document masterfies)
# * documentation (this repo)

# these env vars must be defined
true "${BRANCH?undefined}"
true "${PACKAGE_JOB?undefined}"
true "${PACKAGE_UPLOAD_DIRECTORY?undefined}"
true "${PACKAGE_BUILD?undefined}"

c=$(buildah from -v $PWD:/nt docs-revamp-22)
trap "buildah run $c bash -c 'sudo chmod -R a+rwX /nt'; buildah rm $c >/dev/null" EXIT
buildah run $c bash -x documentation/generator/build/main.sh $BRANCH $PACKAGE_JOB $PACKAGE_UPLOAD_DIRECTORY $PACKAGE_BUILD
buildah run $c bash -x documentation/generator/_scripts/_publish.sh $BRANCH

