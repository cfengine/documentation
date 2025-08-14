#!/usr/bin/env bash
set -ex
if [ -z "$BUILDCACHE_ACCESS_PRIVATE_KEY_PATH" ]; then
  echo "BUILDCACHE_ACCESS_PRIVATE_KEY_PATH must be in environment to publish documentation build result to buildcache."
  exit 42
fi

eval $(ssh-agent -s)
ssh-add "$BUILDCACHE_ACCESS_PRIVATE_KEY_PATH"

rsync -avzn output/ buildcache.cloud.cfengine.com:upload/"$BUILD_TAG"/build-documentation-"$DOCS_BRANCH"/"$BUILD_TAG"/

ssh buildcache.cloud.cfengine.com <<EOF
set -ex
export WRKDIR=`pwd`

mkdir -p upload
mkdir -p output

# find two tarballs
archive=`find upload -name 'cfengine-documentation-*.tar.gz'`
tarball=`find upload -name packed-for-shipping.tar.gz`
echo "TARBALL: $tarball"
echo "ARCHIVE: $archive"

# unpack $tarball
cd `dirname $tarball`
echo tar zxvf packed-for-shipping.tar.gz
echo rm packed-for-shipping.tar.gz

# move $archive to the _site
echo mv $WRKDIR/$archive _site

ls -la
cd -

ls -la upload

# note: this triggers systemd job to AV-scan new files
# and move them to proper places
echo mv upload/* output
EOF
