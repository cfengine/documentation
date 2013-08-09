---
layout: default
title: islessthan
categories: [Reference, Functions, islessthan]
published: true
alias: reference-functions-islessthan.html
tags: [reference, data functions, functions, islessthan]
---

[%CFEngine_function_prototype(value1, value2)%]

**Description:** Returns whether `value1` is less than `value2`.

The comparison is made numerically if possible. If the values are
strings, the result is the inverse to that of comparing with strcmp().

[%CFEngine_function_attributes(value1, value2)%]

**Example:**

```cf3
bundle agent test
{
classes:

  "ok" expression => islessthan("0","1");

reports:

  ok::

    "Assertion is true";

 !ok::

  "Assertion is false";

}
```

**See also:** [`isgreaterthan()`][isgreaterthan].
