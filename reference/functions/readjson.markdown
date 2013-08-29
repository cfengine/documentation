---
layout: default
title: readjson
categories: [Reference, Functions, readjson]
published: true
alias: reference-functions-readjson.html
tags: [reference, io functions, functions, readjson, json, container]
---

[%CFEngine_function_prototype(filename, maxbytes)%]

**Description:** Parses JSON data from the first `maxbytes` bytes of
file `filename` and returns the result as a `container` variable.

[%CFEngine_function_attributes(filename, maxbytes)%]

**Example:**

```cf3
    vars:

      "loadthis" 

         container =>  readjson("/tmp/data.json", 4000);
```

**See also:** [`parsejson()`][parsejson] and `container` documentation.
