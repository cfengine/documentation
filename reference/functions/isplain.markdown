---
layout: default
title: isplain
categories: [Reference, Functions, isplain]
published: true
alias: reference-functions-isplain.html
tags: [reference, functions, isplain]
---

**Prototype**: isplain(arg1) 

**Return type**: `class`

* `arg1` : File object name, *in the range* "?(/.\*)   

True if the named object is a plain/regular file

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

  "isplain" expression => isplain("/etc/passwd");

reports:

  isplain::

    "File exists..";

}
```

**Notes**:  
   
