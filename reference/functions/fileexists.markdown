---
layout: default
title: fileexists
categories: [Reference, Functions, fileexists]
published: true
alias: reference-functions-fileexists.html
tags: [reference, files functions, functions, fileexists]
---

[%CFEngine_function_prototype(filename)%]

**Description:** Returns whether the file `filename` can be accessed.

The file must exist, and the user must have access permissions to the file for 
this function to return true.

[%CFEngine_function_attributes(filename)%]

**Example:**  

```cf3
    body common control
    {
      bundlesequence  => { "example" };
    }

    bundle agent example
    {     
      classes:

        "exists" expression => fileexists("/etc/passwd");

      reports:

        exists::

          "File exists";
    }
```

