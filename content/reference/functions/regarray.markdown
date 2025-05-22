---
layout: default
title: regarray
---

[%CFEngine_function_prototype(array, regex)%]

**Description:** Returns whether `array` contains elements matching the
[anchored][anchored]regular expression `regex`.

[%CFEngine_function_attributes(array, regex)%]

**Example:**

[%CFEngine_include_snippet(regarray.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(regarray.cf, #\+begin_src\s+example_output\s*, .*end_src)%]
