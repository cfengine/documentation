---
layout: default
title: islessthan
categories: [Reference, Functions, islessthan]
published: true
alias: reference-functions-islessthan.html
tags: [reference, functions, islessthan]
---

### Function islessthan

**Synopsis**: islessthan(arg1,arg2) returns type **class**

  
 *arg1* : Smaller string or value, *in the range* .\*   
 *arg2* : Larger string or value, *in the range* .\*   

True if arg1 is numerically less than arg2, else compare strings like
NOT strcmp

**Example**:  
   

```cf3
body common control

{
bundlesequence  => { "test"  };
}

###########################################################

bundle agent test

{
classes:

  "ok" expression => islessthan("0","1");

reports:

  ok::

    "Assertion is true";

 !ok::

  "Assertion is false";

}
```

**Notes**:  
   

The complement of `isgreaterthan`. The comparison is made numerically if
possible. If the values are strings, the result is identical to that of
comparing with strcmp().
