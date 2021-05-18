---
layout: default
title: FUNCTION NAME
published: false
tags: [reference, functions, more, tags]
---

[%CFEngine_function_prototype(arguments, here)%]

**Description:** Brief description of function.

**Return type:** `data|int|real|string|(i|r|s)list|class|(i|r)range|`

[%CFEngine_function_attributes(arguments, here)%]

Write a detailed description here.

**Example:**

The whole thing:

[%CFEngine_include_snippet(type.cf)%]

Or, selected sections:

[%CFEngine_include_snippet(type.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(type.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:**

* Introduced in VERSION
* Behavior foo added in VERSION
