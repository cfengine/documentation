---
layout: default
title: ago
published: true
tags: [reference, data functions, functions, ago]
---

[%CFEngine_function_prototype(years, months, days, hours, minutes, seconds)%]

**Description:** Convert a time relative to now to an integer system representation.

The `ago` function measures time relative to now. Arguments are applied
in order, so that ago(0,18,55,27,0,0) means "18 months, 55 days, and 27
hours ago". However, you are strongly encouraged to keep your usage of
`ago` sensible and readable, e.g., ago(0,0,120,0,0,0) or
ago(0,0,0,72,0,0).

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

[%CFEngine_include_snippet(ago.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(ago.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

