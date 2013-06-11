---
layout: default
title: laterthan
categories: [Reference, Functions, laterthan]
published: true
alias: reference-functions-laterthan.html
tags: [reference, files functions, functions, laterthan]
---

**Prototype:** `laterthan(years, months, days, hours, minutes, seconds)`

**Return type:** `class`

**Description:** Returns whether the current time is later than the given 
date and time.

The arguments are standard time (See [Function on](#Function-on)).

**Arguments**:

* `years` : year in the range `1970,3000`
* `month` : month, in the range `1,12`
* `day` : day of month, in the range `1,31`
* `hour` : hour of day, in the range `0,23`
* `minute` : minute, in the range `0,59`
* `second` : second, in the range `0,59`

**Example:**

```cf3
    classes:

      "after_deadline" expression => laterthan(2000,1,1,0,0,0);
```
