---
layout: default
title: canonify
categories: [Reference, Functions, canonify]
published: true
alias: reference-functions-canonify.html
tags: [reference, functions, canonify]
---

**Synopsis**: `canonify(arg1)`

**Return type**: `string`

**Description**: Convert an arbitrary string into a legal class name.

This function turns arbitrary text into class data (See
[classify](reference-functions-classfiy.html)).

**Arguments**:

* *arg1* : String containing non-identifier characters, *in the range* .\*   

**Example**:  


```cf3
    commands:

       "/var/cfengine/bin/$(component)"

           ifvarclass => canonify("start_$(component)");
```

