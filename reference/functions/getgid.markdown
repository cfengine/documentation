---
layout: default
title: getgid
categories: [Reference, Functions, getgid]
published: true
alias: reference-functions-getgid.html
tags: [reference, functions, getgid]
---

**Prototype**: `getgid(groupname)`

**Return type**: `int`

**Description**: Return the integer group id of the group `groupname` on this 
host.

If the named group does not exist, the function will fail and the variable 
will not be defined. 

**Arguments**:

* `groupname` : Group name as text, *in the range* .\*

**Example**:

```cf3
bundle agent example
{     
vars:

  "gid" int => getgid("users");

reports:

  Yr2008::

    "Users gid is $(gid)";
}
```

**Notes**:
On Windows, which does not support group ids, the variable will not be
defined.
