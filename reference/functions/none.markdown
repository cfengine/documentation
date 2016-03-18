---
layout: default
title: none
published: true
tags: [reference, data functions, functions, none, inline_json]]
---

[%CFEngine_function_prototype(regex, list)%]

**Description:** Returns whether no element in `list` matches the regular 
expression `regex`.

This is a collecting function so it can accept many types of data parameters.

[%CFEngine_function_attributes(regex, list)%]

The regular expression is [unanchored][unanchored].

**Example:**

[%CFEngine_include_snippet(none.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(none.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** The collecting function behavior was added in 3.9.

**See also:** About collecting functions, `filter()`, `every()`, and `some()`.
