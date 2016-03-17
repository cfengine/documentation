---
layout: default
title: grep
published: true
tags: [reference, data functions, functions, grep]
---

[%CFEngine_function_prototype(regex, list)%]

**Description:** Returns the sub-list if items  in `list` matching the 
[anchored][anchored] regular expression `regex`.

`list` can be a data container or a regular list.

[%CFEngine_function_attributes(regex, list)%]

**Example:**

[%CFEngine_include_snippet(grep.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(grep.cf, #\+begin_src\s+example_output\s*, .*end_src)%]
