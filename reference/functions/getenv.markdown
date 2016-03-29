---
layout: default
title: getenv
published: true
tags: [reference, system functions, functions, getenv]
---

[%CFEngine_function_prototype(variable, maxlength)%]

**Description:** Return the environment variable `variable`, truncated at
`maxlength` characters

Returns an empty string if the environment variable is not defined.
`maxlength` is used to avoid unexpectedly large return values, which could
lead to security issues. Choose a reasonable value based on the environment
variable you are querying.

[%CFEngine_function_attributes(variable, maxlength)%]

**Example:**

[%CFEngine_include_snippet(getenv.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(getenv.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**

**History:** This function was introduced in CFEngine version 3.0.4
(2010)
