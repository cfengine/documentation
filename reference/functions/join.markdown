---
layout: default
title: join
published: true
tags: [reference, data functions, functions, join, inline_json]
---

[%CFEngine_function_prototype(glue, list)%]

**Description:** Join the items of `list` into a string, using the conjunction in `glue`.

Converts a list or data container into a scalar variable using the
join string in first argument.

This is a [Collecting Functions][collecting function] so it can accept many types of data parameters.

[%CFEngine_function_attributes(glue, list)%]

**Example:**

[%CFEngine_include_snippet(join.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(join.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** The [Collecting Functions][collecting function] behavior was added in 3.9.

**See also:** `string_split()`, [Collecting Functions][about collecting functions].
