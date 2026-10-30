---
layout: default
title: regarray
aliases:
  - "/reference-functions-regarray.html"
---

{{< CFEngine_function_prototype(array, regex) >}}

**Description:** Returns whether `array` contains elements matching the
[anchored][anchored]regular expression `regex`.

{{< CFEngine_function_attributes(array, regex) >}}

`regarray()` will return as soon as any element matches.

**Example:**

{{< CFEngine_include_snippet(regarray.cf, #\+begin_src cfengine3, .*end_src) >}}

Output:

{{< CFEngine_include_snippet(regarray.cf, #\+begin_src\s+example_output\s*, .*end_src) >}}

**See also:** [short-circuit evaluation][Functions#short-circuit evaluation]
