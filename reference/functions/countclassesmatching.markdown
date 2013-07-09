---
layout: default
title: countclassesmatching
categories: [Reference, Functions, countclassesmatching]
published: true
alias: reference-functions-countclassesmatching.html
tags: [reference, utility functions, functions, countclassesmatching]
---

[%CFEngine_function_prototype(regex)%]

**Description:** Count the number of defined classes matching `regex`.

This function matches classes, using an [anchored][anchored] regular 
expression that should match the whole line. The function returns the number 
of classes matched.

[%CFEngine_function_attributes(regex)%]

**Example:**  

```cf3
    bundle agent example
    {
      vars:
        "num" int => countclassesmatching("entropy.*low");

      reports:
        "Found $(num) classes matching";
    }
```
