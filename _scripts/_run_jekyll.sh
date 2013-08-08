#!/bin/bash
DIFF=$(sudo diff /home/vagrant/syntax_map.json $WRKDIR/documentation-generator/_json/syntax_map.json)

if [ ! -z "$DIFF" ]; then
   cp /home/vagrant/syntax_map.json $WRKDIR/documentation-generator/_json/
   cp /home/vagrant/syntax_map.json /home/vagrant/documentation-generator/_json/
   cd /home/vagrant/documentation-generator
   git commit -a -m "autocommit syntax map changed `date +%F-%T`"
   git push -f
   /home/vagrant/bin/hub pull-request "Auto Pull Request" -b cfengine:master -h cfengine-autobuild:autocheckSyntaxMap
   cd ..
fi

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
$WRKDIR/documentation-generator/_scripts/_create_pdf.sh