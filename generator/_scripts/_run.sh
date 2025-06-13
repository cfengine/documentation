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
cp -r $WRKDIR/documentation/content/* $WRKDIR/documentation/generator/pages
cp -r $WRKDIR/documentation/generator/_includes/lts_versions_list.html $WRKDIR/documentation/hugo/static/
cp -rf $WRKDIR/documentation/generator/_includes/versions_list.html $WRKDIR/documentation/hugo/static/
cp -rf $WRKDIR/documentation/generator/_includes/header_nav_options.html $WRKDIR/documentation/hugo/layouts/partials/
rm -rf $WRKDIR/documentation/generator/pages/generator
# remove not published .markdown files
find $WRKDIR/documentation/generator/pages -type f -name "*.markdown" -exec grep -l '^published: false$' {} + | xargs rm -f
mkdir $WRKDIR/documentation/hugo/content
cp -rf $WRKDIR/documentation/generator/pages/* $WRKDIR/documentation/hugo/content

# Hugo build
cp -rn $WRKDIR/nt-docs/* $WRKDIR/documentation/hugo/
cd $WRKDIR/documentation/hugo
npm ci
npm run build:all

cd $WRKDIR/documentation/generator
cp -rf $WRKDIR/documentation/hugo/scripts/search/index/searchIndex $WRKDIR/documentation/generator/_site/assets/

$WRKDIR/documentation/generator/_scripts/cfdoc_postprocess.py "$@"
if [ "$?" -gt "0" ]; then
    exit 2;
fi
