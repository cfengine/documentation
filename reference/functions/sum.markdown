---
layout: default
title: sum
categories: [Reference, Functions, sum]
published: true
alias: reference-functions-sum.html
tags: [reference, functions, sum]
---

**Prototype**: `sum(list)`

**Return type**: `real`

**Description**: Return the sum of the reals in `list`.

This function might be used for simple ring computation. Of course, you could 
easily combine `sum` with `readstringarray` or `readreallist` etc., to collect 
summary information from a source external to CFEngine.

**Arguments**:

* `list` : A list of arbitrary real values, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+

**Example**:

```cf3
bundle agent test
{
  vars:
      "adds_to_six" ilist => { "1", "2", "3" };
      "six" real => sum("adds_to_six");
      "adds_to_zero" rlist => { "1.0", "2", "-3e0" };
      "zero" real => sum("adds_to_zero");

  reports:
    cfengine_3::
      "six is $(six), zero is $(zero)";
}
```

Because `$(six)` and `$(zero)` are both real numbers, the report that is
generated will be:

```
six is 6.000000, zero is 0.000000
```

**Notes**:  
   
**History**: Was introduced in version 3.1.0b1,Nova 2.0.0b1 (2010)
