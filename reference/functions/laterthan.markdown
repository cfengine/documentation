---
layout: default
title: laterthan
categories: [Reference, Functions, laterthan]
published: true
alias: reference-functions-laterthan.html
tags: [reference, functions, laterthan]
---

**Prototype**: `laterthan(years, months, days, hours, minutes, seconds)`

**Return type**: `class`

**Description**: Returns whether the current time is later than the given 
date and time.

The arguments are standard time (See [Function on](#Function-on)).

**Arguments**:

* `years`, *in the range* 0,1000   

Years of run time. For convenience in conversion, a year of runtime is
always 365 days (one year equals 31,536,000 seconds).   

* `month`, *in the range* 0,1000   

Months of run time. For convenience in conversion, a month of runtime is
always equal to 30 days of runtime (one month equals 2,592,000 seconds).

* `days`, *in the range* 0,1000   

Days of runtime (one day equals 86,400 seconds)   

* `hours`, *in the range* 0,1000

Hours of runtime   

* `minutes`, *in the range* 0,1000

Minutes of runtime 0-59   

* `seconds`, *in the range* 0,40000

Seconds of runtime

**Example**:

```cf3
    classes:

      "after_deadline" expression => laterthan(2000,1,1,0,0,0);
```
