---
layout: default
title: readjson
published: true
tags: [reference, io functions, functions, readjson, json, container]
---

[%CFEngine_function_prototype(filename, optional_maxbytes)%]

**Description:** Parses JSON data from the file `filename` and returns the
result as a `data` variable. `maxbytes` is optional, if specified, only the
first `maxbytes` bytes are read from `filename`.

[%CFEngine_function_attributes(filename, optional_maxbytes)%]

**Example:**

```cf3
    vars:

      "loadthis"

         data =>  readjson("/tmp/data.json", 4000);
```

**See also:** `readdata()`, `parsejson()`, `storejson()`, `parseyaml()`, `readyaml()`, `mergedata()`, and `data` documentation.
