---
layout: default
title: storejson
categories: [Reference, Functions, storejson]
published: true
alias: reference-functions-storejson.html
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

**See also:** `readjson()` and `data` documentation.
