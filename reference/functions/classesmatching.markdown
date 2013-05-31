---
layout: default
title: classesmatching
categories: [Reference, Functions, classesmatching]
published: true
alias: reference-functions-classesmatching.html
tags: [reference, functions, classesmatching]
---

**Synopsis**: `classesmatching(arg1)`

**Return type**: `slist`

**Description**: Return the list of set classes matching regex `arg1`.

This function searches for the regular expression in the list of currently set 
classes (in order hard, then soft, then local to the current bundle).


**Arguments**:

* *arg1* : Regular expression, *in the range* .\*   

A regular expression matching zero or more classes in the current list
of defined classes. The regular expression is not [anchored](manuals-language-concepts-pattern-matching-and-referencing.html#Anchored-vs-unanchored-regular-expressions)).

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
