#!/bin/bash

# Post-processes the site built in the hugo stage of build/Dockerfile.

if [ -z "$WRKDIR" ]
then
    echo Environment WRKDIR is not set, setting it to current working directory
    WRKDIR=`pwd`
    export WRKDIR
fi

export LC_ALL=C.UTF-8

cd $WRKDIR/documentation/generator
mkdir -p $WRKDIR/documentation/generator/_site/assets/searchIndex/documents
cp -rf $WRKDIR/documentation/hugo/scripts/search/index/searchIndex/* $WRKDIR/documentation/generator/_site/assets/searchIndex
cp -rf $WRKDIR/documentation/hugo/scripts/search/index/documents/* $WRKDIR/documentation/generator/_site/assets/searchIndex/documents/
cp -f $WRKDIR/documentation/redirects.conf $WRKDIR/documentation/generator/_site/

$WRKDIR/documentation/generator/_scripts/cfdoc_postprocess.py "$@"
if [ "$?" -gt "0" ]; then
    exit 2;
fi
