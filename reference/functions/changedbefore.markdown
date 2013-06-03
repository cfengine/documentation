---
layout: default
title: changedbefore
categories: [Reference, Functions, changedbefore]
published: true
alias: reference-functions-changedbefore.html
tags: [reference, functions, changedbefore]
---

**Prototype**: `changedbefore(newer, older)`

**Return type**: `class`

**Description**: Compares the `ctime` fields of two files.

Returns true if `newer` was changed before `older`, otherwise returns false.

Change times include both file permissions and file contents.
Comparisons like this are normally used for updating files (like the
'make' command).

**Arguments**:
 
* `newer` : Newer filename, *in the range* "?(/.\*)
* `older` : Older filename, *in the range* "?(/.\*)

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
