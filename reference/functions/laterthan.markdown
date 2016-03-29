---
layout: default
title: laterthan
published: true
tags: [reference, files functions, functions, laterthan]
---

[%CFEngine_function_prototype(year, month, day, hour, minute, second)%]

**Description:** Returns whether the current time is later than the given
date and time.

The specified date/time is an absolute date in the local timezone.
Note that, unlike some other functions, the month argument is 1-based (i.e. 1 corresponds to January).

[%CFEngine_function_attributes(year, month, day, hour, minute, second)%]

**Example:**

```cf3
bundle agent example
{
    classes:

      "after_deadline" expression => laterthan(2000,1,1,0,0,0);
    reports:
      after_deadline::
        "deadline has passed";
}
```

**See also:** `on()`
