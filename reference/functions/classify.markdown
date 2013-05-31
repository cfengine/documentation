---
layout: default
title: classify
categories: [Reference, Functions, classify]
published: true
alias: reference-functions-classify.html
tags: [reference, functions, classify]
---

**Synopsis**: `classify(arg1)`

**Return type**: `class`

**Description**: Returns whether the canonicalization of `arg1` is a currently 
set class.

This is useful for transforming variables into classes. See also 
[canonify](reference-functions-canonify.html).

**Arguments**:

* *arg1* : Input string, *in the range* .\*

**Example**:  

```cf3
    classes:

     "i_am_the_policy_host" expression => classify("master.example.org");
```

