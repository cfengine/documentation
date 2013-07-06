---
layout: default
title: accumulated
categories: [Reference, Functions, accumulated]
published: true
alias: reference-functions-accumulated.html
tags: [reference, data functions, functions, accumulated]
---

[%CFEngine_function_prototype(years, months, days, hours, minutes, seconds)%]

**Description:** Convert an accumulated amount of time into a system representation.

The `accumulated` function measures total accumulated runtime. Arguments
are applied additively, so that accumulated(0,0,2,27,90,0) means "2
days, 27 hours and 90 minutes of runtime" ". However, you are strongly
encouraged to keep your usage of `accumulated` sensible and readable;
for example, accumulated(0,0,0,48,0,0) or accumulated(0,0,0,0,90,0).


**Arguments:**

* `years`, in the range `0,1000`

Years of run time. For convenience in conversion, a year of runtime is
always 365 days (one year equals 31,536,000 seconds).

* `month`, in the range `0,1000`

Months of run time. For convenience in conversion, a month of runtime is
always equal to 30 days of runtime (one month equals 2,592,000 seconds).

* `days`, in the range `0,1000`

Days of runtime (one day equals 86,400 seconds)   

* `hours`, in the range `0,1000`

Hours of runtime   

* `minutes`, in the range `0,1000`

Minutes of runtime 0-59   

* `seconds`, in the range `0,40000`

Seconds of runtime

**Example:**

```cf3
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

    body process_select proc_finder
    {
      ttime_range => irange(accumulated(0,0,0,0,2,0),accumulated(0,0,0,0,20,0));
      process_result => "ttime";
    }

    body process_count anyprocs
    {
      match_range => "0,0";
      out_of_range_define => { "any_procs" };
    }
```

In the example we look for processes that have accumulated between 2 and
20 minutes of total run time.
