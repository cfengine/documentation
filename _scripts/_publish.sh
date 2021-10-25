#!/bin/bash

VERSION=$1

if [ -z "$WRKDIR" ]
then
    echo Environment WRKDIR is not set, setting it to current working directory
    WRKDIR=`pwd`
    export WRKDIR
fi

cd $WRKDIR
find documentation-generator/pages -name "*.markdown" | xargs rm
cp `find documentation-generator/pages -name "*.*"` documentation-generator/_site
if [  ! -d documentation-generator/_site ]; then
  exit 1
fi

OUTPUT=$WRKDIR/output
mkdir -p $OUTPUT

# replace absolute style and script links with relative ones. This way, no
# matter how docs will be served (on https://docs.cfengine.com/docs/3.18/ or
# http://buildcache.cfengine.com/packages/build-documentation-pr/jenkins-pr-pipeline-7204/output/_site/),
# these links will still be valid.
cd documentation-generator/_site
for source in *.html;
do
  sed -i "s/<base href\([^>]*\)>/<!-- base href\1 -->/
          s/<link href='.*assets\(.*\)>/<link href='assets\1>/
          s/<script src='.*assets\(.*\)>/<script src='assets\1>/" $source
done
cd -

# Pack the site for transfer (its faster to transfer one big file than thousands of small ones)
# This archive is expected to be unpacked by the build system after the artifacts have been moved to their storage location
tar -czvf $OUTPUT/packed-for-shipping.tar.gz -C documentation-generator _site

ARCHIVE_FILE=cfengine-documentation-$VERSION
echo "Creating $ARCHIVE_FILE..."
cd documentation-generator/_site
# Disable interactive elements (selects and forms) since they won't be working
# in the downloaded archive
for source in *.html;
do
  sed -i "s/<select/<!-- select/
          s/<\/select>/<\/select -->/
          s/<form/<!-- from/
          s/<\/form>/<\/form -->/" $source
done
cd ..
tar -czf $OUTPUT/$ARCHIVE_FILE.tar.gz _site

ls -al $OUTPUT
