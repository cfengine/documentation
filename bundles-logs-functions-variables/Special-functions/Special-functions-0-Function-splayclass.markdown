---
layout: default
title: Function-splayclass
categories: [Special-functions,Function-splayclass]
published: true
alias: Special-functions-Function-splayclass.html
tags: [Special-functions,Function-splayclass]
---

### Function splayclass

**Synopsis**: splayclass(arg1,arg2) returns type **class**

\
 *arg1* : Input string for classification, *in the range* .\* \
 *arg2* : Splay time policy, *in the range* daily,hourly \

True if the first argument's time-slot has arrived, according to a
policy in arg2

**Example**:\
 \

~~~~ {.verbatim}
body common control

{
bundlesequence  => { "example" };
}

###########################################################

bundle agent example

{     
classes:

  "my_result" expression => splayclass("$(sys.host)$(sys.ipv4)","daily");

reports:

  my_result::

    "Load balanced class activated";

}
~~~~

**Notes**:\
 \

The lvalue class evaluates to true if the system clock lies within a
scheduled time-interval that maps to a hash of the first argument (which
may be any arbitrary string). Different strings will hash to different
time intervals, and thus one can map different tasks to time-intervals.

This function may be used to distribute a task, typically on multiple
hosts, in time over a day or an hourly period, depending on the policy
in the second argument (that must be one of `"daily"` or `"hourly"`).
This is useful for copying resources to multiple hosts from a single
server, (e.g. large software updates), when simultaneous scheduling
would lead to a bottleneck and/or server overload.

The function is similar to the `splaytime` feature in `cf-execd`, except
that it allows you to base the decision on any string-criterion on a
given host. The entropy (or string-variation) in the first argument
determines how effectively CFEngine will be able to distribute tasks.
CFEngine instances with the same first argument will yield a true result
at the same time (and different first argument will yield a true result
at a different time). Thus tasks could be scheduled according to group
names for predictability, or according to IP addresses for distribution
across the policy interval.

The times at which the splayclass will be defined depends on the second
argument. If the first argument is `"hourly"` then the class will be
defined for a 5-minute interval every hour (and if the first argument is
`"daily"`, then the class will be defined for one 5-minute interval
every day. This means that `splayclass` assumes that you are running
CFEngine with the default schedule of "every 5 minutes". If you change
the executor `schedule` control variable, you may prevent the splayclass
from ever being defined (that is, if the hashed 5-minute interval that
is selected by the splayclass is a time when you have told CFEngine
*not* to run).
