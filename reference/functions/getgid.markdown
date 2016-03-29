---
layout: default
title: getgid
published: true
tags: [reference, data functions, functions, getgid]
---

[%CFEngine_function_prototype(groupname)%]

**Description:** Return the integer group id of the group `groupname` on this
host.

If the named group does not exist, the function will fail and the variable
will not be defined.

[%CFEngine_function_attributes(groupname)%]

**Example:**

[%CFEngine_include_snippet(getgid.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(getgid.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**
On Windows, which does not support group ids, the variable will not be
defined.
