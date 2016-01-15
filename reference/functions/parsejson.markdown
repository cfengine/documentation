---
layout: default
title: parsejson
published: true
tags: [reference, io functions, functions, parsejson, json, container]
---

[%CFEngine_function_prototype(json_data)%]

**Description:** Parses JSON data directly from an inlined string and
returns the result as a `data` variable

[%CFEngine_function_attributes(json_data)%]

Please note that because JSON uses double quotes, it's usually most
convenient to use single quotes for the string (CFEngine allows both
types of quotes around a string).

**NOTE** that the `json_data` can contain variable references. This is
standard across many CFEngine functions and explained in the
`mergedata()` documentation.

**Example:**

```cf3
    vars:

      "loadthis"

         data =>  parsejson('{ "key": "value" }');

      # inline syntax since 3.7
      "loadthis_inline"

         data =>  '{ "key": "value" }';
```

**See also:** `readjson()`, `parseyaml()`, `readyaml()`, `mergedata()`, `Inline YAML and JSON data`, and `data` documentation.
