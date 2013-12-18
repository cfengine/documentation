---
layout: default
title: variablesmatching
categories: [Reference, Functions, variablesmatching]
published: true
alias: reference-functions-variablesmatching.html
tags: [reference, utility functions, functions, variablesmatching]
---

[%CFEngine_function_prototype(regex, tag1, tag2, ...)%]

**Description:** Return the list of variables matching `regex` and any tags given.

This function searches for the [unanchored][unanchored] regular expression in 
the list of currently defined variables.

When any tags are given, only the variables with those tags are returned.

[%CFEngine_function_attributes(regex, tag1, tag2, ...)%]

**Example:**  


[%CFEngine_include_snippet(variablesmatching.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(variablesmatching.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Introduced in CFEngine 3.6
