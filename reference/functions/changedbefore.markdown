---
layout: default
title: changedbefore
categories: [Reference, Functions, changedbefore]
published: true
alias: reference-functions-changedbefore.html
tags: [reference, files functions, functions, changedbefore]
---

[%CFEngine_function_prototype(newer,older)%]

**Description:** Compares the `ctime` fields of two files.

Returns true if `newer` was changed before `older`, otherwise returns false.

Change times include both file permissions and file contents.
Comparisons like this are normally used for updating files (like the
'make' command).

[%CFEngine_function_attributes(newer, older)%]

**Example:**  

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
