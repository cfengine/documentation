---
layout: default
title: Function-hostinnetgroup
categories: [Special-functions,Function-hostinnetgroup]
published: true
alias: Special-functions-Function-hostinnetgroup.html
tags: [Special-functions,Function-hostinnetgroup]
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
