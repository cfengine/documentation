---
layout: default
title: mergedata
published: true
tags: [reference, data functions, functions, json, merge, mergedata, container, wrap, extract, array, map]
---

[%CFEngine_function_prototype(one, two, etc)%]

**Description:** Returns the merger of any named data containers or lists.  Can also wrap and unwrap data containers.

The returned data container will have the keys from each of the named
data containers, arrays, or lists.

If all the data containers are JSON arrays, they are merged into a
single array, as you'd expect from merging two arrays.

If any of the data containers are JSON objects, all the containers are
treated as JSON objects (for arrays, the key is the element's offset).

If a key inside a data container is specified (`container[key]`), the
value under that key is extracted and merged. The key can be a string
for JSON objects or a number for JSON arrays. Note that a single data
container, CFEngine array, or slist can be named, in which case you're
simply extracting the contents of the data container into a new data
container.

If any list (slist, ilist, or rlist) is named, it's first converted to
a JSON array, then merged as above.

If any CFEngine "classic" array (`array[key]`) is named, it's first
converted to a JSON object, then merged as above.

`mergedata()` is thus a convenient way, together with `getindices()` and
`getvalues()`, to bridge the gap between data container and the
traditional list and array data types in CFEngine.

If any of the above-mentioned variables are named inside brackets like
`[ thing ]` then the `thing` will be wrapped in a JSON array and
**then** merged..

If any of the above-mentioned variables are named inside braces with a
key like `{ "newkey": thing }` then the `thing` will be wrapped
in a JSON object under key `newkey` and **then** merged.

[%CFEngine_function_attributes()%]

**Example:**

[%CFEngine_include_snippet(mergedata.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(mergedata.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** `getindices()`, `getvalues()`, `readjson()`, `parsejson()`, `readyaml()`, `parseyaml()`, and `data` documentation.
