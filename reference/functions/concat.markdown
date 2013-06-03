---
layout: default
title: concat
categories: [Reference, Functions, concat]
published: true
alias: reference-functions-concat.html
tags: [reference, functions, concat]
---

**Prototype**: `concat(...)`

**Return type**: `string`

**Description**: Concatenates all arguments into a string.

**Example**:  

```cf3
    commands:
      "/usr/bin/generate_config $(config)"
        ifvarclass => concat("have_config_", canonify("$(config)"));
```

**History**: Was introduced in 3.2.0, Nova 2.1.0 (2011)
