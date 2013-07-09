---
layout: default
title: filesexist
categories: [Reference, Functions, filesexist]
published: true
alias: reference-functions-filesexist.html
tags: [reference, files functions, functions, filesexist]
---

[%CFEngine_function_prototype(list)%]

**Description:** Returns whether all the files in `list` can be accessed.

All files must exist, and the user must have access permissions to them for 
this function to return true.

[%CFEngine_function_attributes(list)%]

**Example:**

```cf3
    body common control

    {
      bundlesequence  => { "example" };
    }

    bundle agent example

    {     
      vars:

        "mylist" slist => { "/tmp/a", "/tmp/b", "/tmp/c" };

      classes:

        "exists" expression => filesexist("@(mylist)");

      reports:

        exists::

          "All files exist";

        !exists::

          "Not all files exist";
    }
```
