---
layout: default
title: difference
published: true
tags: [reference, data functions, functions, difference]
---

[%CFEngine_function_prototype(list1, list2)%]

**Description:** Returns the unique elements in `list1` that are not in
`list2`.

[%CFEngine_function_attributes(list1, list2)%]

**Example:**

[%CFEngine_include_snippet(difference.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(difference.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** [`intersection()`][intersection].
