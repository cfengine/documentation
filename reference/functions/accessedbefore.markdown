---
layout: default
title: Function accessedbefore
categories: [Reference, Functions,Function accessedbefore]
published: true
alias: reference-functions-accessedbefore.html
tags: [reference, functions, function accessedbefore]
---

### Function accessedbefore

**Synopsis**: accessedbefore(arg1,arg2) returns type **class**

  
 *arg1* : Newer filename, *in the range* "?(/.\*)   
 *arg2* : Older filename, *in the range* "?(/.\*)   

True if arg1 was accessed before arg2 (atime)

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

  "do_it" and => { accessedbefore("/tmp/earlier","/tmp/later"), "linux" }; 

reports:

  do_it::

    "The secret changes have been accessed after the reference time";

}
```

**Notes**:  
   

The function accesses the `atime` fields of a file and makes a
comparison.

```cf3
     
      touch /tmp/reference
      touch /tmp/secretfile
     
      /var/cfengine/bin/cf-agent -f ./unit_accessed_before.cf -K
      R: The secret changes have been accessed after the reference time
     
```
