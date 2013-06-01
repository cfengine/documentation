---
layout: default
title: now
categories: [Reference, Functions, now]
published: true
alias: reference-functions-now.html
tags: [reference, functions, now]
---

**Prototype**: now() 

**Return type**: `int`


Convert the current time into system representation

**Example**:

```cf3
body file_select zero_age
{
mtime       => irange(ago(1,0,0,0,0,0),now);
file_result => "mtime";
}
```

**Notes**:  
   
