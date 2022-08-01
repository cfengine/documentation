---
layout: default
title: readfile
published: true
tags: [reference, io functions, functions, readfile]
---

[%CFEngine_function_prototype(filename, optional_maxbytes)%]

**Description:**
Returns the first `maxbytes` bytes from file `filename`.
`maxbytes` is optional, if specified, only the first `maxbytes` bytes are read from `filename`.
When `maxbytes` is `0`, `inf` or not specified, the whole file will be read (but see **Notes** below).

[%CFEngine_function_attributes(filename, optional_maxbytes)%]

**Example:**

Prepare:

[%CFEngine_include_snippet(readfile.cf, #\+begin_src prep, .*end_src)%]

Run:

[%CFEngine_include_snippet(readfile.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(readfile.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**

* On Windows, the file will be read in text mode, which means that
CRLF line endings will be converted to LF line endings in the
resulting variable. This can make the variable length shorter than the
size of the file being read.

**History:**

* Warnings about the size limit and the special `0` value were introduced in 3.6.0
* 4095 bytes limitation removed in 3.6.3


