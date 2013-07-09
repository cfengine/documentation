---
layout: default
title: diskfree
categories: [Reference, Functions, diskfree]
published: true
alias: reference-functions-diskfree.html
tags: [reference, files functions, functions, diskfree]
---

[%CFEngine_function_prototype(path)%]

**Descriptions**: Return the free space (in KB) available on the current
partition of `path`.

If `path` is not found, this function returns 0.

[%CFEngine_function_attributes(path)%]

**Example:**  

```cf3
    bundle agent example
    {     
      vars:
        "free" int => diskfree("/tmp"); 

      reports:
        "Freedisk $(free)";
    }
```
