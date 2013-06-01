---
layout: default
title: iprange
categories: [Reference, Functions, iprange]
published: true
alias: reference-functions-iprange.html
tags: [reference, functions, iprange]
---

**Prototype**: iprange(arg1) 

**Return type**: `class`

 *arg1* : IP address range syntax, *in the range* .\*   

True if the current host lies in the range of IP addresses specified

**Example**:

```cf3
body common control

{
bundlesequence  => { "example" };
}

###########################################################

bundle agent example

{     
classes:

  "adhoc_group_1" expression => iprange("128.39.89.10-15");
  "adhoc_group_2" expression => iprange("128.39.74.1/23");

reports:

  adhoc_group_1::

    "Some numerology";

  adhoc_group_2::

    "The masked warriors";
}
```

**Notes**:
Pattern matching based on IP addresses.
