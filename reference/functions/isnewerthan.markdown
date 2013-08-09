---
layout: default
title: isnewerthan
categories: [Reference, Functions, isnewerthan]
published: true
alias: reference-functions-isnewerthan.html
tags: [reference, files functions, functions, isnewerthan]
---

[%CFEngine_function_prototype(newer, older)%]

**Description:** Returns whether the file `newer` is newer (modified later) 
than the file `older`.

This function compares the modification time (mtime) of the files, referring 
to changes of content only.

[%CFEngine_function_attributes(newer, older)%]

**Example:**

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
