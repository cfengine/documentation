---
layout: default
title: Function isplain
categories: [Reference, Functions,Function isplain]
published: true
alias: reference-functions-function-isplain.html
tags: [reference, functions, function isplain]
---

### Function isplain

**Synopsis**: isplain(arg1) returns type **class**

  
 *arg1* : File object name, *in the range* "?(/.\*)   

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
   
