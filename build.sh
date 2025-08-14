#!/usr/bin/env bash
set -ex
if [ ! -d documentation ]; then
  echo "Run this script from a top-level dir containing documentation and other repositories."
  exit 42
fi
command -v parallel || sudo apt install -y parallel
command -v buildah || sudo apt install -y buildah
command -v curl || sudo apt install -y curl
command -v curl || sudo apt install -y curl

export REPOS="core enterprise nova masterfiles northerntechhq/nt-docs"
# running locally in a debian-12 virtualbox vagrant VM on MacOS I see the entire /nt aka pwd dir owned by random high uid/gid afterwards and needing re-owning
# sudo chown -R $USER .

# running locally I need to remove the repos before running the parallel fetch script
# for r in $REPOS; do rm -rf "$(basename "$r")"; done
export BASE_BRANCH="master"
export CORE_REV="$BASE_BRANCH"
export ENTERPRISE_REV="$BASE_BRANCH"
export NOVA_REV="$BASE_BRANCH"
export MASTERFILES_REV="$BASE_BRANCH"
export DOCS_REV="$main"
# todo: NT_DOCS_REV is defined in Jenkinsfile parameter but running locally we need to hard-code to main
export NT_DOCS_REV="main"

export DOCS_BRANCH="master"
export PACKAGE_JOB="cf-remote"
export PACKAGE_UPLOAD_DIRECTORY="n/a"
export PACKAGE_BUILD="n/a"
./buildscripts/ci/create-revisions-file.sh
cat revisions
curl -O https://gitlab.com/Northern.tech/OpenSource/GODS/-/raw/master/parallel_git_rev_fetch.sh
# todo: for local runs would be nice if parallel_git_rev_fetch.sh simply ensured that existing dirs were according to revisions file
chmod u+x ./parallel_git_rev_fetch.sh
# todo: add a debug option to see progress in parallel_git_rev_fetch.sh
bash -x ./parallel_git_rev_fetch.sh revisions

echo "fetch is done, running the build in a container"
BRANCH=${DOCS_BRANCH} bash -x ./documentation/generator/build/run.sh

