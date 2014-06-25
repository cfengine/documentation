---
layout: default
title: readcsv
published: true
tags: [reference, io functions, functions, readcsv, CSV, container]
---

[%CFEngine_function_prototype(filename)%]

**Description:** Parses CSV data from the first 1 MB of
file `filename` and returns the result as a `data` variable.

While it may seem similar to `data_readstringarrayidx()` and
`data_readstringarray()`, the `readcsv()` function is more capable
because it follows [RFC 4180][http://www.ietf.org/rfc/rfc4180.txt],
especially regarding quoting. This is not possible if you just split
strings on a regular expression delimiter.

The returned data is in the same format as
`data_readstringarrayidx()`, that is, a data container that holds a
JSON array of JSON arrays.

[%CFEngine_function_attributes(filename)%]

**Example:**

Prepare:

[%CFEngine_include_snippet(readcsv.cf, #\+begin_src prep, .*end_src)%]

Run:

[%CFEngine_include_snippet(readcsv.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(readcsv.cf, #\+begin_src\s+example_output\s*, .*end_src)%]


**See also:** `data_readstringarrayidx()`,`data_readstringarray()`, `parsejson()`, `storejson()`, `mergedata()`, and `data` documentation.

**History:** Was introduced in 3.6.1.
