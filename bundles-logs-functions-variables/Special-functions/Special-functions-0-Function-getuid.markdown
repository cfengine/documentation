---
layout: default
title: Function-getuid
categories: [Special-functions,Function-getuid]
published: true
alias: Special-functions-Function-getuid.html
tags: [Special-functions,Function-getuid]
---

### Function getuid

**Synopsis**: getuid(arg1) returns type **int**

\
 *arg1* : User name in text, *in the range* .\* \

Return the integer user id of the named user on this host

**Example**:\
 \

~~~~ {.verbatim}
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
~~~~

**Notes**:\
 \

If the named user is not registered the variable will not be defined. On
Windows, which does not support user ids, the variable will not be
defined.
