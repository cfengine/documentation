---
layout: default
title: Function-classify
categories: [Special-functions,Function-classify]
published: true
alias: Special-functions-Function-classify.html
tags: [Special-functions,Function-classify]
---

### Function classify

**Synopsis**: classify(arg1) returns type **class**

\
 *arg1* : Input string, *in the range* .\* \

True if the canonicalization of the argument is a currently defined
class

**Example**:\
 \

~~~~ {.verbatim}
classes:

 "i_am_the_policy_host" expression => classify("master.example.org");
~~~~

**Notes**:\
 \

This function returns true if the canonical form of the argument is
already a defined class. This is useful for transforming variables into
classes.

See: [Function canonify](#Function-canonify).
