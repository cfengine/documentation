---
layout: default
title: filesize
categories: [Reference, Functions, filesize]
published: true
alias: reference-functions-filesize.html
tags: [reference, functions, filesize]
---

**Prototype**: `filesize(filename)`

**Return type**: `int`

**Description**: Returns the size of the file `filename` in bytes.

If the file object does not exist, the function call fails and the
variable does not expand.

**Arguments**:

* `filename` : File object name, *in the range* "?(/.\*)

**Example**:  

```cf3
    bundle agent example
    {     
      vars:

        "exists" int => filesize("/etc/passwd");
        "nexists" int => filesize("/etc/passwdx");

      reports:
        "File size $(exists)";
        "Does not exist $(nexists)";
    }
```


**History**: Was introduced in version 3.1.3,Nova 2.0.2 (2010)
