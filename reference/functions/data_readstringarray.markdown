---
layout: default
title: data_readstringarray
published: true
tags: [reference, io functions, functions, data_readstringarray]
---

[%CFEngine_function_prototype(filename, comment, split, maxentries, maxbytes)%]

**Description:** Returns a data container (map) with up to
`maxentries`-1 fields from the first `maxbytes` bytes of file
`filename`.  The first field becomes the key in the map.

One dimension is separated by the regex `split`, the other by the
lines in the file. The array key (the first field) must be unique; if
you need to allow duplicate lines use `data_readstringarrayidx()`.

The `comment` field is a multiline regular expression and will strip out
unwanted patterns from the file being read, leaving unstripped characters to be
split into fields. Using the empty string (`""`) indicates no comments.

[%CFEngine_function_attributes(filename, comment, split, maxentries, maxbytes)%]

**Example:**

Prepare:

[%CFEngine_include_snippet(data_readstringarray.cf, #\+begin_src prep, .*end_src)%]

Run:

[%CFEngine_include_snippet(data_readstringarray.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(data_readstringarray.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** `data_readstringarrayidx()`, `data`
