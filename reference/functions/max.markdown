---
layout: default
title: max
published: true
tags: [reference, data functions, functions, max, inline_json]
---

[%CFEngine_function_prototype(list, sortmode)%]

**Description:** Return the maximum of the items in `list` according to `sortmode` (same sort modes as in `sort()`).

This is a [Collecting Functions][collecting function] so it can accept many types of data parameters.

[%CFEngine_function_attributes(list, sortmode)%]

**Example:**

[%CFEngine_include_snippet(max-min-mean-variance.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(max-min-mean-variance.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Was introduced in version 3.6.0 (2014). `canonify` mode was introduced in 3.9.0. The [Collecting Functions][collecting function] behavior was added in 3.9.

**See also:** `sort()`, `variance()`, `sum()`, `mean()`, `min()`, [Collecting Functions][about collecting functions], and `data` documentation.
