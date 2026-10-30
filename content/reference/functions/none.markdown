---
layout: default
title: none
aliases:
  - "/reference-functions-none.html"
---

{{< CFEngine_function_prototype(regex, list) >}}

**Description:** Returns whether no element in `list` matches the regular
expression `regex`.

[This function can accept many types of data parameters.][Functions#collecting functions]

{{< CFEngine_function_attributes(regex, list) >}}

The regular expression is [unanchored][unanchored].

`none()` will return as soon as any element matches.

**Example:**

{{< CFEngine_include_snippet(none.cf, #\+begin_src cfengine3, .*end_src) >}}

Output:

{{< CFEngine_include_snippet(none.cf, #\+begin_src\s+example_output\s*, .*end_src) >}}

**History:**

- The [collecting function][Functions#collecting functions] behavior was added in 3.9.
- Returns as soon as an element matches in 3.29.0 (CFE-4272).

**See also:** [About collecting functions][Functions#collecting functions], [short-circuit evaluation][Functions#short-circuit evaluation], `filter()`, `every()`, and `some()`.
