---
layout: default
title: isgreaterthan
categories: [Reference, Functions, isgreaterthan]
published: true
alias: reference-functions-isgreaterthan.html
tags: [reference, functions, isgreaterthan]
---

**Prototype**: `isgreaterthan(value1, value2)`

**Return type**: `class`

**Description**: Returns whether `value1` is greater than `value2`.

The comparison is made numerically if possible. If the values are
strings, the result is identical to that of comparing with strcmp().

**Arguments**:

* `value1` : Larger string or value, *in the range* .\*
* `value2` : Smaller string or value, *in the range* .\*

**Example**:

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
