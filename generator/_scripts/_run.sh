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

mkdir $WRKDIR/documentation/hugo/content
cp -r $WRKDIR/documentation/content/* $WRKDIR/documentation/hugo/content
cp -r $WRKDIR/documentation/generator/_includes/lts_versions_list.html $WRKDIR/documentation/hugo/static/
cp -rf $WRKDIR/documentation/generator/_includes/versions_list.html $WRKDIR/documentation/hugo/static/
cp -rf $WRKDIR/documentation/generator/_includes/header_nav_options.html $WRKDIR/documentation/hugo/layouts/partials/
# remove not published .markdown files
find $WRKDIR/documentation/hugo/content -type f -name "*.markdown" -exec grep -l '^published: false$' {} + | xargs rm -f
# remove .include.markdown files used in CFEngine_include_markdown function
find $WRKDIR/documentation/hugo/content -name "*.include.markdown" -type f -delete


# Hugo build
cp -rn $WRKDIR/nt-docs/* $WRKDIR/documentation/hugo/
cd $WRKDIR/documentation/hugo
npm ci
npm run build:all || exit 2

cd $WRKDIR/documentation/generator
mkdir -p $WRKDIR/documentation/generator/_site/assets/searchIndex
cp -rf $WRKDIR/documentation/hugo/scripts/search/index/searchIndex/* $WRKDIR/documentation/generator/_site/assets/searchIndex
cp -rf $WRKDIR/documentation/hugo/scripts/search/index/documents $WRKDIR/documentation/generator/_site/assets/searchIndex/documents
cp -f $WRKDIR/documentation/redirects.conf $WRKDIR/documentation/generator/_site/

$WRKDIR/documentation/generator/_scripts/cfdoc_postprocess.py "$@"
if [ "$?" -gt "0" ]; then
    exit 2;
fi
