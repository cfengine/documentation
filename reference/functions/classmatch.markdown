---
layout: default
title: classmatch
published: true
tags: [reference, utility functions, functions, classmatch]
---

[%CFEngine_function_prototype(regex)%]

**Description:** Tests whether `regex` matches any currently set class.

Returns true if the [anchored][anchored] regular expression matches any
currently defined class, otherwise returns false.

[%CFEngine_function_attributes(text)%]

**Example:**

[%CFEngine_include_snippet(classmatch.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(classmatch.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

