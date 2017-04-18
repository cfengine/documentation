---
layout: default
title: string_head
published: true
tags: [reference, text functions, functions, text, head, string_head, substring]
---

[%CFEngine_function_prototype(data, max)%]

**Description:** Returns the first `max` bytes of `data`.

If `max` is negative, then everything but the last `max` bytes is returned.

[%CFEngine_function_attributes(data, max)%]

**Example:**

[%CFEngine_include_snippet(string_head.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(string_head.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Introduced in CFEngine 3.6

**See also:** `string_tail()`, `string_length()`, `string_reverse()`.
