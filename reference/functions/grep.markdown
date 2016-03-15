---
layout: default
title: grep
published: true
tags: [reference, data functions, functions, grep, inline_json]
---

[%CFEngine_function_prototype(regex, list)%]

**Description:** Returns the sub-list if items  in `list` matching the 
[anchored][anchored] regular expression `regex`.

This is a [Collecting Functions][collecting function] so it can accept many types of data parameters.

[%CFEngine_function_attributes(regex, list)%]

**Example:**

[%CFEngine_include_snippet(grep.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(grep.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** The [Collecting Functions][collecting function] behavior was added in 3.9.

**See also:** [Collecting Functions][About collecting functions], `filter()`, `every()`, `some()`, and `none()`.
