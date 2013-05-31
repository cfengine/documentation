---
layout: default
title: getuid
categories: [Reference, Functions, getuid]
published: true
alias: reference-functions-getuid.html
tags: [reference, functions, getuid]
---



**Synopsis**: getuid(arg1) returns type **int**

  
 *arg1* : User name in text, *in the range* .\*   

Return the integer user id of the named user on this host

**Example**:  
   

```cf3
body common control

{
bundlesequence  => { "example" };
}

###########################################################

bundle agent example

{
vars:

  "uid" int => getuid("mark");

reports:

  Yr2008::

    "Users uid is $(uid)";

}
```

**Notes**:  
   

If the named user is not registered the variable will not be defined. On
Windows, which does not support user ids, the variable will not be
defined.
