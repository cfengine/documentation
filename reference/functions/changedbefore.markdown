---
layout: default
title: changedbefore
categories: [Reference, Functions, changedbefore]
published: true
alias: reference-functions-changedbefore.html
tags: [reference, functions, changedbefore]
---

**Synopsis**: `changedbefore(arg1,arg2)`

**Return type**: `class`

**Description**: Compares the `ctime` fields of two files.

Returns true if arg1 was changed before arg2 (ctime), otherwise returns false.

Change times include both file permissions and file contents.
Comparisons like this are normally used for updating files (like the
'make' command).

**Arguments**:
 
* *arg1* : Newer filename, *in the range* "?(/.\*)
* *arg2* : Older filename, *in the range* "?(/.\*)

**Example**:  

```cf3
    body common control
    {
      bundlesequence  => { "example" };
    }

    bundle agent example
    {     
      classes:

        "do_it" and => { changedbefore("/tmp/earlier","/tmp/later"), "linux" }; 

      reports:

        do_it::

          "The derived file needs updating";
    }
```
