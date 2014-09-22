#!/bin/bash
$WRKDIR/core/cf-promises/cf-promises -sjson > _generated/syntax_map.json

for lib in $WRKDIR/masterfiles/lib/3.7/*.cf
do
  out="${lib/..\/masterfiles/_generated}"
  out="${out/%.cf/.json}"
  $WRKDIR/core/cf-promises/cf-promises --eval-functions --policy-output-format=json $lib > $out
done

