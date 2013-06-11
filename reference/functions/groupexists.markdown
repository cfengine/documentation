---
layout: default
title: groupexists
categories: [Reference, Functions, groupexists]
published: true
alias: reference-functions-groupexists.html
tags: [reference, functions, groupexists]
---

**Prototype**: `groupexists(group)`

**Return type**: `class`

**Description:** Returns whether a group `group` exists on this host.

The group may be specified by name or identifier.

**Arguments**:

* `group` : Group name or identifier, in the range `.*`

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
