---
layout: default
title: Function-randomint
categories: [Special-functions,Function-randomint]
published: true
alias: Special-functions-Function-randomint.html
tags: [Special-functions,Function-randomint]
---

### Function randomint

**Synopsis**: randomint(arg1,arg2) returns type **int**

\
 *arg1* : Lower inclusive bound, *in the range* -99999999999,9999999999
\
 *arg2* : Upper inclusive bound, *in the range* -99999999999,9999999999
\

Generate a random integer between the given limits

**Example**:\
 \

~~~~ {.verbatim}
vars:

 "ran"    int => randomint(4,88);
~~~~

**Notes**:\
 \

The limits must be integer values and the resulting numbers are based on
the entropy of the md5 algorithm.
