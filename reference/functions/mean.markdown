---
layout: default
title: mean
published: true
tags: [reference, data functions, functions, mean]
---

[%CFEngine_function_prototype(list)%]

**Description:** Return the mean of the numbers in `list`.

`list` can be a data container or a regular list.

[%CFEngine_function_attributes(list)%]

**Example:**

[%CFEngine_include_snippet(max-min-mean-variance.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(max-min-mean-variance.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**

**History:** Was introduced in version 3.6.0 (2014)

**See also:** `sort()`, `variance()`, `sum()`, `max()`, `min()`
