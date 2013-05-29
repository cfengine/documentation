---
layout: default
title: intersection
categories: [Reference, Functions, intersection]
published: true
alias: reference-functions-intersection.html
tags: [reference, functions, intersection]
---

### Function intersection

**Synopsis**: intersection(arg1,arg2) returns type **slist**

 *arg1* : The name of the base list variable, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+   

 *arg2* : The name of the intersected list variable, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+   

Returns the unique elements in arg1 that are also in arg2.

**Example**:  
   

```cf3
undle agent test

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
