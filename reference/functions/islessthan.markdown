---
layout: default
title: islessthan
published: true
tags: [reference, data functions, functions, islessthan]
---

[%CFEngine_function_prototype(value1, value2)%]

**Description:** Returns whether `value1` is less than `value2`.

The comparison is made numerically if possible. If the values are
strings, the result is the inverse to that of comparing with strcmp().

[%CFEngine_function_attributes(value1, value2)%]

**Example:**

[%CFEngine_include_snippet(islessthan.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(islessthan.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** [`isgreaterthan()`][isgreaterthan].
