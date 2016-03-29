---
layout: default
title: maparray
published: true
tags: [reference, data functions, functions, maparray]
---

[%CFEngine_function_prototype(pattern, array)%]

**Description:** Returns a list with each array element modified by a pattern.

The `$(this.k)` and `$(this.v)` variables expand to the key and value of the
array element, similar to the way `this` is available for `maplist`.

If a value in the array is an `slist`, you'll get one result for each
value (implicit looping).

The order of the array keys is not guaranteed.  Use the `sort`
function if you need order in the resulting output.

[%CFEngine_function_attributes(pattern, array)%]

**Example:**

[%CFEngine_include_snippet(maparray.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(maparray.cf, #\+begin_src\s+example_output\s*, .*end_src)%]
