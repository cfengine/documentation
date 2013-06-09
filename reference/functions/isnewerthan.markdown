---
layout: default
title: isnewerthan
categories: [Reference, Functions, isnewerthan]
published: true
alias: reference-functions-isnewerthan.html
tags: [reference, functions, isnewerthan]
---

**Prototype**: `isnewerthan(newer, older)`

**Return type**: `class`

**Description**: Returns whether the file `newer` is newer (modified later) 
than the file `older`.

This function compares the modification time (mtime) of the files, referring 
to changes of content only.

**Arguments**:

* `arg1` : Newer file name, in the range `"?(/.*)`
* `arg2` : Older file name, in the range `"?(/.*)`

**Example**:

```cf3
    bundle agent example
    {     
    classes:

      "do_it" and => { isnewerthan("/tmp/later","/tmp/earlier"), "linux" }; 

    reports:

      do_it::

        "The derived file needs updating";
    }
```
