---
layout: default
title: data_sysctlvalues
published: true
tags: [reference, system functions, functions, sysctl, data_sysctlvalues]
---

[%CFEngine_function_prototype()%]

**Description:** Returns all sysctl values using `/proc/sys`.

[%CFEngine_function_attributes()%]

**Example:**

Policy:

[%CFEngine_include_example(data_sysctlvalues.cf, #\+begin_src\s+cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(data_sysctlvalues.cf, #\+begin_src\s+mock_example_output\s*, .*end_src)%]

**Notes:**

**History:** Was introduced in version 3.11.0 (2017)

**See also:** `sysctlvalue()`
