---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Special-functions-0-Function-hostinnetgroup-33.markdown.html
tags: [xx]
---

### Function hostinnetgroup

**Synopsis**: hostinnetgroup(arg1) returns type **class**

\
 *arg1* : Netgroup name, *in the range* .\* \

True if the current host is in the named netgroup

**Example**:\
 \

    classes:

      "ingroup" expression => hostinnetgroup("my_net_group");

**Notes**:\
 \
