---
layout: default
title: string_tail
published: true
tags: [reference, text functions, functions, text, string_tail, tail, substring]
---

[%CFEngine_function_prototype(data, max)%]

**Description:** Returns the last `max` bytes of `data`.

If `max` is negative, then everything but the first `max` bytes is returned.

**Arguments:**

* `data`: `string`, in the range: `.*`
* `max`: `int`, in the range: `-99999999999,99999999999`

**Example:**

[%CFEngine_include_snippet(string_tail.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(string_tail.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Introduced in CFEngine 3.6

**See also:** `string_head()`, `string_length()`, `string_reverse()`.
