---
layout: default
title: classesmatching
categories: [Reference, Functions, classesmatching]
published: true
alias: reference-functions-classesmatching.html
tags: [reference, utility functions, functions, classesmatching]
---

[%CFEngine_function_prototype(regex, tag1, tag2, ...)%]

**Description:** Return the list of set classes matching `regex` and any tags given.

This function searches for the [unanchored][unanchored] regular expression in 
the list of currently set classes (in order hard, then soft, then local to the 
current bundle).

When any tags are given, only the classes with those tags are returned.

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
          "all" slist => classesmatching(".*");
          "c" slist => classesmatching("cfengine");
          "c_plus_plus" slist => classesmatching("cfengine", "plus");
      reports:
          "All classes = $(all)";
          "Classes matching 'cfengine' = $(c)";
          "Classes matching 'cfengine' with the 'plus' tag = $(c_plus_plus)";
    }

```


**Note**: This function replaces the `allclasses.txt` static file available
in older versions of CFEngine.

**History:** Introduced in CFEngine 3.6
