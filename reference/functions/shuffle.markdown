---
layout: default
title: shuffle
published: true
tags: [reference, data functions, functions, shuffle, inline_json]
---

[%CFEngine_function_prototype(list, seed)%]

**Description:** Return `list` shuffled with `seed`.

This is a [collecting function][Functions#collecting functions] so it can accept many types of data parameters.

The same seed will produce the same shuffle every time. For a random shuffle, 
provide a random seed with the `randomint` function.

[%CFEngine_function_attributes(list, seed)%]

**Example:**

[%CFEngine_include_snippet(shuffle.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(shuffle.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** The [collecting function][Functions#collecting functions] behavior was added in 3.9.

**See also:** `sort()`, [about collecting functions][Functions#collecting functions], and `data` documentation.
