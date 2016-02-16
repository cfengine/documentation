---
layout: default
title: splitstring
published: true
tags: [reference, data functions, functions, splitstring]
---

[%CFEngine_function_prototype(string, regex, maxent)%]

**Description:** Splits `string` into at most `maxent` substrings wherever
`regex` occurs, and  returns the list with those strings.

The regular expression is [unanchored][unanchored].

If the maximum number of substrings is insufficient to accommodate all
the entries, the final entry in the generated `slist` will contain the
rest of the un-split string.

[%CFEngine_function_attributes(string, regex, maxent)%]

**Example:**

[%CFEngine_include_snippet(splitstring.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(splitstring.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Deprecated in CFEngine 3.6 in favor of `string_split`

**See also:** `string_split()`
