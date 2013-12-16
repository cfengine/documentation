---
layout: default
title: tail
categories: [Reference, Functions, tail]
published: true
alias: reference-functions-tail.html
tags: [reference, text functions, functions, text, tail, substring]
---

[%CFEngine_function_prototype(data, max)%]

**Description:** Returns the last `max` bytes of `data`.

[%CFEngine_function_attributes(data, max)%]

**Example:**

[%CFEngine_include_snippet(tail.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(tail.cf, #\+begin_src\s+example_output\s*[ ,.0-9]+, .*end_src)%]

**History:** Introduced in CFEngine 3.6

**See also:** `head()`, `strlen()`, `reversestring()`.
