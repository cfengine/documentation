---
layout: default
title: readfile
categories: [Reference, Functions,Function readfile]
published: true
alias: reference-functions-readfile.html
tags: [reference, functions, function readfile]
---

### Function readfile

**Synopsis**: readfile(arg1,arg2) returns type **string**

  
 *arg1* : File name, *in the range* "?(/.\*)   
 *arg2* : Maximum number of bytes to read, *in the range* 0,99999999999
  

Read max number of bytes from named file and assign to variable

**Example**:  
   

```cf3
vars:

 "xxx"   

    string => readfile( "/home/mark/tmp/testfile" , "33" );
```

**Notes**:  
   

The file (fragment) is read into a single scalar variable.
