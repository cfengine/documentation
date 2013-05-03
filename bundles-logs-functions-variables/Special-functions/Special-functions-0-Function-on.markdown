---
layout: default
title: Function-on
categories: [Special-functions,Function-on]
published: true
alias: Special-functions-Function-on.html
tags: [Special-functions,Function-on]
---

### Function on

**Synopsis**: on(arg1,arg2,arg3,arg4,arg5,arg6) returns type **int**

\
 *arg1* : Year, *in the range* 1970,3000 \
 *arg2* : Month, *in the range* 1,12 \
 *arg3* : Day, *in the range* 1,31 \
 *arg4* : Hour, *in the range* 0,23 \
 *arg5* : Minute, *in the range* 0,59 \
 *arg6* : Second, *in the range* 0,59 \

Convert an exact date/time to an integer system representation

**Example**:\
 \

~~~~ {.verbatim}
body file_select zero_age
{
mtime       => irange(on(2000,1,1,0,0,0),now);
file_result => "mtime";
}
~~~~

**Notes**:\
 \

An absolute date in the local timezone. Note that in process matching
dates could be wrong by an hour depending on Daylight Savings Time /
Summer Time. This is a known bug to be fixed.

**ARGUMENTS**:

Years

The year, e.g. 2009 \

Month

The Month, 1-12 \

Day

The day 1-31 \

Hours

The hour 0-23 \

Minutes

The minutes 0-59 \

Seconds

The number of seconds 0-59
