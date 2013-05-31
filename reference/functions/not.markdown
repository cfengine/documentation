---
layout: default
title: not
categories: [Reference, Functions, not]
published: true
alias: reference-functions-not.html
tags: [reference, functions, not]
---



**Synopsis**: not(arg1) 

**Return type**: `string`

  
 *arg1* : Class value, *in the range* .\*   

Calculate whether argument is false

**Example**:  
   

```cf3
commands:
  "/usr/bin/generate_config $(config)"
    ifvarclass => not(fileexists("/etc/config/$(config)"));
```

**Notes**:  
   
 *History*: Was introduced in 3.2.0, Nova 2.1.0 (2011)
