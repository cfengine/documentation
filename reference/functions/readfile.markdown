---
layout: default
title: readfile
categories: [Reference, Functions, readfile]
published: true
alias: reference-functions-readfile.html
tags: [reference, io functions, functions, readfile]
---

[%CFEngine_function_prototype(filename, maxbytes)%]

**Description:** Returns the first `maxbytes` bytes from file `filename`.

[%CFEngine_function_attributes(filename, maxbytes)%]

**Example:**

```cf3
    vars:

     "xxx"   
        string => readfile( "/home/mark/tmp/testfile" , "33" );
```

