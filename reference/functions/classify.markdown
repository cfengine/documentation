---
layout: default
title: classify
categories: [Reference, Functions, classify]
published: true
alias: reference-functions-classify.html
tags: [reference, data functions, functions, classify]
---

[%CFEngine_function_prototype(text)%]

**Description:** Returns whether the canonicalization of `text` is a currently 
set class.

This is useful for transforming variables into classes.

[%CFEngine_function_attributes(text)%]

**Example:**  

```cf3
    classes:

     "i_am_the_policy_host" expression => classify("master.example.org");
```

**See also:** [canonify()][canonify]
