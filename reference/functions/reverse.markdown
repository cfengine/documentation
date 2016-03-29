---
layout: default
title: reverse
published: true
tags: [reference, data functions, functions, reverse]
---

[%CFEngine_function_prototype(list)%]

**Description:** Reverses a list.

This is a simple function to reverse a list.

**Arguments**:

* list : The name of the list variable to check, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`

**Example:**


[%CFEngine_include_snippet(reverse.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(reverse.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** `filter()`, `grep()`, `every()`, `some()`, and `none()`.
