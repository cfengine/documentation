---
layout: default
title: string_downcase
aliases:
  - "/reference-functions-string_downcase.html"
---

{{< CFEngine_function_prototype(data) >}}

**Description:** Returns `data` in lower case.

{{< CFEngine_function_attributes(data) >}}

**Example:**

{{< CFEngine_include_snippet(string_downcase.cf, #\+begin_src cfengine3, .*end_src) >}}

Output:

{{< CFEngine_include_snippet(string_downcase.cf, #\+begin_src\s+example_output\s*, .*end_src) >}}

**History:** Introduced in CFEngine 3.6

**See also:** `string_upcase()`.
