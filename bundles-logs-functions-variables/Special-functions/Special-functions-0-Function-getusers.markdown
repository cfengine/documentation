---
layout: default
title: Function-getusers
categories: [Special-functions,Function-getusers]
published: true
alias: Special-functions-Function-getusers.html
tags: [Special-functions,Function-getusers]
---

### Function getusers

**Synopsis**: getusers(arg1,arg2) returns type **slist**

\
 *arg1* : Comma separated list of User names, *in the range* .\* \
 *arg2* : Comma separated list of UserID numbers, *in the range* .\* \

Get a list of all system users defined, minus those names defined in
arg1 and uids in arg2

**Example**:\
 \

~~~~ {.verbatim}
vars:
  "allusers" slist => getusers("zenoss,mysql,at","12,0");

reports:

 linux::

  "Found user $(allusers)";
~~~~

**Notes**:\
 \

**History**: Was introduced in version 3.1.0b1,Nova 2.0.0b1 (2010). This
function is only available on Unix-like systems in the present version.

The function has two arguments, both are comma separated lists. The
first argument is a list of user names that should be excluded from the
output. The second is a list of integer UIDs that should be excluded.
