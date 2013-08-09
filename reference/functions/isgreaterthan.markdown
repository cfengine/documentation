---
layout: default
title: isgreaterthan
categories: [Reference, Functions, isgreaterthan]
published: true
alias: reference-functions-isgreaterthan.html
tags: [reference, data functions, functions, isgreaterthan]
---

[%CFEngine_function_prototype(value1, value2)%]

**Description:** Returns whether `value1` is greater than `value2`.

The comparison is made numerically if possible. If the values are
strings, the result is identical to that of comparing with strcmp().

[%CFEngine_function_attributes(value1, value2)%]

**Example:**

```cf3
bundle agent example
{
classes:

  "ok" expression => isgreaterthan("1","0");

reports:

  ok::

    "Assertion is true";

 !ok::

  "Assertion is false";

}
```
