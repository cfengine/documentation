---
layout: default
title: join
categories: [Reference, Functions, join]
published: true
alias: reference-functions-join.html
tags: [reference, functions, join]
---

**Prototype**: join(arg1,arg2) 

**Return type**: `string`

  
 *arg1* : Join glue-string, *in the range* .\*   
 *arg2* : CFEngine list identifier, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+   

Join the items of arg2 into a string, using the conjunction in arg1

**Example**:

```cf3
bundle agent test

{
vars:

  "mylist" slist => { "one", "two", "three", "four", "five" };

  "scalar" string => join("->","mylist");

reports:

 linux::

  "Concatenated $(scalar)";

}
```

**Notes**:
Converts a string of type list into a scalar variable using the join
string in first argument.
