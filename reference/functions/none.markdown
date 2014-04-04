---
layout: default
title: none
published: true
tags: [reference, data functions, functions, none]
---

[%CFEngine_function_prototype(regex, list)%]

**Description:** Returns whether no element in `list` matches the regular 
expression `regex`.

`list` can be a data container or a regular list.

[%CFEngine_function_attributes(regex, list)%]

The regular expression is [unanchored][unanchored].

**Example:**

[%CFEngine_include_snippet(none.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(none.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** [`filter()`][filter], [`every()`][every], and [`some()`][some].
