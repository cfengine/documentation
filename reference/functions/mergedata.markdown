---
layout: default
title: mergedata
categories: [Reference, Functions, mergedata]
published: true
alias: reference-functions-mergedata.html
tags: [reference, data functions, functions, json, merge, mergedata, container]
---

[%CFEngine_function_prototype(one, two, etc)%]

**Description:** Returns the merger of any named data containers or lists.

The returned data container will have the keys from each of the named
data containers.

If all data containers are JSON arrays, they are merged into a single
array, as you'd expect from merging two arrays.

If any of the data containers are JSON objects, all the containers are
treated as JSON objects (for arrays, the key is the element's offset).

If any list (slist, ilist, or rlist) is named, it's first converted to
a JSON array, then merged as above.

`mergedata` is thus a convenient way, together with `getindices` and
`getvalues`, to bridge the gap between data container and the
traditional list data types in CFEngine.

[%CFEngine_function_attributes()%]

**Example:**

**Example:**

[%CFEngine_include_snippet(mergedata.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(mergedata.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** `getindices`, `getvalues`, `readjson()`, `parsejson()`, and `data` documentation.
