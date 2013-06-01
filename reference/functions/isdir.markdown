---
layout: default
title: isdir
categories: [Reference, Functions, isdir]
published: true
alias: reference-functions-isdir.html
tags: [reference, functions, isdir]
---

**Prototype**: isdir(arg1) 

**Return type**: `class`

 *arg1* : File object name, *in the range* "?(/.\*)   

True if the named object is a directory

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

  "isdir" expression => isdir("/etc");

reports:

  isdir::

    "Directory exists..";

}
```

**Notes**:
The CFEngine process must have access to the object concerned in order
for this to work.
