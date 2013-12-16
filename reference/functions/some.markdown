---
layout: default
title: some
categories: [Reference, Functions, some]
published: true
alias: reference-functions-some.html
tags: [reference, data functions, functions, some]
---

[%CFEngine_function_prototype(regex, list)%]

**Description:** Return whether any element of `list` matches the 
[Unanchored][unanchored] regular expression `regex`.

[%CFEngine_function_attributes(regex, list)%]

**Example:**

[%CFEngine_include_snippet(some.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(some.cf, #\+begin_src\s+example_output\s*[ ,.0-9]+, .*end_src)%]

**See also:** [`filter()`][filter], [`every()`][every], and [`none()`][none].
