---
layout: default
title: changedbefore
categories: [Reference, Functions, changedbefore]
published: true
alias: reference-functions-changedbefore.html
tags: [reference, functions, changedbefore]
---

### Function changedbefore

**Synopsis**: changedbefore(arg1,arg2) returns type **class**

  
 *arg1* : Newer filename, *in the range* "?(/.\*)   
 *arg2* : Older filename, *in the range* "?(/.\*)   

True if arg1 was changed before arg2 (ctime)

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

  "do_it" and => { changedbefore("/tmp/earlier","/tmp/later"), "linux" }; 

reports:

  do_it::

    "The derived file needs updating";

}
```

**Notes**:  
   

Change times include both file permissions and file contents.
Comparisons like this are normally used for updating files (like the
\`make' command).
