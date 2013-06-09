---
layout: default
title: countclassesmatching
categories: [Reference, Functions, countclassesmatching]
published: true
alias: reference-functions-countclassesmatching.html
tags: [reference, functions, countclassesmatching]
---

**Prototype**: `countclassesmatching(regex)`

**Return type**: `int`

**Description**: Count the number of defined classes matching `regex`.

This function matches classes, using a regular expression that should
match the whole line. The function returns the number of classes matched.

**Arguments**:

* `regex` : Regular expression, in the range `.*`

A regular expression matching zero or more classes in the current list
of set classes. The regular expression is 
[anchored][anchored], meaning it must match a complete 
class.

**Example**:  

```cf3
    bundle agent example
    {
      vars:
        "num" int => countclassesmatching("entropy.*low");

      reports:
        "Found $(num) classes matching";
    }
```
