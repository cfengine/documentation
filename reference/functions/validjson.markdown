---
layout: default
title: validjson
published: true
---

[%CFEngine_function_prototype(string, strict)%]

**Description:** Validates a JSON container from `string` and returns
`true` if the contents are valid JSON. An optional second argument `strict` may be used to enable strict validation. When set to `"true"` the function will not evaluate to true for JSON primitives.

[%CFEngine_function_attributes(string, strict)%]

**Example:**

Run:

[%CFEngine_include_snippet(validjson.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(validjson.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** `readjson()`, `validdata()`

**History:** Was introduced in 3.16.0.
