#!/bin/bash

## /home/vagrant/_json is updated via MP API test run.
## if content changed, make commits and create pull request
## do not update working copies of generator in $WRKDIR
## - only once pull request is merged
cd /home/vagrant/documentation-generator
git fetch original
git reset --hard original/master
git clean -dfx
cp -r /home/vagrant/_json /home/vagrant/documentation-generator
cp -r /home/vagrant/doc_help /home/vagrant/documentation-generator/_generated
cd /home/vagrant/documentation-generator/_json
DIFF=$(git diff -- .)

SYNTAX_DIFF=$(git diff -- syntax_map.json)
if [ ! -z "$SYNTAX_DIFF" ]; then
   git add syntax_map.json
   git commit -m "Autocommit: syntax map changed `date +%F-%T`"
fi

cd lib
LIB_DIFF=$(git diff -- .)
if [ ! -z "$LIB_DIFF" ]; then
   git add -A .
   git commit -m "Autocommit: libraries changed `date +%F-%T`"
fi

cd /home/vagrant/documentation-generator/_generated/doc_help
HELP_DIFF=$(git diff -- .)
if [ ! -z "$HELP_DIFF" ]; then
   git add -A .
   git commit -m "Autocommit: help text changed `date +%F-%T`"
fi

if [ ! -z "$DIFF" ]; then
   git push -f
   /home/vagrant/bin/hub pull-request "Auto Pull Request" -b cfengine:master -h cfengine-autobuild:autocheckSyntaxMap
fi
cd /home/vagrant/documentation-generator


sed '/^\[.*\[.*\].*\]/d' $WRKDIR/documentation-generator/_references.md > $WRKDIR/documentation-generator/new_references.md
mv $WRKDIR/documentation-generator/new_references.md $WRKDIR/documentation-generator/_references.md

mkdir $WRKDIR/documentation-generator/pages
rm -rf $WRKDIR/documentation-generator/.git
rm -rf $WRKDIR/documentation/.git
rm -rf $WRKDIR/core/.git
cp -r $WRKDIR/documentation/* $WRKDIR/documentation-generator/pages
cd $WRKDIR/documentation-generator
source /home/vagrant/.rvm/scripts/rvm
echo "Latest jekyll run :$BUILD_ID" > $WRKDIR/output.log
echo "Based on latest git commit :$GIT_COMMIT" >> $WRKDIR/output.log
echo "*********************************************************" >> $WRKDIR/output.log
echo "*                  CONSOLE OUTPUT                       *" >> $WRKDIR/output.log
echo "*********************************************************" >> $WRKDIR/output.log
jekyll
$WRKDIR/documentation-generator/_scripts/cfdoc_postprocess.py
#$WRKDIR/documentation-generator/_scripts/_create_pdf.sh
