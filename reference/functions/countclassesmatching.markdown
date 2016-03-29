---
layout: default
title: countclassesmatching
published: true
tags: [reference, utility functions, functions, countclassesmatching]
---

[%CFEngine_function_prototype(regex)%]

**Description:** Count the number of defined classes matching `regex`.

This function matches classes, using an [anchored][anchored] regular
expression that should match the whole line. The function returns the number
of classes matched.

[%CFEngine_function_attributes(regex)%]

**Example:**

[%CFEngine_include_snippet(countclassesmatching.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(countclassesmatching.cf, #\+begin_src\s+example_output\s*, .*end_src)%]
