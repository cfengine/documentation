---
layout: default
title: accessedbefore
categories: [Reference, Functions, accessedbefore]
published: true
alias: reference-functions-accessedbefore.html
tags: [reference, files functions, functions, accessedbefore]
---

[%CFEngine_function_prototype(newer,older)%]

**Description:** Compares the `atime` fields of two files.

Return true if `newer` was accessed before `older`.

[%CFEngine_function_attributes(newer, older)%]

**Example:**  


[%CFEngine_include_snippet(accessedbefore.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(accessedbefore.cf, #\+begin_src\s+example_output\s*[ ,.0-9]+, .*end_src)%]
