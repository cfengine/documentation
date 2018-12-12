---
layout: default
title: countclassesmatching
published: true
tags: [reference, utility functions, functions, countclassesmatching]
---

[%CFEngine_function_prototype(regex, tag1, tag2, ...)%]

**Description:** Count the number of defined classes matching `regex`.

This function matches classes, using an [anchored][anchored] regular
expression that should match the whole line. The function returns the number
of classes matched.

You can optionally restrict the search by tags, which you can list after the regular expression.

[%CFEngine_function_attributes(regex, tag1, tag2, ...)%]

**Example:**

[%CFEngine_include_snippet(countclassesmatching.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(countclassesmatching.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** [classes defined via augments][Augments#classes], [classmatch()][classmatch], [classesmatching()][classesmatching] 
