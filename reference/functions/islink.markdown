---
layout: default
title: islink
categories: [Reference, Functions, islink]
published: true
alias: reference-functions-islink.html
tags: [reference, files functions, functions, islink]
---

[%CFEngine_function_prototype(filename)%]

**Description:** Returns whether the named object `filename` is a symbolic 
link.

The link node must both exist and be a symbolic link. Hard links cannot
be detected using this function.

[%CFEngine_function_attributes(filename)%]

**Example:**

[%CFEngine_include_snippet(islink.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(islink.cf, #\+begin_src\s+example_output\s*[ ,.0-9]+, .*end_src)%]
