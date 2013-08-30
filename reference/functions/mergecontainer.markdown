---
layout: default
title: mergecontainer
categories: [Reference, Functions, mergecontainer]
published: true
alias: reference-functions-mergecontainer.html
tags: [reference, data functions, functions, json, merge, mergecontainer]
---

[%CFEngine_function_prototype(one, two, etc)%]

**Description:** Returns the merger of any named containers.

[%CFEngine_function_attributes()%]

**Example:**

```cf3
    bundle agent test
    {
      vars:
          "x" container => parsejson('{ "a": [1,2,3], "b": [] }')
          "y" container => parsejson('{ "b": [4,5,6] }')
          "merged" container => mergecontainer("x", "y");
    }
```

After the `mergecontainer` call, the `merged` container will have the
`a` key from `x` and the `b` key from `y`.

**See also:** `readjson()`, `parsejson()`, and `container` documentation.
