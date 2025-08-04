---
layout: default
title: readintlist
---

[%CFEngine_function_prototype(filename, comment, split, maxentries, maxbytes)%]

**Description:** Splits the file `filename` into separated
values and returns the list.

The `comment` field is a multiline regular expression and will strip out
unwanted patterns from the file being read, leaving unstripped characters to be
split into fields. Using the empty string (`""`) indicates no comments.

[%CFEngine_function_attributes(filename, comment, split, maxentries, maxbytes)%]

**Example:**

Prepare:

[%CFEngine_include_snippet(readintlist.cf, #\+begin_src prep, .*end_src)%]

Run:

[%CFEngine_include_snippet(readintlist.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(readintlist.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** [`readstringlist()`][readstringlist], [`readreallist()`][readreallist]
