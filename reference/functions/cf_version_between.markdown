---
layout: default
title: cf_version_between
published: true
tags: [reference, utility functions, functions]
---

[%CFEngine_function_prototype(string, string)%]

**Description:** Returns `true` if local CFEngine version is between the first `string` and the second `string`. This function is inclusive.

[%CFEngine_function_attributes(string, string)%]

**Example:**

[%CFEngine_include_snippet(cf_version_between.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(cf_version_between.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** `cf_version_maximum()`, `cf_version_minimum()`, `cf_version_after()`, `cf_version_before()`, `cf_version_at()`.

**History:**
* Introduced in 3.16.0
