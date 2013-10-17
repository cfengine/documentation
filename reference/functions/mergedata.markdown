---
layout: default
title: mergedata
categories: [Reference, Functions, mergedata]
published: true
alias: reference-functions-mergedata.html
tags: [reference, data functions, functions, json, merge, mergedata, container]
---

[%CFEngine_function_prototype(one, two, etc)%]

**Description:** Returns the merger of any named data containers.

[%CFEngine_function_attributes()%]

**Example:**

```cf3
    bundle agent test
    {
      vars:
          "x" data => parsejson('{ "a": [1,2,3], "b": [] }')
          "y" data => parsejson('{ "b": [4,5,6] }')
          "merged" data => mergedata("x", "y");
    }
```

After the `mergedata` call, the `merged` data container will have the
`a` key from `x` and the `b` key from `y`.

**See also:** `readjson()`, `parsejson()`, and `data` documentation.
