---
layout: default
title: iprange
categories: [Reference, Functions, iprange]
published: true
alias: reference-functions-iprange.html
tags: [reference, communication functions, functions, iprange]
---

[%CFEngine_function_prototype(range)%]

**Description:** Returns whether the current host lies in the range of IP 
addresses specified.

Pattern matching based on IP addresses.

[%CFEngine_function_attributes(range)%]

**Example:**

```cf3
bundle agent example
{
classes:

  "dmz_1" expression => iprange("128.39.89.10-15");
  "lab_1" expression => iprange("128.39.74.1/23");

reports:

  dmz_1::

    "DMZ 1 subnet";

  lab_1::

    "Lab 1 subnet";
}
```
