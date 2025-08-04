---
layout: default
title: groupexists
---

{{< CFEngine_function_prototype(group) >}}

**Description:** Returns whether a group `group` exists on this host.

The group may be specified by name or identifier.

{{< CFEngine_function_attributes(group) >}}

**Example:**

{{< CFEngine_include_snippet(groupexists.cf, #\+begin_src cfengine3, .*end_src) >}}

Output:

{{< CFEngine_include_snippet(groupexists.cf, #\+begin_src\s+example_output\s*, .*end_src) >}}
