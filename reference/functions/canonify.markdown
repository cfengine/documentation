---
layout: default
title: canonify
categories: [Reference, Functions, canonify]
published: true
alias: reference-functions-canonify.html
tags: [reference, functions, canonify]
---

### Function canonify

**Synopsis**: canonify(arg1) returns type **string**

  
 *arg1* : String containing non-identifier characters, *in the range*
.\*   

Convert an arbitrary string into a legal class name

**Example**:  
   

```cf3
commands:

   "/var/cfengine/bin/$(component)"

       ifvarclass => canonify("start_$(component)");
```

**Notes**:  
   

This is for use in turning arbitrary text into class data (See [Function
classify](#Function-classify)).
