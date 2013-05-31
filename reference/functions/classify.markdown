---
layout: default
title: classify
categories: [Reference, Functions, classify]
published: true
alias: reference-functions-classify.html
tags: [reference, functions, classify]
---



**Synopsis**: classify(arg1) returns type **class**

  
 *arg1* : Input string, *in the range* .\*   

True if the canonicalization of the argument is a currently defined
class

**Example**:  
   

```cf3
classes:

 "i_am_the_policy_host" expression => classify("master.example.org");
```

**Notes**:  
   

This function returns true if the canonical form of the argument is
already a defined class. This is useful for transforming variables into
classes.

See: [Function canonify](#Function-canonify).
