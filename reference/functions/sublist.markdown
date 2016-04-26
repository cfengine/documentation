---
layout: default
title: sublist
published: true
tags: [reference, data functions, functions, sublist, inline_json]
---

[%CFEngine_function_prototype(list, head_or_tail, max_elements)%]

**Description:** Returns list of up to `max_elements` of `list`, obtained from head or tail depending on `head_or_tail`.

[This function can accept many types of data parameters.][Functions#collecting functions]

[%CFEngine_function_attributes(list, head_or_tail, max_elements)%]

**Example:**

[%CFEngine_include_snippet(sublist.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(sublist.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** The [collecting function][Functions#collecting functions] behavior was added in 3.9.

**See also:** `nth()`, `filter()`, [about collecting functions][Functions#collecting functions], and `data` documentation.
