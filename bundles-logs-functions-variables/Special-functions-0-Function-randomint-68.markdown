---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Special-functions-0-Function-randomint-68.markdown.html
tags: [xx]
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

    vars:

     "ran"    int => randomint(4,88);

**Notes**:\
 \

The limits must be integer values and the resulting numbers are based on
the entropy of the md5 algorithm.
