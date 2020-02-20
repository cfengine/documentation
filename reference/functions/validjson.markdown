---
layout: default
title: validjson
published: true
tags: [reference, functions, validjson, JSON, context]
---

[%CFEngine_function_prototype(data_container)%]

**Description:** Validates a JSON container from `data_container` and returns
`true` if the contents are valid JSON.

[%CFEngine_function_attributes(data_container)%]

**Example:**

Run:

[%CFEngine_include_snippet(validjson.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(validjson.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** `readjson()`, `validdata()`

**History:** Was introduced in 3.16.0.
