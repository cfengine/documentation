---
layout: default
title: laterthan
categories: [Reference, Functions, laterthan]
published: true
alias: reference-functions-laterthan.html
tags: [reference, functions, laterthan]
---

**Prototype**: `laterthan(arg1,arg2,arg3,arg4,arg5,arg6)`

**Return type**:

`class`

* `arg1` : Years, *in the range* 0,1000   
* `arg2` : Months, *in the range* 0,1000   
* `arg3` : Days, *in the range* 0,1000   
* `arg4` : Hours, *in the range* 0,1000   
* `arg5` : Minutes, *in the range* 0,1000   
* `arg6` : Seconds, *in the range* 0,40000   

True if the current time is later than the given date

**Example**:

```cf3
classes:

  "after_deadline" expression => laterthan(2000,1,1,0,0,0);
```

**Notes**:
The arguments are standard time (See [Function on](#Function-on)).
