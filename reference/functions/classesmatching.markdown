---
layout: default
title: classesmatching
categories: [Reference, Functions, classesmatching]
published: true
alias: reference-functions-classesmatching.html
tags: [reference, functions, classesmatching]
---

**Prototype**: `classesmatching(regex)`

**Return type**: `slist`

**Description**: Return the list of set classes matching `regex`.

This function searches for the regular expression in the list of currently set 
classes (in order hard, then soft, then local to the current bundle).

**Arguments**:

* `regex` : Regular expression, in the range `.*`

A regular expression matching zero or more classes in the current list
of set classes. The regular expression is [unanchored][unanchored].

**Example**:  


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
