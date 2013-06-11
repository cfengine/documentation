---
layout: default
title: readfile
categories: [Reference, Functions, readfile]
published: true
alias: reference-functions-readfile.html
tags: [reference, functions, readfile]
---

**Prototype**: `readfile(filename, maxbytes)`

**Return type**: `string`

**Description:** Returns the first `maxbytes` bytes from file `filename`.

**Arguments**:

* `filename` : File name, in the range `"?(/.*)`
* `maxbytes` : Maximum number of bytes to read, in the range `0,99999999999`

**Example:**

```cf3
    vars:

     "xxx"   
        string => readfile( "/home/mark/tmp/testfile" , "33" );
```

