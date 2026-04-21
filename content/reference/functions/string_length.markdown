---
layout: default
title: string_length
aliases:
  - "/reference-functions-string_length.html"
---

{{< CFEngine_function_prototype(data) >}}

**Description:** Returns the byte length of `data`.

{{< CFEngine_function_attributes(data) >}}

**Example:**

{{< CFEngine_include_snippet(string_length.cf, #\+begin_src cfengine3, .*end_src) >}}

Output:

{{< CFEngine_include_snippet(string_length.cf, #\+begin_src\s+example_output\s*, .*end_src) >}}

**History:** Introduced in CFEngine 3.6

**See also:** `string_head()`, `string_tail()`, `string_reverse()`.
