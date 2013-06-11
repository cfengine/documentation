---
layout: default
title: classify
categories: [Reference, Functions, classify]
published: true
alias: reference-functions-classify.html
tags: [reference, functions, classify]
---

**Prototype**: `classify(text)`

**Return type**: `class`

**Description:** Returns whether the canonicalization of `text` is a currently 
set class.

This is useful for transforming variables into classes.

**Arguments**:

* `text` : Input string, in the range `.*`

**Example:**  

```cf3
    classes:

     "i_am_the_policy_host" expression => classify("master.example.org");
```

**See also:** [canonify()][canonify]
