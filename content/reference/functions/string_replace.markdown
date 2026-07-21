---
layout: default
title: string_replace
aliases:
  - "/reference-functions-string_replace.html"
---

{{< CFEngine_function_prototype(string, match, replacement, option) >}}

**Description:** Replaces a substring, or a list of substrings, within a given string with a specified replacement string or list of replacement strings.
{{< CFEngine_function_attributes(string, match, replacement, option) >}}

Reads a string from left to right, replacing the occurences of the second
argument with the third argument in order.

By default, the `option` parameter is set to `"strings"`, meaning the function expects `match` and `replacement` to be single strings. To use lists of strings instead, set option to `"lists"`. Lists can be passed as variables or inline JSON. However, their lengths must match exactly, as substitutions are applied pairwise. Note that mixing single string and list arguments is not supported.

All characters in the string to replace in, the substring to match for and the
replacement are read literally. This means that `.`, `*`, `\` and similar
characters will be read and replaced as they are. If you are looking for more
advanced replace functionality, check out `regex_replace()`.

**Example:**

{{< CFEngine_include_snippet(string_replace.cf, #\+begin_src cfengine3, .*end_src) >}}

**Output:**

{{< CFEngine_include_snippet(string_replace.cf, #\+begin_src\s+example_output\s*, .*end_src) >}}

**History:**

- Introduced in 3.12.1 (2018) as a simpler version of `regex_replace()`
- Added multiple string replacement via list or inline JSON in 3.29.0

**See also:** `regex_replace()`
