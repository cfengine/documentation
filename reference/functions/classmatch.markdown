---
layout: default
title: classmatch
categories: [Reference, Functions, classmatch]
published: true
alias: reference-functions-classmatch.html
tags: [reference, functions, classmatch]
---



**Synopsis**: classmatch(arg1) returns type **class**

  
 *arg1* : Regular expression, *in the range* .\*   

True if the regular expression matches any currently defined class

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

  "do_it" and => { classmatch(".*_cfengine_com"), "linux" }; 

reports:

  do_it::

    "Host matches pattern";

}
```

**Notes**:  
   

The regular expression is matched against the current list of defined
classes. The regular expression must match a complete class for the
expression to be true (i.e. the regex is anchored).

See: [Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions).
