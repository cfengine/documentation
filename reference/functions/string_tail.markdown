---
layout: default
title: string_tail
categories: [Reference, Functions, string_tail]
published: true
alias: reference-functions-string_tail.html
tags: [reference, text functions, functions, text, string_tail, tail, substring]
---

[%CFEngine_function_prototype(data, max)%]

**Description:** Returns the last `max` bytes of `data`.

[%CFEngine_function_attributes(data, max)%]

**Example:**

[%CFEngine_include_snippet(string_tail.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(string_tail.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Introduced in CFEngine 3.6

**See also:** `string_head()`, `string_length()`, `string_reverse()`.
