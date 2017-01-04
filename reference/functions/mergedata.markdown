---
layout: default
title: mergedata
published: true
tags: [reference, data functions, functions, json, merge, mergedata, container, wrap, extract, array, map, inline_json]
---

[%CFEngine_function_prototype(one, two, etc)%]

**Description:** Returns the merger of any named data containers or lists. Can
also wrap and unwrap data containers.

The returned data container will have the keys from each of the named
data containers, arrays, or lists.

If all the data containers are JSON arrays, they are merged into a
single array, as you'd expect from merging two arrays.

If any of the data containers are JSON objects, all the containers are
treated as JSON objects (for arrays, the key is the element's offset).

[This function can accept many types of data parameters.][Functions#collecting functions]

`mergedata()` is thus a convenient way, together with `getindices()` and
`getvalues()`, to bridge the gap between data container and the
traditional list and array data types in CFEngine.

**Note:** It is only possible to wrap data containers in the current namespace.

[%CFEngine_function_attributes()%]

**Example:**

[%CFEngine_include_snippet(mergedata.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(mergedata.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Was introduced in CFEngine 3.6.0 (2014). The [collecting function][Functions#collecting functions] behavior was added in 3.9.

**See also:** `getindices()`, `getvalues()`, `readjson()`, `parsejson()`, `readyaml()`, `parseyaml()`, [about collecting functions][Functions#collecting functions], and `data` documentation.
