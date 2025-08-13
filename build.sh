#!/usr/bin/env bash
set -ex
if [ ! -d documentation ]; then
  echo "Run this script from a top-level dir containing documentation and other repositories."
  exit 42
fi
command -v parallel || sudo apt install -y parallel
command -v buildah || sudo apt install -y buildah
export REPOS="core enterprise nova masterfiles northerntechhq/nt-docs"
export BASE_BRANCH="master"
export CORE_REV="$BASE_BRANCH"
export ENTERPRISE_REV="$BASE_BRANCH"
export NOVA_REV="$BASE_BRANCH"
export MASTERFILES_REV="$BASE_BRANCH"
export DOCS_REV="$BASE_BRANCH"
export NT_DOCS_REV="$BASE_BRANCH"

export DOCS_BRANCH="master"
export PACKAGE_JOB="cf-remote"
export PACKAGE_UPLOAD_DIRECTORY="n/a"
export PACKAGE_BUILD="n/a"
./buildscripts/ci/create-revisions-file.sh
cat revisions
curl -O https://gitlab.com/Northern.tech/OpenSource/GODS/-/raw/master/parallel_git_rev_fetch.sh
chmod u+x ./parallel_git_rev_fetch.sh
bash -x ./parallel_git_rev_fetch.sh revisions
BRANCH=${DOCS_BRANCH} bash -x ./documentation/generator/build/run.sh
