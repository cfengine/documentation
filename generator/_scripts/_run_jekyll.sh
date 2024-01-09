#!/bin/bash

if [ -z "$WRKDIR" ]
then
    echo Environment WRKDIR is not set, setting it to current working directory
    WRKDIR=`pwd`
    export WRKDIR
fi

echo "Generating documentation from '$WRKDIR'..."

sed '/^\[.*\[.*\].*\]/d' $WRKDIR/documentation/generator/_references.md > $WRKDIR/documentation/generator/new_references.md
mv $WRKDIR/documentation/generator/new_references.md $WRKDIR/documentation/generator/_references.md

mkdir $WRKDIR/documentation/generator/pages
cp -r $WRKDIR/documentation/* $WRKDIR/documentation/generator/pages
rm -rf $WRKDIR/documentation/generator/pages/generator
# remove not published .markdown files
find $WRKDIR/documentation/generator/pages -type f -name "*.markdown" -exec grep -l '^published: false$' {} + | xargs rm -f
cd $WRKDIR/documentation/generator


echo "Latest jekyll run :$BUILD_ID" > $WRKDIR/output.log
echo "Based on latest git commit :$GIT_COMMIT" >> $WRKDIR/output.log
echo "*********************************************************" >> $WRKDIR/output.log
echo "*                  CONSOLE OUTPUT                       *" >> $WRKDIR/output.log
echo "*********************************************************" >> $WRKDIR/output.log
set -x
jekyll
if [ "$?" -gt "0" ]; then
    exit 1;
fi

$WRKDIR/documentation/generator/_scripts/cfdoc_postprocess.py "$@"
if [ "$?" -gt "0" ]; then
    exit 2;
fi

$WRKDIR/documentation/generator/_scripts/_create_pdf.sh
if [ "$?" -gt "0" ]; then
    exit 3;
fi
