---
layout: default
title: mapdata
published: true
tags: [reference, data functions, functions, mapdata, inline_json]
---

[%CFEngine_function_prototype(interpretation, pattern, array_or_container)%]

**Description:** Returns a data container holding a JSON array. The
array is a map across each element of `array_or_container`, modified by
a `pattern`. The map is either collected literally when `interpretation`
is `none`, or canonified when `interpretation` is `canonify`,
or parsed as JSON when `interpretation` is `json`.

This is a [Collecting Functions][collecting function] so it can accept many types of data parameters.

The `$(this.k)` and `$(this.v)` variables expand to the key and value
of the current element, similar to the way `this` is available for
`maplist`.

If the array or data container has two levels, you'll also be able to
use the `$(this.k[1])` variable for the key at the second level. See
the example below for an illustration.

The order of the keys is not guaranteed. Use the `sort()` function if
you need order in the resulting output.

[%CFEngine_function_attributes(interpretation, pattern, array_or_container)%]

**Example:**

[%CFEngine_include_snippet(mapdata.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(mapdata.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Was introduced in 3.7.0. `canonify` mode was introduced in 3.9.0. The [Collecting Functions][collecting function] behavior was added in 3.9.

**See also:** `maplist()`, `maparray()`, `canonify()`, [Collecting Functions][about collecting functions], and `data` documentation.
