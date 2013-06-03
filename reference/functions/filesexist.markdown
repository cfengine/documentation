---
layout: default
title: filesexist
categories: [Reference, Functions, filesexist]
published: true
alias: reference-functions-filesexist.html
tags: [reference, functions, filesexist]
---

**Prototype**: `filesexist(list)`

**Return type**: `class`

**Description**: Returns whether all the files in `list` can be accessed.

All files must exist, and the user must have access permissions to them for 
this function to return true.

**Arguments**:

* `list` : Reference to a list variable, *in the range*
@[(][a-zA-Z0-9]+[)]

**Example**:

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
