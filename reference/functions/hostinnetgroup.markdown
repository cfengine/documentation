---
layout: default
title: hostinnetgroup
categories: [Reference, Functions, hostinnetgroup]
published: true
alias: reference-functions-hostinnetgroup.html
tags: [reference, functions, hostinnetgroup]
---



**Prototype**: hostinnetgroup(arg1) 

**Return type**: `class`

  
 *arg1* : Netgroup name, *in the range* .\*   

True if the current host is in the named netgroup

**Example**:  
   

```cf3
classes:

  "ingroup" expression => hostinnetgroup("my_net_group");
```

**Notes**:  
   
