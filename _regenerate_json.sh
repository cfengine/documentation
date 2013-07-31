#!/bin/bash
for in in ../core/masterfiles/lib/3.6/*.cf
do
  out="${in/..\/core\/masterfiles/_json}"
  out="${newname/%.cf/.json}"
  ../core/cf-promises/cf-promises --policy-output-format=json $in > $out
done

