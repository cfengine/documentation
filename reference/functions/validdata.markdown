---
layout: default
title: validdata
published: true
tags: [reference, functions, validdata, JSON, context]
---

[%CFEngine_function_prototype(data_container, type)%]

**Description:** Validates a JSON container from `data_container` and returns
`true` if the contents are valid JSON.

This function is intended to be expanded with functionality for validating
CSV and YAML files eventually, mirroring `readdata()`. If `type` is `JSON`,
it behaves the same as `validjson()`.

[%CFEngine_function_attributes(data_container, type)%]

**Example:**

Run:

[%CFEngine_include_snippet(validdata.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(validdata.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** `readdata()`, `validjson()`

**History:** Was introduced in 3.16.0.
