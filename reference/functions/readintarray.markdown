---
layout: default
title: "readintarray"
published: true
tags: [reference, io functions, functions, readintarray]
---

**Prototype:** `readintarray(array, filename, comment, split, maxentries, maxbytes)`<br>

**Return type:** `int`

**Description:** Populates `array` with up to `maxentries` values, parsed from
the first `maxbytes` bytes in file `filename`.

Reads a two dimensional array from a file. One dimension is separated by the
regex `split`, the other by the lines in the file. The first field of the
lines names the first array argument.

The `comment` field is a multiline regular expression and will strip out
unwanted patterns from the file being read, leaving unstripped characters to be
split into fields. Using the empty string (`""`) indicates no comments.

Returns the number of keys in the array, i.e., the number of
lines matched.

**Arguments**:

* `array` : Array identifier to populate, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`
* `filename` : File name to read, in the range `"?(/.*)`
* `comment` : [Unanchored][unanchored] regex matching comments, in the range `.*`
* `split` : [Unanchored][unanchored] regex to split lines into fields, in the range `.*`
* `maxentries` : Maximum number of entries to read, in the range
`0,99999999999`
* `maxbytes` : Maximum bytes to read, in the range `0,99999999999`

**Example:**

Prepare:

[%CFEngine_include_snippet(readintarray.cf, #\+begin_src prep, .*end_src)%]

Run:

[%CFEngine_include_snippet(readintarray.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(readintarray.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See Also:** [`readstringarray()`][readstringarray], [`readrealarray()`][readrealarray], [`parseintarray()`][parseintarray], [`parserealarray()`][parserealarray], [`parsestringarray()`][parsestringarray] 
