---
layout: default
title: Function-countclassesmatching
categories: [Special-functions,Function-countclassesmatching]
published: true
alias: Special-functions-Function-countclassesmatching.html
tags: [Special-functions,Function-countclassesmatching]
---

### Function countclassesmatching

**Synopsis**: countclassesmatching(arg1) returns type **int**

\
 *arg1* : Regular expression, *in the range* .\* \

Count the number of defined classes matching regex arg1

**Example**:\
 \

~~~~ {.verbatim}
bundle agent example
{
vars:

  "num" int => countclassesmatching("entropy.*low");

reports:

  cfengine_3::

    "Found $(num) classes matching";

}
~~~~

**Notes**:\
 \

This function matches classes, using a regular expression that should
match the whole line.

regex

A regular expression matching zero or more classes in the current list
of defined classes. The regular expression is anchored, meaning it must
match a complete class (See [Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)).

The function returns the number of classes matched.
