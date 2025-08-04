---
layout: default
title: useringroup
---

{{< CFEngine_function_prototype(user) >}}

**Description:** Return whether a `user` is a member of a given `group`

Looks up the group `"group_name"` in the group database located in /etc/group and checks whether `"user_name"` is one of its members. This function is not available on Windows.

{{< CFEngine_function_attributes(user_name, group_name) >}}

**Example:**

{{< CFEngine_include_snippet(useringroup.cf, #\+begin_src cfengine3, .*end_src) >}}

Output:

{{< CFEngine_include_snippet(useringroup.cf, #\+begin_src\s+example_output\s*, .*end_src) >}}

**History:**

- Added in CFEngine 3.26.0
