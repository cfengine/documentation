---
layout: default
title: readcsv
published: true
tags: [reference, io functions, functions, readcsv, CSV, container]
---

[%CFEngine_function_prototype(filename, optional_maxbytes)%]

**Description:**
Parses CSV data from the file `filename` and returns the result as a `data` variable.
`maxbytes` is optional, if specified, only the first `maxbytes` bytes are read from `filename`.

While it may seem similar to `data_readstringarrayidx()` and
`data_readstringarray()`, the `readcsv()` function is more capable
because it follows [RFC 4180](http://www.ietf.org/rfc/rfc4180.txt),
especially regarding quoting. This is not possible if you just split
strings on a regular expression delimiter.

The returned data is in the same format as
`data_readstringarrayidx()`, that is, a data container that holds a
JSON array of JSON arrays.

[%CFEngine_function_attributes(filename, optional_maxbytes)%]

**Example:**

Prepare:

[%CFEngine_include_snippet(readcsv.cf, #\+begin_src prep, .*end_src)%]

Run:

[%CFEngine_include_snippet(readcsv.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(readcsv.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Note:** CSV files formatted according to RFC 4180 must end with the `CRLF`
sequence. Thus a text file created on Unix with standard Unix tools
like vi will not, by default, have those line endings.

**See also:** `readdata()`, `data_readstringarrayidx()`,`data_readstringarray()`, `parsejson()`, `storejson()`, `mergedata()`, and `data` documentation.

**History:** Was introduced in 3.7.0.
