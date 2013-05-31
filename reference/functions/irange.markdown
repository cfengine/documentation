---
layout: default
title: irange
categories: [Reference, Functions, irange]
published: true
alias: reference-functions-irange.html
tags: [reference, functions, irange]
---



**Synopsis**: irange(arg1,arg2) 

**Return type**:
 **irange [int,int]**

  
 *arg1* : Integer, *in the range* -99999999999,9999999999   
 *arg2* : Integer, *in the range* -99999999999,9999999999   

Define a range of integer values for cfengine internal use

**Example**:  
   

```cf3
irange("1","100");

irange(ago(0,0,0,1,30,0), "0");
```

**Notes**:  
   

Used for any scalar attribute which requires an integer range. You can
generally interchangeably say "1,10" or irange("1","10"). However, if
you want to create a range of dates or times, you must use irange if you
also use the functions ago, now, accumulated, etc.
