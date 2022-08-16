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
cd $WRKDIR/documentation/generator

# rvm commands are insane scripts which pollut output
# so instead of set -x we just echo each command ourselves
set +x
if [ -e "/home/jenkins/.rvm/scripts/rvm" ]; then
  echo "+ /home/jenkins/.rvm/scripts/rvm"
  source /home/jenkins/.rvm/scripts/rvm
elif [ -e "$HOME/.rvm/scripts/rvm" ]; then
  echo "+ $HOME/.rvm/scripts/rvm"
  source $HOME/.rvm/scripts/rvm
else
    echo "ERROR: I couldn't source rvm from '/home/jenkins/.rvm/scripts/rvm' or '\$HOME/.rvm/scripts/rvm', probably jekyll won't work"
fi

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

