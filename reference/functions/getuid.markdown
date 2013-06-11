---
layout: default
title: getuid
categories: [Reference, Functions, getuid]
published: true
alias: reference-functions-getuid.html
tags: [reference, functions, getuid]
---

**Prototype**: `getuid(username)`

**Return type**: `int`

**Description:** Return the integer user id of the named user on this host

If the named user is not registered the variable will not be defined.

**Arguments**:

* `username` : User name in text, in the range `.*`

**Example:**

```cf3
bundle agent example
{
vars:

  "uid" int => getuid("mark");

reports:

  Yr2008::

    "Users uid is $(uid)";
}
```
**Notes:**
On Windows, which does not support user ids, the variable will not 
be defined.
