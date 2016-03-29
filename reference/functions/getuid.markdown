---
layout: default
title: getuid
published: true
tags: [reference, system functions, functions, getuid]
---

[%CFEngine_function_prototype(username)%]

**Description:** Return the integer user id of the named user on this host

If the named user is not registered the variable will not be defined.

[%CFEngine_function_attributes(username)%]

**Example:**

[%CFEngine_include_snippet(getuid.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(getuid.cf, #\+begin_src\s+example_output\s*, .*end_src)%]
**Notes:**
On Windows, which does not support user ids, the variable will not
be defined.
