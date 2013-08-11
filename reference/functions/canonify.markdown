---
layout: default
title: canonify
categories: [Reference, Functions, canonify]
published: true
alias: reference-functions-canonify.html
tags: [reference, data functions, functions, canonify]
---

[%CFEngine_function_prototype(text)%]

**Description:** Convert an arbitrary string `text` into a legal class name.

This function turns arbitrary text into class data.

[%CFEngine_function_attributes(text)%]

**Example:**  


```cf3
    commands:

       "/var/cfengine/bin/$(component)"

           ifvarclass => canonify("start_$(component)");
```

**See also:** [classify()][classify]).
