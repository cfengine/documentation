---
layout: default
title: variance
published: true
tags: [reference, data functions, functions, variance, inline_json]
---

[%CFEngine_function_prototype(list)%]

**Description:** Return the variance of the numbers in `list`.

[This function can accept many types of data parameters.][Functions#collecting functions]

[%CFEngine_function_attributes(list)%]

Use the `eval()` function to easily get the standard deviation (square root of the variance).

This is not part of a full statistical package but a convenience function.

**Example:**

[%CFEngine_include_snippet(max-min-mean-variance.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(max-min-mean-variance.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Was introduced in version 3.6.0 (2014). The [collecting function][Functions#collecting functions] behavior was added in 3.9.

**See also:** `sort()`, `mean()`, `sum()`, `max()`, `min()`, [about collecting functions][Functions#collecting functions], and `data` documentation.
