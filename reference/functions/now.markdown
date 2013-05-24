---
layout: default
title: Function now
categories: [Reference, Functions,Function now]
published: true
alias: reference-functions-function-now.html
tags: [reference, functions, function now]
---

### Function now

**Synopsis**: now() returns type **int**

  

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
   
