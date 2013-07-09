---
layout: default
title: getuid
categories: [Reference, Functions, getuid]
published: true
alias: reference-functions-getuid.html
tags: [reference, system functions, functions, getuid]
---

[%CFEngine_function_prototype(username)%]

**Description:** Return the integer user id of the named user on this host

If the named user is not registered the variable will not be defined.

[%CFEngine_function_attributes(username)%]

**Example:**

```cf3
    bundle agent example
    {
    vars:

      "uid" int => getuid("mark");

    reports:
      "Users uid is $(uid)";
    }
```
**Notes:**
On Windows, which does not support user ids, the variable will not 
be defined.
