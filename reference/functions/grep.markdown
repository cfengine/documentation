---
layout: default
title: grep
categories: [Reference, Functions, grep]
published: true
alias: reference-functions-grep.html
tags: [reference, data functions, functions, grep]
---

[%CFEngine_function_prototype(regex, list)%]

**Description:** Returns the sub-list if items  in `list` matching the 
[anchored][anchored] regular expression `regex`.

[%CFEngine_function_attributes(regex, list)%]

**Example:**

[%CFEngine_include_snippet(grep.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(grep.cf, #\+begin_src\s+example_output\s*, .*end_src)%]
