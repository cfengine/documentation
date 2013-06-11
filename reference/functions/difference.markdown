---
layout: default
title: difference
categories: [Reference, Functions, difference]
published: true
alias: reference-functions-difference.html
tags: [reference, functions, difference]
---

**Prototype**: `difference(list1, list2)`

**Return type**: `slist`

**Description:** Returns the unique elements in `list1` that are not in 
`list2`.

**Arguments**:

* `list1` : The name of the base list variable, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`

* `list2` : The name of the subtracted list variable, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`

**Example:**

```cf3
    bundle agent test
    {
      vars:
          "a" slist => { 1,2,3,"x" };
          "b" slist => { "x" };

          "listname1" slist => { "a", "b" };
          "listname2" slist => { "a", "b" };
          "$(listname1)_str" string => join(",", $(listname1));

          "diff_$(listname1)_$(listname2)" slist => difference($(listname1), $(listname2));
          "diff_$(listname1)_$(listname2)_str" string => join(",", "diff_$(listname1)_$(listname2)");

      reports:
          "The difference of list '$($(listname1)_str)' with '$($(listname2)_str)' is '$(diff_$(listname1)_$(listname2)_str)'";
}
```

**See also:** [`intersection()`][intersection].
