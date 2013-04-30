---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Special-functions-0-Function-isgreaterthan-42.markdown.html
tags: [xx]
---

### Function isgreaterthan

**Synopsis**: isgreaterthan(arg1,arg2) returns type **class**

\
 *arg1* : Larger string or value, *in the range* .\* \
 *arg2* : Smaller string or value, *in the range* .\* \

True if arg1 is numerically greater than arg2, else compare strings like
strcmp

**Example**:\
 \

    body common control

    {
    bundlesequence  => { "test"  };
    }

    ###########################################################

    bundle agent test

    {
    classes:

      "ok" expression => isgreaterthan("1","0");

    reports:

      ok::

        "Assertion is true";

     !ok::

      "Assertion is false";

    }

**Notes**:\
 \

The comparison is made numerically if possible. If the values are
strings, the result is identical to that of comparing with strcmp().
