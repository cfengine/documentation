---
layout: default
title: escape
published: true
tags: [reference, data functions, functions, escape]
---

[%CFEngine_function_prototype(text)%]

**Description:** Escape regular expression characters in `text`.

This function is useful for making inputs readable when a regular
expression is required, but the literal string contains special
characters. The function simply 'escapes' all the regular expression
characters, so that you do not have to.

[%CFEngine_function_attributes(path)%]

**Example:**


[%CFEngine_include_snippet(escape.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(escape.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

In this example, the string "192.168.2.1" is "escaped" to be equivalent to
"192\\.168\\.2\\.1", because without the backslashes, the regular expression
"192.168.2.1" will also match the IP ranges "192.168.201", "192.168.231", etc
(since the dot character means "match any character" when used in a regular
expression).

**Notes:**

**History:** This function was introduced in CFEngine version 3.0.4 (2010)
