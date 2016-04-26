---
layout: default
title: unique
published: true
tags: [reference, data functions, functions, unique, inline_json]
---

[%CFEngine_function_prototype(list)%]

**Description:** Returns list of unique elements from `list`.

[This function can accept many types of data parameters.][Functions#collecting functions]

[%CFEngine_function_attributes(list)%]

**Example:**

[%CFEngine_include_snippet(unique.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(unique.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** The [collecting function][Functions#collecting functions] behavior was added in 3.9.

**See also:** `filter()`, [about collecting functions][Functions#collecting functions], and `data` documentation.
