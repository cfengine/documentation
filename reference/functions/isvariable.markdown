---
layout: default
title: isvariable
published: true
tags: [reference, utility functions, functions, isvariable]
---

[%CFEngine_function_prototype(var)%]

**Description:** Returns whether a variable named `var` is defined.

The variable need only exist. This says nothing about its value. Use
`regcmp` to check variable values. Variable references like `foo[bar]`
are also checked, so this is a way to check if a classic CFEngine
array or a data container has a specific key or element.

[%CFEngine_function_attributes(var)%]

**Example:**

[%CFEngine_include_snippet(isvariable.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(isvariable.cf, #\+begin_src\s+example_output\s*, .*end_src)%]
