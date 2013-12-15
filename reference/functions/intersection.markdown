---
layout: default
title: intersection
categories: [Reference, Functions, intersection]
published: true
alias: reference-functions-intersection.html
tags: [reference, data functions, functions, intersection]
---

[%CFEngine_function_prototype(list1, list2)%]

**Description:** Returns the unique elements in list1 that are also in list2.

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

      "int_$(listname1)_$(listname2)" slist => intersection($(listname1), $(listname2));
      "int_$(listname1)_$(listname2)_str" string => join(",", "int_$(listname1)_$(listname2)");

  reports:
      "The intersection of list '$($(listname1)_str)' with '$($(listname2)_str)' is '$(int_$(listname1)_$(listname2)_str)'";
}
```

Output:

```
R: The intersection of list '1,2,3,x' with '1,2,3,x' is '1,2,3,x'
R: The intersection of list '1,2,3,x' with 'x' is 'x'
R: The intersection of list 'x' with '1,2,3,x' is 'x'
R: The intersection of list 'x' with 'x' is 'x'
```

**See also:** [`difference()`][difference].
