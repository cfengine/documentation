#!/bin/bash

VERSION=$1
SERVER=$2
PORT=$3

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

cp -a documentation-generator/_site $OUTPUT

ARCHIVE_FILE=cfengine-documentation-$VERSION
echo "Creating $ARCHIVE_FILE..."
cd documentation-generator/_site
for source in *.html;
do
  sed -i "s/<base href\(.*\)>/<!-- base href\1 -->/" $source
  sed -i "s/<link href='.*assets\(.*\)>/<link href='assets\1>/" $source
  sed -i "s/<script src='.*assets\(.*\)>/<script src='assets\1>/" $source
  sed -i "s/<select/<!-- select/" $source
  sed -i "s/<\/select>/<\/select -->/" $source
  sed -i "s/<form/<!-- select/" $source
  sed -i "s/<\/form>/<\/form -->/" $source
done
cd ..
tar -czf $OUTPUT/$ARCHIVE_FILE.tar.gz _site
# Placing offline copy of docs into site directory
#mv $OUTPUT/$ARCHIVE_FILE.tar.gz _site/
#ls -al _site/$ARCHIVE_FILE.tar.gz
# Pack the site for transfer (its faster to transfer one big file than thousands of small ones)
# This archive is expected to be unpacked by the build system after the artifacts have been moved to their storage location
# tar -czvf $OUTPUT/packed-for-shipping.tar.gz _site/ && rm -rf _site/
