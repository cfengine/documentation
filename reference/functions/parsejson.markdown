---
layout: default
title: parsejson
published: true
tags: [reference, io functions, functions, parsejson, json, container, inline_json]
---

[%CFEngine_function_prototype(json_data)%]

**Description:** Parses JSON data directly from an inlined string and
returns the result as a `data` variable

[%CFEngine_function_attributes(json_data)%]

Please note that because JSON uses double quotes, it's usually most
convenient to use single quotes for the string (CFEngine allows both
types of quotes around a string).

This is a [Collecting Functions][collecting function] so it can accept many types of data parameters.

**Example:**

```cf3
    vars:

      "loadthis"

         data =>  parsejson('{ "key": "value" }');

      # inline syntax since 3.7
      "loadthis_inline"

         data =>  '{ "key": "value" }';
```

**History:** The [Collecting Functions][collecting function] behavior was added in 3.9.

**See also:** `readjson()`, `parseyaml()`, `readyaml()`, `mergedata()`, `Inline YAML and JSON data`, [Collecting Functions][about collecting functions], and `data` documentation.
