---
layout: default
title: "parse[int|real|string]array"
published: true
tags: [reference, io functions, functions, parseintarray, parserealarray, parsestringarray]
---

**Prototype:** `parseintarray(array, input, comment, split, maxentries, maxbytes)`<br>
**Prototype:** `parserealarray(array, input, comment, split, maxentries, maxbytes)`<br>
**Prototype:** `parsestringarray(array, input, comment, split, maxentries, maxbytes)`<br>

**Return type:** `int`

**Description:** Parses up to `maxentries` values from the first `maxbytes`
bytes in string `input` and populates `array`. Returns the dimension.

These functions mirror the exact behavior of their
[`read[int|real|string]array()`][readstringarray] counterparts, but read data from a variable
instead of a file. By making data readable from a variable, data driven
policies can be kept inline.

**Arguments**:

* `array` : Array identifier to populate, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`
* `input` : A string to parse for input data, in the range `"?(/.*)`
* `comment` : [Unanchored][unanchored] regex matching comments, in the range `.*`
* `split` : [Unanchored][unanchored] regex to split data, in the range `.*`
* `maxentries` : Maximum number of entries to read, in the range
`0,99999999999`
* `maxbytes` : Maximum bytes to read, in the range `0,99999999999`

**Example:**

[%CFEngine_include_snippet(parseintrealstringarray.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(parseintrealstringarray.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Was introduced in version 3.1.5a1, Nova 2.1.0 (2011)
