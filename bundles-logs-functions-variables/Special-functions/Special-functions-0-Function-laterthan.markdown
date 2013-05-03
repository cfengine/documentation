---
layout: default
title: Function-laterthan
categories: [Special-functions,Function-laterthan]
published: true
alias: Special-functions-Function-laterthan.html
tags: [Special-functions,Function-laterthan]
---

### Function laterthan

**Synopsis**: laterthan(arg1,arg2,arg3,arg4,arg5,arg6) returns type
**class**

\
 *arg1* : Years, *in the range* 0,1000 \
 *arg2* : Months, *in the range* 0,1000 \
 *arg3* : Days, *in the range* 0,1000 \
 *arg4* : Hours, *in the range* 0,1000 \
 *arg5* : Minutes, *in the range* 0,1000 \
 *arg6* : Seconds, *in the range* 0,40000 \

True if the current time is later than the given date

**Example**:\
 \

~~~~ {.verbatim}
classes:

  "after_deadline" expression => laterthan(2000,1,1,0,0,0);
~~~~

**Notes**:\
 \

The arguments are standard time (See [Function on](#Function-on)).
