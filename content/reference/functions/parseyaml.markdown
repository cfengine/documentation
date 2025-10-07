---
layout: default
title: parseyaml
aliases:
  - "/reference-functions-parseyaml.html"
---

{{< CFEngine_function_prototype(yaml_data) >}}

**Description:** Parses YAML data directly from an inlined string and
returns the result as a `data` variable

{{< CFEngine_function_attributes(yaml_data) >}}

Please note that it's usually most convenient to use single quotes for
the string (CFEngine allows both types of quotes around a string).

**Example:**

```cf3
vars:

  "loadthis"

  data =>  parseyaml('
- arrayentry1
- arrayentry2
- key1: 1
  key2: 2
');

  # inline syntax since 3.7
  # note the --- preamble is required with inline data
  "loadthis_inline"

  data =>  '---
- arrayentry1
- arrayentry2
- key1: 1
  key2: 2
';
```

**See also:** `readjson()`, `readyaml()`, `mergedata()`, `Inline YAML and JSON data`, and `data` documentation.
