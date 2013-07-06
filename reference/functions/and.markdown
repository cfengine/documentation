---
layout: default
title: and
categories: [Reference, Functions, and]
published: true
alias: reference-functions-and.html
tags: [reference, data functions, functions, and]
---

[%CFEngine_function_prototype(...)%]

**Description:** Returns whether all arguments evaluate to true.

**Arguments**: A list of classes and class expressions

**Example:**

```cf3
    commands:
      "/usr/bin/generate_config $(config)"
        ifvarclass => and(not(fileexists("/etc/config/$(config)")), "generating_configs");
```

**Notes:**  
   
**History:** Was introduced in 3.2.0, Nova 2.1.0 (2011)
