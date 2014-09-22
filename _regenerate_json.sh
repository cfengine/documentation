#!/bin/bash
OUTDIR=$WRKDIR/documentation-generator/_generated
mkdir -p $OUTDIR/lib/3.7
$WRKDIR/core/cf-promises/cf-promises -sjson > $OUTDIR/syntax_map.json

for lib in $WRKDIR/masterfiles/lib/3.7/*.cf
do
  out="${lib/$WRKDIR\/masterfiles/$OUTDIR}"
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

