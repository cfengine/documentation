---
layout: default
title: irange
categories: [Reference, Functions, irange]
published: true
alias: reference-functions-irange.html
tags: [reference, data functions, functions, irange]
---

[%CFEngine_function_prototype(arg1, arg2)%]

**Description:** Define a range of integer values for CFEngine internal use.

Used for any scalar attribute which requires an integer range. You can
generally interchangeably say "1,10" or irange("1","10"). However, if
you want to create a range of dates or times, you must use irange if you
also use the functions `ago`, `now`, `accumulated`, etc.

[%CFEngine_function_attributes(arg1, arg2)%]

**Example:**

```cf3
    irange("1","100");

    irange(ago(0,0,0,1,30,0), "0");
```
