---
layout: default
title: concat
categories: [Reference, Functions, concat]
published: true
alias: reference-functions-concat.html
tags: [reference, data functions, functions, concat]
---

[%CFEngine_function_prototype(...)%]

**Description:** Concatenates all arguments into a string.

**Example:**  

```cf3
    commands:
      "/usr/bin/generate_config $(config)"
        ifvarclass => concat("have_config_", canonify("$(config)"));
```

**History:** Was introduced in 3.2.0, Nova 2.1.0 (2011)
