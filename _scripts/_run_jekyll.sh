#!/bin/bash
echo "Generating documentation from '$WRKDIR'..."

sed '/^\[.*\[.*\].*\]/d' $WRKDIR/documentation-generator/_references.md > $WRKDIR/documentation-generator/new_references.md
mv $WRKDIR/documentation-generator/new_references.md $WRKDIR/documentation-generator/_references.md

mkdir $WRKDIR/documentation-generator/pages
rm -rf $WRKDIR/documentation-generator/.git
rm -rf $WRKDIR/documentation/.git
rm -rf $WRKDIR/core/.git
cp -r $WRKDIR/documentation/* $WRKDIR/documentation-generator/pages
cd $WRKDIR/documentation-generator
source /home/jenkins/.rvm/scripts/rvm
echo "Latest jekyll run :$BUILD_ID" > $WRKDIR/output.log
echo "Based on latest git commit :$GIT_COMMIT" >> $WRKDIR/output.log
echo "*********************************************************" >> $WRKDIR/output.log
echo "*                  CONSOLE OUTPUT                       *" >> $WRKDIR/output.log
echo "*********************************************************" >> $WRKDIR/output.log
jekyll
if [ "$?" -gt "0" ]; then
   exit 1;
fi

$WRKDIR/documentation-generator/_scripts/cfdoc_postprocess.py
if [ "$?" -gt "0" ]; then
   exit 2;
fi

#$WRKDIR/documentation-generator/_scripts/_create_pdf.sh
if [ "$?" -gt "0" ]; then
   exit 3;
fi

