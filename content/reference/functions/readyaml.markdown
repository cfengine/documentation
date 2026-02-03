---
layout: default
title: readyaml
aliases:
  - "/reference-functions-readyaml.html"
---

{{< CFEngine_function_prototype(filename, optional_maxbytes) >}}

**Description:** Parses YAML data from the file `filename` and returns the
result as a `data` variable. `maxbytes` is optional, if specified, only the
first `maxbytes` bytes are read from `filename`.

{{< CFEngine_function_attributes(filename, optional_maxbytes) >}}

**Example:**

```cf3 {skip TODO}
vars:

  "loadthis"

     data =>  readyaml("/tmp/data.yaml", 4000);
```

**See also:** [`data_expand()`][data_expand], `readdata()`, `parsejson()`, `parseyaml()`, `storejson()`, `mergedata()`, and `data` documentation.
