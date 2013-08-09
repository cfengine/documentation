---
layout: default
title: "on"
categories: [Reference, Functions, "on"]
published: true
alias: reference-functions-on.html
tags: [reference, data functions, functions, "on"]
---

[%CFEngine_function_prototype(year, month, day, hour, minute, second)%]

**Description:** Returns the specified date/time in integer system representation.

The specified date/time is an absolute date in the local timezone.

[%CFEngine_function_attributes(year, month, day, hour, minute, second)%]

**Example:**

```cf3
    body file_select zero_age
    {
      mtime       => irange(on(2000,1,1,0,0,0),now);
      file_result => "mtime";
    }
```

**Notes:**
In process matching, dates could be wrong by an hour depending on Daylight 
Savings Time / Summer Time. This is a known bug to be fixed.
