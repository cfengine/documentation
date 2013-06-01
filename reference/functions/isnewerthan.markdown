---
layout: default
title: isnewerthan
categories: [Reference, Functions, isnewerthan]
published: true
alias: reference-functions-isnewerthan.html
tags: [reference, functions, isnewerthan]
---

**Prototype**: isnewerthan(arg1,arg2) 

**Return type**: `class`

  
 *arg1* : Newer file name, *in the range* "?(/.\*)   
 *arg2* : Older file name, *in the range* "?(/.\*)   

True if arg1 is newer (modified later) than arg2 (mtime)

**Example**:

```cf3
body common control

{
bundlesequence  => { "example" };
}

###########################################################

bundle agent example

{     
classes:

  "do_it" and => { isnewerthan("/tmp/later","/tmp/earlier"), "linux" }; 

reports:

  do_it::

    "The derived file needs updating";

}
```

**Notes**:
This function compares the modification time of the file, referring to
changes of content only.
