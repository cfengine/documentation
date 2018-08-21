---
layout: default
title: string_replace
published: true
tags: [reference, data functions, functions, string_replace]
---

[%CFEngine_function_prototype(string, match, replacement)%]

**Description:** In a given string, replaces a substring with another string.

[%CFEngine_function_attributes(string, match, replacement)%]

Reads a string from left to right, replacing the occurences of the second
argument with the third argument in order.

All characters in the string to replace in, the substring to match for and the
replacement are read literally. This means that `.`, `*`, `\` and similar
characters will be read and replaced as they are. If you are looking for more
advanced replace functionality, check out `regex_replace()`.

**Example:**

[%CFEngine_include_snippet(string_replace.cf, #\+begin_src cfengine3, .*end_src)%]

**Output:**

[%CFEngine_include_snippet(string_replace.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Introduced in 3.12.1 (2018) as a simpler version of `regex_replace()`

**See also:** `regex_replace()`
