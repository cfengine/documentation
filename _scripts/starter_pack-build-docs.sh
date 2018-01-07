#!/usr/bin/env bash

# build instructions pulled from Jenkins

export WRKDIR=/northern.tech/cfengine

cd $WRKDIR/masterfiles
NO_CONFIGURE=1 ./autogen.sh

cd $WRKDIR

$WRKDIR/documentation-generator/_scripts/cfdoc_bootstrap.py master

# Prepare core for syntax docs
cd /northern.tech/cfengine/core
./configure --with-lmdb=/usr/local --without-pam
make

export WRKDIR=/northern.tech/cfengine
cd /northern.tech/cfengine/documentation-generator

# Generate syntax data
source ~/.profile
source ~/.rvm/scripts/rvm

bash -x ./_regenerate_json.sh

# Preprocess Documentation with custom macros
./_scripts/cfdoc_preprocess.py master

# Build docs
bash -x ./_scripts/_run_jekyll.sh master

#strip leading slash from assets
#in the _site directory
find ./_site/ -name "*.html" | xargs sed -i "s|/docs/master/||g"
