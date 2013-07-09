---
layout: default
title: groupexists
categories: [Reference, Functions, groupexists]
published: true
alias: reference-functions-groupexists.html
tags: [reference, system functions, functions, groupexists]
---

[%CFEngine_function_prototype(group)%]

**Description:** Returns whether a group `group` exists on this host.

The group may be specified by name or identifier.

[%CFEngine_function_attributes(group)%]

**Example:**

```cf3
body common control

{
bundlesequence  => { "example" };
}

###########################################################

bundle agent example

{     
classes:

  "gname" expression => groupexists("users");
  "gid"   expression => groupexists("100");

reports:

  gname::

    "Group exists by name";

  gid::

    "Group exists by id";

}
```
