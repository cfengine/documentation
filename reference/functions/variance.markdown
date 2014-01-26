---
layout: default
title: variance
categories: [Reference, Functions, variance]
published: true
alias: reference-functions-variance.html
tags: [reference, data functions, functions, variance]
---

[%CFEngine_function_prototype(list)%]

**Description:** Return the variance of the numbers in `list`.

[%CFEngine_function_attributes(list)%]

Use the `eval()` function to easily get the standard deviation (square root of the variance).

This is not part of a full statistical package but a convenience function.

**Example:**

[%CFEngine_include_snippet(max-min-mean-variance.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(max-min-mean-variance.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**  
   
**History:** Was introduced in version 3.6.0 (2014)

**See also:** `sort()`, `mean()`, `sum()`, `max()`, `min()`
