---
layout: default
title: storejson
published: true
tags: [reference, io functions, functions, storejson, json, inline_json, container]
---

[%CFEngine_function_prototype(data_container)%]

**Description:** Converts a data container to a JSON string.

This is a [collecting function][Functions#collecting functions] so it can accept many types of data parameters.

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

**History:** The [collecting function][Functions#collecting functions] behavior was added in 3.9.

**See also:** `readjson()`, `readyaml()`, `parsejson()`, `parseyaml()`, [about collecting functions][Functions#collecting functions], and `data` documentation.
