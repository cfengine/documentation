---
layout: default
title: "on"
categories: [Reference, Functions, "on"]
published: true
alias: reference-functions-on.html
tags: [reference, data functions, functions, "on"]
---

**Prototype:** `on(years, months, days, hours, minutes, seconds)`

**Return type:** `int`

**Description:** Returns the specified date/time in integer system representation.

The specified date/time is an absolute date in the local timezone.

**Arguments**:

* `years` : year in the range `1970,3000`
* `month` : month, in the range `1,12`
* `day` : day of month, in the range `1,31`
* `hour` : hour of day, in the range `0,23`
* `minute` : minute, in the range `0,59`
* `second` : second, in the range `0,59`

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
