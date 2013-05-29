---
layout: default
title: difference
categories: [Reference, Functions, difference]
published: true
alias: reference-functions-difference.html
tags: [reference, functions, difference]
---

### Function difference

**Synopsis**: difference(arg1,arg2) returns type **slist**

 *arg1* : The name of the base list variable, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+   

 *arg2* : The name of the subtracted list variable, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+   

Returns the unique elements in arg1 that are not in arg2.

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

      "diff_$(listname1)_$(listname2)" slist => difference($(listname1), $(listname2));
      "diff_$(listname1)_$(listname2)_str" string => join(",", "diff_$(listname1)_$(listname2)");

  reports:
      "The difference of list '$($(listname1)_str)' with '$($(listname2)_str)' is '$(diff_$(listname1)_$(listname2)_str)'";
}
```

**Notes**:  

See also `intersection`.
