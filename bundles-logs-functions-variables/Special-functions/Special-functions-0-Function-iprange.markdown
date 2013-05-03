---
layout: default
title: Function-iprange
categories: [Special-functions,Function-iprange]
published: true
alias: Special-functions-Function-iprange.html
tags: [Special-functions,Function-iprange]
---

### Function iprange

**Synopsis**: iprange(arg1) returns type **class**

\
 *arg1* : IP address range syntax, *in the range* .\* \

True if the current host lies in the range of IP addresses specified

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

  "adhoc_group_1" expression => iprange("128.39.89.10-15");
  "adhoc_group_2" expression => iprange("128.39.74.1/23");

reports:

  adhoc_group_1::

    "Some numerology";

  adhoc_group_2::

    "The masked warriors";
}
~~~~

**Notes**:\
 \

Pattern matching based on IP addresses.
