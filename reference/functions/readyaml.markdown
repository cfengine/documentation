---
layout: default
title: readyaml
published: true
tags: [reference, io functions, functions, readyaml, yaml, json, container]
---

[%CFEngine_function_prototype(filename, maxbytes)%]

**Description:** Parses YAML data from the file `filename` and returns the
result as a `data` variable. `maxbytes` is optional, if specified, only the
first `maxbytes` bytes are read from `filename`.

[%CFEngine_function_attributes(filename, maxbytes)%]

**Example:**

```cf3
    vars:

      "loadthis"

         data =>  readyaml("/tmp/data.yaml", 4000);
```

**See also:** `readdata()`, `parsejson()`, `parseyaml()`, `storejson()`, `mergedata()`, and `data` documentation.
