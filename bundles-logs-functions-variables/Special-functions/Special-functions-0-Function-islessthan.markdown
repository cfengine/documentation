---
layout: default
title: Function-islessthan
categories: [Special-functions,Function-islessthan]
published: true
alias: Special-functions-Function-islessthan.html
tags: [Special-functions,Function-islessthan]
---

### Function islessthan

**Synopsis**: islessthan(arg1,arg2) returns type **class**

\
 *arg1* : Smaller string or value, *in the range* .\* \
 *arg2* : Larger string or value, *in the range* .\* \

True if arg1 is numerically less than arg2, else compare strings like
NOT strcmp

**Example**:\
 \

~~~~ {.verbatim}
body common control

{
bundlesequence  => { "test"  };
}

###########################################################

bundle agent test

{
classes:

  "ok" expression => islessthan("0","1");

reports:

  ok::

    "Assertion is true";

 !ok::

  "Assertion is false";

}
~~~~

**Notes**:\
 \

The complement of `isgreaterthan`. The comparison is made numerically if
possible. If the values are strings, the result is identical to that of
comparing with strcmp().
