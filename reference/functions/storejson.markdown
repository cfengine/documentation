---
layout: default
title: storejson
published: true
tags: [reference, io functions, functions, storejson, json, container]
---

[%CFEngine_function_prototype(data_container)%]

**Description:** Converts a data container to a JSON string.

[%CFEngine_function_attributes(data_container)%]

**Example:**

```cf3
   vars:

      "loadthis"
         data =>  readjson("/tmp/data.json", 4000);
      "andback"
         string =>  storejson(loadthis);
   reports:
      "Converted /tmp/data.json to '$(andback)'";
```

**See also:** `readjson()`, `readyaml()`, `parsejson()`, `parseyaml()`, and `data` documentation.
