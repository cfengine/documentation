---
layout: default
title: CFEngine Administration Examples
published: true
sorting: 2
tags: [Examples][CFEngine Administration]
---

* [Ordering promises][Basic Examples#Ordering promises]
* [Aborting execution][Software Administration and Execution#Aborting execution]
* Aborting execution
* Updating from a central policy server

## Ordering promises ##
## Aborting execution ##

```cf3
body common control

{
bundlesequence  => { "testbundle"  };

version => "1.2.3";
}

###########################################


body agent control

{
abortbundleclasses => { "invalid.Hr16" };
}

###########################################


bundle agent testbundle
{
vars:

 "userlist" slist => { "xyz", "mark", "jeang", "jonhenrik", "thomas", "eben" };

methods:

 "any" usebundle => subtest("$(userlist)");

}

###########################################


bundle agent subtest(user)

{
classes:

  "invalid" not => regcmp("[a-z][a-z][a-z][a-z]","$(user)");

reports:

 !invalid::

  "User name $(user) is valid at 4 letters";

 invalid::

  "User name $(user) is invalid";
}
```