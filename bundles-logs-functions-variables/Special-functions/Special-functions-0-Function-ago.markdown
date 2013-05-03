---
layout: default
title: Function-ago
categories: [Special-functions,Function-ago]
published: true
alias: Special-functions-Function-ago.html
tags: [Special-functions,Function-ago]
---

### Function ago

**Synopsis**: ago(arg1,arg2,arg3,arg4,arg5,arg6) returns type **int**

\
 *arg1* : Years, *in the range* 0,1000 \
 *arg2* : Months, *in the range* 0,1000 \
 *arg3* : Days, *in the range* 0,1000 \
 *arg4* : Hours, *in the range* 0,1000 \
 *arg5* : Minutes, *in the range* 0,1000 \
 *arg6* : Seconds, *in the range* 0,40000 \

Convert a time relative to now to an integer system representation

**Example**:\
 \

~~~~ {.verbatim}
bundle agent testbundle

{
processes:

 ".*"

    process_count   => anyprocs,
    process_select  => proc_finder;

reports:

 any_procs::

   "Found processes out of range";
}

########################################################

body process_select proc_finder

{
# Processes started between 5.5 hours and 20 minutes ago
stime_range => irange(ago(0,0,0,5,30,0),ago(0,0,0,0,20,0));
process_result => "stime";
}

########################################################

body process_count anyprocs

{
match_range => "0,0";
out_of_range_define => { "any_procs" };
}
~~~~

**Notes**:\
 \

The `ago` function measures time relative to now. Arguments are applied
in order, so that ago(0,18,55,27,0,0) means "18 months, 55 days, and 27
hours ago". However, you are strongly encouraged to keep your usage of
`ago` sensible and readable, e.g., ago(0,0,120,0,0,0) or
ago(0,0,0,72,0,0).

**ARGUMENTS**:

Years

Years ago. If today is February 29, and "**n** years ago" is not within
a leap-year, February 28 will be used. \

Month

Months ago. If the current month has more days that "**n** months ago",
the last day of "**n** months ago" will be used (e.g., if today is April
31 and you compute a date 1 month ago, the resulting date will be March
30), equal to 30 days of runtime (one month equals 2,592,000 seconds). \

Day

Days ago (you may, for example, specify 120 days) \

Hours

Hours ago. Since all computation are done using "Epoch time", 1 hour ago
will alway result in a time 60 minutes in the past, even during the
transition from Daylight time to Standard time. \

Minutes

Minutes ago 0-59 \

Seconds

Seconds ago
