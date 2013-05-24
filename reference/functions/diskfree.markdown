---
layout: default
title: Function diskfree
categories: [Reference, Functions, diskfree]
published: true
alias: reference-functions-diskfree.html
tags: [reference, functions, diskfree]
---

### Function diskfree

**Synopsis**: diskfree(arg1) returns type **int**

  
 *arg1* : File system directory, *in the range* "?(/.\*)   

Return the free space (in KB) available on the directory's current
partition (0 if not found)

**Example**:  
   

```cf3
bundle agent example
{     
vars:

  "free" int => diskfree("/tmp"); 

reports:

  cfengine_3::

    "Freedisk $(free)";

}
```

**Notes**:  
   

Values returned in kilobytes.
