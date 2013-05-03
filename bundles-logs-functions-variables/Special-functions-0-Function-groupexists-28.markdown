---
layout: default
title: Function-groupexists-28
categories: [Special-functions,Function-groupexists-28]
published: true
alias: Special-functions-Function-groupexists-28.html
tags: [Special-functions,Function-groupexists-28]
---

### Function groupexists

**Synopsis**: groupexists(arg1) returns type **class**

\
 *arg1* : Group name or identifier, *in the range* .\* \

True if group or numerical id exists on this host

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
classes:

  "gname" expression => groupexists("users");
  "gid"   expression => groupexists("100");

reports:

  gname::

    "Group exists by name";

  gid::

    "Group exists by id";

}
~~~~

**Notes**:\
 \

The group may be specified by name or number.
