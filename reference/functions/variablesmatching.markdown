---
layout: default
title: variablesmatching
categories: [Reference, Functions, variablesmatching]
published: true
alias: reference-functions-variablesmatching.html
tags: [reference, utility functions, functions, variablesmatching]
---

[%CFEngine_function_prototype(regex, tag1, tag2, ...)%]

**Description:** Return the list of variables matching `regex` and any tags given.

This function searches for the [unanchored][unanchored] regular expression in 
the list of currently defined variables.

When any tags are given, only the variables with those tags are returned.

[%CFEngine_function_attributes(regex, tag1, tag2, ...)%]

**Example:**  


```cf3
    body common control
    {
      bundlesequence => { run };
    }

    bundle agent run
    {
      vars:
          "all" slist => variablesmatching(".*");
          "c" slist => variablesmatching("sys");
          "c_plus_plus" slist => variablesmatching("sys", "plus");
      reports:
          "All classes = $(all)";
          "Classes matching 'sys' = $(c)";
          "Classes matching 'sys' with the 'plus' tag = $(c_plus_plus)";
    }

```

**History:** Introduced in CFEngine 3.6
