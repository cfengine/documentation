---
layout: default
title: mean
published: true
tags: [reference, data functions, functions, mean, inline_json]
---

[%CFEngine_function_prototype(list)%]

**Description:** Return the mean of the numbers in `list`.

This is a [Collecting Functions][collecting function] so it can accept many types of data parameters.

[%CFEngine_function_attributes(list)%]

**Example:**

[%CFEngine_include_snippet(max-min-mean-variance.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(max-min-mean-variance.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Was introduced in version 3.6.0 (2014). The [Collecting Functions][collecting function] behavior was added in 3.9.

**See also:** `sort()`, `variance()`, `sum()`, `max()`, `min()`, [Collecting Functions][about collecting functions], and `data` documentation.
