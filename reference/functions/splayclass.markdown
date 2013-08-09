---
layout: default
title: splayclass
categories: [Reference, Functions, splayclass]
published: true
alias: reference-functions-splayclass.html
tags: [reference, utility functions, functions, splayclass]
---

[%CFEngine_function_prototype(input, policy)%]

**Description:** Returns whether `input`'s time-slot has arrived, 
according to a `policy`.

The function returns true if the system clock lies within a scheduled 
time-interval that maps to a hash of `input` (which may be any arbitrary 
string). Different strings will hash to different time intervals, and thus one 
can map different tasks to time-intervals.

This function may be used to distribute a task, typically on multiple hosts, in time over a day or an hourly period, depending on the `policy` (that must be either `daily` or `hourly`). This is useful for copying resources to multiple hosts from a single server, (e.g. large software updates), when simultaneous scheduling would lead to a bottleneck and/or server overload.

The function is similar to the `splaytime` feature in `cf-execd`, except that it allows you to base the decision on any string-criterion on a given host. 

[%CFEngine_function_attributes(input, policy)%]

The variation in `input` determines how effectively CFEngine will be able to 
distribute tasks. CFEngine instances with the same `input` will yield a true 
result at the same time, and different `input` will yield a true result at 
different times. Thus tasks could be scheduled according to group names for 
predictability, or according to IP addresses for distribution across the 
policy interval.

The times at which the `splayclass` will be defined depends on the `policy`. 
If it is `hourly` then the class will be defined for a 5-minute interval every 
hour. If the policy `daily`, then the class will be defined for one 5-minute 
interval every day. This means that `splayclass` assumes that you are running 
CFEngine with the default schedule of "every 5 minutes". If you change the 
executor `schedule` control variable, you may prevent the `splayclass` from 
ever being defined (that is, if the hashed 5-minute interval that is selected 
by the `splayclass` is a time when you have told CFEngine *not* to run).

**Example:**

```cf3
    bundle agent example
    {     
    classes:

      "my_turn" expression => splayclass("$(sys.host)$(sys.ipv4)","daily");

    reports:

      my_turn::

        "Load balanced class activated";
    }
```
