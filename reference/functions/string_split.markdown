---
layout: default
title: string_split
published: true
tags: [reference, data functions, functions, string_split]
---

[%CFEngine_function_prototype(string, regex, maxent)%]

**Description:** Splits `string` into at most `maxent` substrings wherever
`regex` occurs, and  returns the list with those strings.

The regular expression is [unanchored][unanchored].

If the maximum number of substrings is insufficient to accommodate all
the entries, the generated `slist` will have `maxent` items and the
last one will contain the rest of the string starting with the
`maxent-1`-th delimiter.  This is standard behavior in many languages
like Perl or Ruby, and different from the `splitstring()` behavior.

[%CFEngine_function_attributes(string, regex, maxent)%]

**Example:**

[%CFEngine_include_snippet(string_split.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(string_split.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Introduced in CFEngine 3.6; deprecates `splitstring()`.

**See also:** `splitstring()`

