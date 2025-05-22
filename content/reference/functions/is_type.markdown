---
layout: default
title: is_type
---

[%CFEngine_function_prototype(var, type)%]

**Description:** Returns whether a variable `var` is of type `type`

[%CFEngine_function_attributes(var, type)%]

This function compares the type description of `var` with the string `type`. The function expects a variable identifier as the first argument and a type string as the second argument. The type accepts both the type and an optional subtype. The function evaluates to false by default if the variable or the type string is wrong.

To see the possible data types and their subtypes, see `type()`

**Example:**

[%CFEngine_include_snippet(is_type.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(is_type.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:**

* Introduced in 3.26.0
