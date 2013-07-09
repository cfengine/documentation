---
layout: default
title: or
categories: [Reference, Functions, or]
published: true
alias: reference-functions-or.html
tags: [reference, data functions, functions, or]
---

[%CFEngine_function_prototype(...)%]

**Description:** Calculate whether any argument evaluates to true

**Example:**

```cf3
    commands:
      "/usr/bin/generate_config $(config)"
        ifvarclass => or(not(fileexists("/etc/config/$(config)")), "force_configs");
```

**Notes:**  

**History:** Was introduced in 3.2.0, Nova 2.1.0 (2011)
