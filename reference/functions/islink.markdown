---
layout: default
title: islink
categories: [Reference, Functions, islink]
published: true
alias: reference-functions-islink.html
tags: [reference, functions, islink]
---



**Synopsis**: islink(arg1) returns type **class**

  
 *arg1* : File object name, *in the range* "?(/.\*)   

True if the named object is a symbolic link

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

  "isdir" expression => islink("/tmp/link");

reports:

  isdir::

    "Directory exists..";

}
```

**Notes**:  
   

The link node must both exist and be a symbolic link. Hard links cannot
be detected using this function. A hard link is a regular file or
directory.
