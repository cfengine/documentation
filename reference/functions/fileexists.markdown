---
layout: default
title: fileexists
categories: [Reference, Functions, fileexists]
published: true
alias: reference-functions-fileexists.html
tags: [reference, functions, fileexists]
---



**Synopsis**: fileexists(arg1) 

**Return type**: `class`

  
 *arg1* : File object name, *in the range* "?(/.\*)   

True if the named file can be accessed

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

  "exists" expression => fileexists("/etc/passwd");

reports:

  exists::

    "File exists";

}
```

**Notes**:  
   

The user must have access permissions to the file for this to work
faithfully.
