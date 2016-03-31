---
layout: default
title: parsestringarrayidx
published: true
tags: [reference, io functions, functions, parsestringarrayidx]
---

[%CFEngine_function_prototype(array, input, comment, split, maxentries, maxbytes)%]

**Description:** Populates the two-dimensional array `array` with up to
`maxentries` fields from the first `maxbytes` bytes of the string `input`.

This function mirrors the exact behavior of `readstringarrayidx()`, but
reads data from a variable instead of a file. By making data readable from a variable, data driven policies can be kept inline.

The `comment` field is a multiline regular expression and will strip out
unwanted patterns from the file being read, leaving unstripped characters to be
split into fields. Using the empty string (`""`) indicates no comments.

[%CFEngine_function_attributes(array, input, comment, split, maxentries, maxbytes)%]

**Example:**

[%CFEngine_include_snippet(parsestringarrayidx.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(parsestringarrayidx.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Was introduced in version 3.1.5, Nova 2.1.0 (2011)
