---
layout: default
title: difference
categories: [Reference, Functions, difference]
published: true
alias: reference-functions-difference.html
tags: [reference, data functions, functions, difference]
---

[%CFEngine_function_prototype(list1, list2)%]

**Description:** Returns the unique elements in `list1` that are not in 
`list2`.

[%CFEngine_function_attributes(list1, list2)%]

**Example:**

```cf3
body common control
{
      bundlesequence => { "test" };
}

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

Output:

```
R: The difference of list '1,2,3,x' with '1,2,3,x' is ''
R: The difference of list '1,2,3,x' with 'x' is '1,2,3'
R: The difference of list 'x' with '1,2,3,x' is ''
R: The difference of list 'x' with 'x' is ''
```

**See also:** [`intersection()`][intersection].
