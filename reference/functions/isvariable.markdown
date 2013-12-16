---
layout: default
title: isvariable
categories: [Reference, Functions, isvariable]
published: true
alias: reference-functions-isvariable.html
tags: [reference, utility functions, functions, isvariable]
---

[%CFEngine_function_prototype(var)%]

**Description:** Returns whether a variable named `var` is defined.

The variable need only exist. This says nothing about its value. Use
`regcmp` to check variable values.

[%CFEngine_function_attributes(var)%]

**Example:**

[%CFEngine_include_snippet(isvariable.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(isvariable.cf, #\+begin_src\s+example_output\s*[ ,.0-9]+, .*end_src)%]
