---
layout: default
title: Function-hostinnetgroup-33
categories: [Special-functions,Function-hostinnetgroup-33]
published: true
alias: Special-functions-Function-hostinnetgroup-33.html
tags: [Special-functions,Function-hostinnetgroup-33]
---

### Function hostinnetgroup

**Synopsis**: hostinnetgroup(arg1) returns type **class**

\
 *arg1* : Netgroup name, *in the range* .\* \

True if the current host is in the named netgroup

**Example**:\
 \

~~~~ {.verbatim}
classes:

  "ingroup" expression => hostinnetgroup("my_net_group");
~~~~

**Notes**:\
 \
