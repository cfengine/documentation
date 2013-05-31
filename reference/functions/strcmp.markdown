---
layout: default
title: strcmp
categories: [Reference, Functions, strcmp]
published: true
alias: reference-functions-strcmp.html
tags: [reference, functions, strcmp]
---



**Synopsis**: strcmp(arg1,arg2) 

**Return type**: `class`

  
 *arg1* : String, *in the range* .\*   
 *arg2* : String, *in the range* .\*   

True if the two strings match exactly

**Example**:  
   

```cf3
body common control

{
bundlesequence  => { "example" };
}

###########################################################

bundle agent example

{     
classes:

  "same" expression => strcmp("test","test");

reports:

  same::

    "Strings are equal";

 !same::

    "Strings are not equal";
}
```

**Notes**:  
   
