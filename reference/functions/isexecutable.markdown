---
layout: default
title: isexecutable
categories: [Reference, Functions, isexecutable]
published: true
alias: reference-functions-isexecutable.html
tags: [reference, functions, isexecutable]
---

**Prototype**: isexecutable(arg1) 

**Return type**: `class`

  
 *arg1* : File object name, *in the range* "?(/.\*)   

True if the named object has execution rights for the current user

**Example**:

```cf3
classes:

  "yes" expression => isexecutable("/bin/ls");
```

**Notes**:
**History**: Was introduced in version 3.1.0b1,Nova 2.0.0b1 (2010)
