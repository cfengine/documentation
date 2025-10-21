---
layout: default
title: readjson
aliases:
  - "/reference-functions-readjson.html"
---

{{< CFEngine_function_prototype(filename, optional_maxbytes) >}}

**Description:** Parses JSON data from the file `filename` and returns the
result as a `data` variable. `maxbytes` is optional, if specified, only the
first `maxbytes` bytes are read from `filename`.

{{< CFEngine_function_attributes(filename, optional_maxbytes) >}}

**Example:**

```cf3 {skip TODO}
vars:

  "loadthis"

     data =>  readjson("/tmp/data.json", 4000);
```

**See also:** [`data_expand()`][data_expand], `readdata()`, `parsejson()`, `storejson()`, `parseyaml()`, `readyaml()`, `mergedata()`, `validjson()`, and `data` documentation.

**History:**

- Introduced in CFEngine 3.6.0
