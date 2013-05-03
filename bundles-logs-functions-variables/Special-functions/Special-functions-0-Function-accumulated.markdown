---
layout: default
title: Function-accumulated
categories: [Special-functions,Function-accumulated]
published: true
alias: Special-functions-Function-accumulated.html
tags: [Special-functions,Function-accumulated]
---

### Function accumulated

**Synopsis**: accumulated(arg1,arg2,arg3,arg4,arg5,arg6) returns type
**int**

\
 *arg1* : Years, *in the range* 0,1000 \
 *arg2* : Months, *in the range* 0,1000 \
 *arg3* : Days, *in the range* 0,1000 \
 *arg4* : Hours, *in the range* 0,1000 \
 *arg5* : Minutes, *in the range* 0,1000 \
 *arg6* : Seconds, *in the range* 0,40000 \

Convert an accumulated amount of time into a system representation

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

   "Found processes in range";
}

########################################################

body process_select proc_finder

{
ttime_range => irange(accumulated(0,0,0,0,2,0),accumulated(0,0,0,0,20,0));
process_result => "ttime";
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

In the example we look for processes that have accumulated between 2 and
20 minutes of total run time.

**ARGUMENTS**:

The `accumulated` function measures total accumulated runtime. Arguments
are applied additively, so that accumulated(0,0,2,27,90,0) means "2
days, 27 hours and 90 minutes of runtime" ". However, you are strongly
encouraged to keep your usage of `accumulated` sensible and readable;
for example, accumulated(0,0,0,48,0,0) or accumulated(0,0,0,0,90,0).

Years

Years of run time. For convenience in conversion, a year of runtime is
always 365 days (one year equals 31,536,000 seconds). \

Month

Months of run time. For convenience in conversion, a month of runtime is
always equal to 30 days of runtime (one month equals 2,592,000 seconds).
\

Day

Days of runtime (one day equals 86,400 seconds) \

Hours

Hours of runtime \

Minutes

Minutes of runtime 0-59 \

Seconds

Seconds of runtime
