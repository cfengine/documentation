#!/bin/bash
for in in ../masterfiles/lib/3.6/*.cf
do
  out="${in/..\/masterfiles/_json}"
  out="${out/%.cf/.json}"
  ../core/cf-promises/cf-promises --policy-output-format=json $in > $out
done

