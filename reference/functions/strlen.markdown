---
layout: default
title: strlen
categories: [Reference, Functions, strlen]
published: true
alias: reference-functions-strlen.html
tags: [reference, text functions, functions, text, strlen, substring]
---

[%CFEngine_function_prototype(data)%]

**Description:** Returns the byte length of `data`.

[%CFEngine_function_attributes(data)%]

**Example:**

[%CFEngine_include_snippet(strlen.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(strlen.cf, #\+begin_src\s+example_output\s*[ ,.0-9]+, .*end_src)%]

**History:** Introduced in CFEngine 3.6

**See also:** `head()`, `tail()`, `reversestring()`.
