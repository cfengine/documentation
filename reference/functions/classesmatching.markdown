---
layout: default
title: classesmatching
categories: [Reference, Functions, classesmatching]
published: true
alias: reference-functions-classesmatching.html
tags: [reference, utility functions, functions, classesmatching]
---

[%CFEngine_function_prototype(regex)%]

**Description:** Return the list of set classes matching `regex`.

This function searches for the [unanchored][unanchored] regular expression in 
the list of currently set classes (in order hard, then soft, then local to the 
current bundle).

[%CFEngine_function_attributes(regex)%]

**Example:**  


```cf3
    body common control
    {
      bundlesequence => { run };
    }

    bundle agent run
    {
      vars:
          "all" slist => classesmatching(".*");
          "c" slist => classesmatching("cfengine");
      reports:
          "All classes = $(all)";
          "Classes matching 'cfengine' = $(c)";
    }

```


**Note**: This function replaces the `allclasses.txt` static file available
in older versions of CFEngine.
