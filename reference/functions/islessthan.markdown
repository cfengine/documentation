---
layout: default
title: islessthan
categories: [Reference, Functions, islessthan]
published: true
alias: reference-functions-islessthan.html
tags: [reference, functions, islessthan]
---

**Prototype**: `islessthan(value1, value2)`

**Return type**: `class`

**Description**: Returns whether `value1` is less than `value2`.

The comparison is made numerically if possible. If the values are
strings, the result is the inverse to that of comparing with strcmp().

**Arguments**:

* `value1` : Smaller string or value, *in the range* .\*
* `value2` : Larger string or value, *in the range* .\*

**Example**:

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

**Notes**:

See also `isgreaterthan`.
