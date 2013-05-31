---
layout: default
title: diskfree
categories: [Reference, Functions, diskfree]
published: true
alias: reference-functions-diskfree.html
tags: [reference, functions, diskfree]
---

**Synopsis**: `diskfree(path)`

**Return type**: `int`

**Descriptions**: Return the free space (in KB) available on the current
partition of `path`.

If `path` is not found, this function returns 0.

**Arguments**:  

* `path` : File system directory, *in the range* "?(/.\*)   

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
