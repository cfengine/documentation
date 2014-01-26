---
layout: default
title: max
categories: [Reference, Functions, max]
published: true
alias: reference-functions-max.html
tags: [reference, data functions, functions, max]
---

[%CFEngine_function_prototype(list, sortmode)%]

**Description:** Return the maximum of the items in `list` according to `sortmode` (same sort modes as in `sort()`, which see).

[%CFEngine_function_attributes(list, sortmode)%]

**Example:**

[%CFEngine_include_snippet(max-min-mean-variance.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(max-min-mean-variance.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**  
   
**History:** Was introduced in version 3.6.0 (2014)

**See also:** `sort()`, `variance()`, `sum()`, `mean()`, `min()`
