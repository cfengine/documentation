---
layout: default
title: data_readstringarrayidx
published: true
tags: [reference, io functions, functions, data_readstringarrayidx]
---

[%CFEngine_function_prototype(filename, comment, split, maxentries, maxbytes)%]

**Description:** Returns a data container (array) with up to
`maxentries` fields from the first `maxbytes` bytes of file `filename`.

One dimension is separated by the regex `split`, the other by the lines in
the file. The array arguments are both integer indexes, allowing for
non-identifiers at first field (e.g. duplicates or names with spaces), unlike
`data_readstringarray()`.

The `comment` field will strip out unwanted patterns from the file being read, leaving unstripped characters to be split into fields. Using the empty string (`""`) indicates no comments.

[%CFEngine_function_attributes(filename, comment, split, maxentries, maxbytes)%]

**Example:**

Prepare:

[%CFEngine_include_snippet(data_readstringarray.cf, #\+begin_src prep, .*end_src)%]

Run:

[%CFEngine_include_snippet(data_readstringarray.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(data_readstringarray.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** `data_readstringarray()`, `data`

**History:**

* Added in CFEngine 3.6.0
