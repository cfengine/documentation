---
layout: default
title: shuffle
published: true
tags: [reference, data functions, functions, shuffle]
---

[%CFEngine_function_prototype(list, seed)%]

**Description:** Return `list` shuffled with `seed`.

The same seed will produce the same shuffle every time. For a random shuffle, 
provide a random seed with the `randomint` function.

[%CFEngine_function_attributes(list, seed)%]

**Example:**

[%CFEngine_include_snippet(shuffle.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(shuffle.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** [`sort()`][sort].
