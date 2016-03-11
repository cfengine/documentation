---
layout: default
title: unique
published: true
tags: [reference, data functions, functions, unique, inline_json]
---

[%CFEngine_function_prototype(list)%]

**Description:** Returns list of unique elements from `list`.

This is a [Collecting Functions][collecting function] so it can accept many types of data parameters.

[%CFEngine_function_attributes(list)%]

**Example:**

[%CFEngine_include_snippet(unique.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(unique.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** The [Collecting Functions][collecting function] behavior was added in 3.9.

**See also:** `filter()`, [Collecting Functions][about collecting functions], and `data` documentation.
