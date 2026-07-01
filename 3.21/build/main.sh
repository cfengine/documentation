#!/bin/bash

if [ "$#" != 4 ]; then
    echo "Pass 4 args, please:"
    echo BRANCH
    echo PACKAGE_JOB
    echo PACKAGE_UPLOAD_DIRECTORY
    echo PACKAGE_BUILD
    exit 1
fi

echo "$(basename "$0"): Diagnostic facts about execution environment:"
echo "======"
whoami
cat /etc/os-release
free -h
df -h
uname -a
echo "======"


export BRANCH=$1
export PACKAGE_JOB=$2
export PACKAGE_UPLOAD_DIRECTORY=$3
export PACKAGE_BUILD=$4

export JOB_TO_UPLOAD=$PACKAGE_JOB
export NO_OUTPUT_DIR=1

env
set -x

# take ownersip of all files
sudo chown -R jenkins:jenkins .

WRKDIR=$(pwd)
export WRKDIR

cd "$WRKDIR"/documentation/generator


### Download CFEngine:

# c https://github.com/cfengine/misc/blob/master/vagrant_quickstart/build.sh

function fetch_file() {
    # $1 -- URL to fetch
    # $2 -- destination
    # $3 -- number of tries (with 10s pauses) [optional, default=1]
    local target="$1"
    local destination="$2"
    local tries=1
    if [ $# -gt 2 ]; then
        tries="$3"
    fi
    local success=1                     # 1 means False in bash, 0 means True
    set +e
    for i in $(seq 1 "$tries"); do
        wget "$target" -O "$destination" && success=0 && break
        if [ "$i" -lt "$tries" ]; then
            sleep 10s
        fi
    done
    set -e
    return $success
}

set -ex

# these env variables must be set by calling script
test ! -z "$JOB_TO_UPLOAD"
test ! -z "$PACKAGE_UPLOAD_DIRECTORY"
test ! -z "$PACKAGE_BUILD"



echo "Install hub package"
if [ "$PACKAGE_JOB" = "cf-remote" ]; then
  echo "Install using cf-remote"
  sudo apt update -y
  sudo apt install -y python3-venv pipx
  pipx install cf-remote
  export PATH="$HOME/.local/bin:$PATH"
  # shellcheck source=/dev/null
  source /etc/os-release
  rm -rf ~/.cfengine/cf-remote/packages # to ensure we only get one
  # in case of LTS branches like 3.21 (without .x since we are in documentation repo) need to add on .x
  if [ "$(expr "$BRANCH" : ".*.x")" = 0 ]; then
    if [ "$BRANCH" = "master" ]; then
      _VERSION=master
    else
      _VERSION="$BRANCH".x
    fi
  else
    _VERSION="$BRANCH" # in case someone copy/pastes this to a repo besides documentation
  fi
  cf-remote --version "$_VERSION" download "${ID}$(echo "${VERSION_ID}" | cut -d. -f1)" hub "$(uname -m)"
  find "$HOME/.cfengine" # debug
  find "$HOME/.cfengine" -name '*.deb' -print0 | xargs -0 -I{} cp {} cfengine-nova-hub.deb
else
  echo "Installing with old-style fetch_file function"
  HUB_DIR_NAME=PACKAGES_HUB_x86_64_linux_ubuntu_22
  HUB_DIR_URL="http://buildcache.cfengine.com/packages/$PACKAGE_JOB/$PACKAGE_UPLOAD_DIRECTORY/$HUB_DIR_NAME/"
  HUB_PACKAGE_NAME="$(wget "$HUB_DIR_URL" -O- | sed '/\.deb/!d;s/.*"\([^"]*\.deb\)".*/\1/')"

  fetch_file "$HUB_DIR_URL$HUB_PACKAGE_NAME" "cfengine-nova-hub.deb" 12
fi

sudo apt-get -y purge cfengine-nova-hub || true
sudo rm -rf /*/cfengine

# we unpack the hub package instead of installing to get around trouble with the package trying to start up services in a container which doesn't work all that well (yet, 2025)
sudo dpkg --unpack cfengine-nova-hub.deb
rm cfengine-nova-hub.deb

# TODO: why copy the masterfiles from the package over the top of one we checked out which could have changes from a PR?
sudo cp -a /var/cfengine/share/NovaBase/masterfiles "$WRKDIR"
sudo chmod -R a+rX "$WRKDIR"/masterfiles

# write current branch into the config.yml
echo "branch: $BRANCH" >> "$WRKDIR"/documentation/generator/_config.yml

# Generate syntax data
./_regenerate_json.sh || exit 4

# Preprocess Documentation with custom macros
./_scripts/cfdoc_preprocess.py "$BRANCH" || exit 5

# rvm commands are insane scripts which pollut output
# so instead of set -x we just echo each command ourselves
set +x

# since May 14 2019, we need this to run jekyll. IDK why.
echo "+ source ~/.rvm/scripts/rvm"
# shellcheck disable=SC1090
source ~/.rvm/scripts/rvm
echo "+ rvm --default use 1.9.3-p551"
rvm --default use 1.9.3-p551
echo "+ source ~/.profile"
ls -lah ~
# shellcheck disable=SC1090
test -f ~/.profile && source ~/.profile
echo "+ source ~/.rvm/scripts/rvm"
# shellcheck disable=SC1090
source ~/.rvm/scripts/rvm

export LC_ALL=C.UTF-8

# finally, run actual jekyll
echo "+ bash -x ./_scripts/_run_jekyll.sh $BRANCH || exit 6"
bash -x ./_scripts/_run_jekyll.sh "$BRANCH" || exit 6

cd "$WRKDIR"/documentation/generator
npm run build
