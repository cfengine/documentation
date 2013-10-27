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

**Notes:**
- At the moment, only the first 4096 bytes of the file can be retrieved.
- To reliably read files located within /proc or /sys directories,
`maxsize` has to be set to `0`.

**History:** 4096 bytes limit and special `0` value were introduced in 3.6.0
