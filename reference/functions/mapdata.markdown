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
or parsed as JSON when `interpretation` is `json`, or collected from `pattern`,
invoked as a program, when `interpretation` is `json_pipe`.

[This function can accept many types of data parameters.][Functions#collecting functions]

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

**json_pipe**

The `json_pipe` interpretation is intended to work with programs that take JSON
as input and produce JSON as output. This is a standard tool convention in the
Unix world. See the example below for the typical usage.

[jq](https://stedolan.github.io/jq/) has a powerful programming language that
fits the `json_pipe` interpretation well. It will take JSON input and product
JSON output. Please read the [jq](https://stedolan.github.io/jq/) manual and
cookbook to get a feel for the power of this tool. When available,
[jq](https://stedolan.github.io/jq/) will offer tremendous data manipulation
power for advanced cases where the built-in CFEngine functions are not enough.

**Example with json_pipe:**

[%CFEngine_include_snippet(mapdata_jsonpipe.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(mapdata_jsonpipe.cf, #\+begin_src\s+output\s*, .*end_src)%]


**History:** Was introduced in 3.7.0. `canonify` mode was introduced in 3.9.0. The [collecting function][Functions#collecting functions] behavior was added in 3.9. The `json_pipe` mode was added in 3.9.

**See also:** `maplist()`, `maparray()`, `canonify()`, [about collecting functions][Functions#collecting functions], and `data` documentation.
