---
layout: default
title: canonify
published: true
tags: [reference, data functions, functions, canonify]
---

[%CFEngine_function_prototype(text)%]

**Description:** Convert an arbitrary string `text` into a legal class name.

This function turns arbitrary text into class data.

[%CFEngine_function_attributes(text)%]

**Example:**


[%CFEngine_include_snippet(canonify.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(canonify.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** [classify()][classify], `canonifyuniquely()`.
