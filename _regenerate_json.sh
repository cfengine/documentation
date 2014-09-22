#!/bin/bash
mkdir -p $WRKDIR/documentation-generator/_generated/lib/3.7
$WRKDIR/core/cf-promises/cf-promises -sjson > $WRKDIR/documentation-generator/_generated/syntax_map.json

for lib in $WRKDIR/masterfiles/lib/3.7/*.cf
do
  out="${lib/$WRKDIR\/masterfiles/$WRKDIR/documentation-generator/_generated}"
  out="${out/%.cf/.json}"
  $WRKDIR/core/cf-promises/cf-promises --eval-functions --policy-output-format=json $lib > $out
done

