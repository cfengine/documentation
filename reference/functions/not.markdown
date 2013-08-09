---
layout: default
title: not
categories: [Reference, Functions, not]
published: true
alias: reference-functions-not.html
tags: [reference, data functions, functions, not]
---

[%CFEngine_function_prototype(expression)%]

**Description:** Calculate whether `expression` is false

[%CFEngine_function_attributes(expression)%]

**Example:**

```cf3
commands:
  "/usr/bin/generate_config $(config)"
    ifvarclass => not(fileexists("/etc/config/$(config)"));
```

**Notes:**  
   
**History:** Was introduced in 3.2.0, Nova 2.1.0 (2011)
