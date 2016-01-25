---
layout: default
title: length
published: true
tags: [reference, data functions, functions, length]
---

[%CFEngine_function_prototype(list)%]

**Description:** Returns the length of `list`.

`list` can be a data container or a regular list.

**NOTE** that the `list` can be specified as inline JSON
instead of a separate variable. This is standard across many CFEngine
functions and explained in the `mergedata()` documentation.

[%CFEngine_function_attributes(list)%]

**Example:**

[%CFEngine_include_snippet(length.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(length.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** [`nth()`][nth], `mergedata()`.
