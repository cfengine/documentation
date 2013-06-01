---
layout: default
title: readfile
categories: [Reference, Functions, readfile]
published: true
alias: reference-functions-readfile.html
tags: [reference, functions, readfile]
---

**Prototype**: readfile(arg1,arg2) 

**Return type**: `string`

* `arg1` : File name, *in the range* "?(/.\*)   
* `arg2` : Maximum number of bytes to read, *in the range* 0,99999999999

Read max number of bytes from named file and assign to variable

**Example**:

```cf3
vars:

 "xxx"   

    string => readfile( "/home/mark/tmp/testfile" , "33" );
```

**Notes**:
The file (fragment) is read into a single scalar variable.
