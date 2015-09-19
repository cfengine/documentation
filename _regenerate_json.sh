#!/bin/bash

if [ -z "$WRKDIR" ]
then
    echo Environment WRKDIR is not set, setting it to current working directory
    WRKDIR=`pwd`
    export WRKDIR
fi

OUTDIR=$WRKDIR/documentation-generator/_generated
LIBDIR=$WRKDIR/masterfiles/lib
mkdir -p $OUTDIR/lib
$WRKDIR/core/cf-promises/cf-promises -sjson > $OUTDIR/syntax_map.json

for lib in $LIBDIR/*.cf
do
  out="${lib/$LIBDIR/$OUTDIR/lib}"
  out="${out/%.cf/.json}"
  $WRKDIR/core/cf-promises/cf-promises --eval-functions --policy-output-format=json $lib > $out
done

(
    echo cf-agent
    echo cf-promises
    echo cf-runagent
    echo cf-serverd
    echo cf-execd
    echo cf-key
    echo cf-monitord
) | while read agent
do
    $WRKDIR/core/$agent/$agent --help > $OUTDIR/$agent.help
done
