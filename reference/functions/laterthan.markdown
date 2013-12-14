---
layout: default
title: laterthan
categories: [Reference, Functions, laterthan]
published: true
alias: reference-functions-laterthan.html
tags: [reference, files functions, functions, laterthan]
---

[%CFEngine_function_prototype(year, month, day, hour, minute, second)%]

**Description:** Returns whether the current time is later than the given 
date and time.

The arguments are standard time.

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
