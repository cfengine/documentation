---
layout: default
title: intersection
categories: [Reference, Functions, intersection]
published: true
alias: reference-functions-intersection.html
tags: [reference, functions, intersection]
---

**Prototype**: `intersection(list1, list2)`

**Return type**: `slist`

**Description**: Returns the unique elements in list1 that are also in list2.

**Arguments**:

* `list1` : The name of the base list variable, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+

* `list2` : The name of the intersected list variable, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+

**Example**:

```cf3
    bundle agent test
    {
      vars:
          "a" slist => { 1,2,3,"x" };
          "b" slist => { "x" };

          "listname1" slist => { "a", "b" };
          "listname2" slist => { "a", "b" };
          "$(listname1)_str" string => join(",", $(listname1));

          "int_$(listname1)_$(listname2)" slist => intersection($(listname1), $(listname2));
          "int_$(listname1)_$(listname2)_str" string => join(",", "int_$(listname1)_$(listname2)");

      reports:
          "The intersection of list '$($(listname1)_str)' with '$($(listname2)_str)' is '$(int_$(listname1)_$(listname2)_str)'";
    }
```

**Notes**:  

See also `difference`.
