---
layout: default
title: strcmp
published: true
tags: [reference, data functions, functions, strcmp]
---

[%CFEngine_function_prototype(string1, string2)%]

**Description:** Returns whether the two strings `string1` and `string2` match
exactly.

[%CFEngine_function_attributes(string1, string2)%]

**Example:**

[%CFEngine_include_snippet(strcmp.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(strcmp.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** `regcmp()`, `regline()`
