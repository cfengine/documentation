---
layout: default
title: validdata
published: true
---

[%CFEngine_function_prototype(data_container, type, strict)%]

**Description:** Validates a JSON container from `data_container` and returns
`"true"` if the contents are valid JSON.
An optional second argument `strict` may be used to enable strict validation.
When set to `"true"` the function will not evaluate to true for JSON primitives.
The default value of `strict`is `"false"`.

The strict behavior matches the expectations in other parts of policy language.
Notably, `data` containers and functions like `readjson()` and `parsejson()` expect JSON containers (arrays and objects) not primitives.
Thus, using `validdata()` with `strict` set to `"true"` is an effective way to check if something can be parsed by those functions.

This function is intended to be expanded with functionality for validating
CSV and YAML files eventually, mirroring `readdata()`. If `type` is `JSON`,
it behaves the same as `validjson()`.

[%CFEngine_function_attributes(data_container, type, strict)%]

**Example:**

Run:

[%CFEngine_include_snippet(validdata.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(validdata.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** `readdata()`, `validjson()`

**History:** Was introduced in 3.16.0.
