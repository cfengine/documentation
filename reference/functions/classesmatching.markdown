---
layout: default
title: classesmatching
categories: [Reference, Functions, classesmatching]
published: true
alias: reference-functions-classesmatching.html
tags: [reference, functions, classesmatching]
---



**Synopsis**: classesmatching(arg1) 

**Return type**: `slist`

  
 *arg1* : Regular expression, *in the range* .\*   

Return the defined classes matching regex arg1

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

**Notes**:  
   
This function searches for the regular expression in the list of
currently defined classes (hard, then soft, then local to the current
bundle).

This function replaces the `allclasses.txt` static file available
in older versions of CFEngine.

regex

A regular expression matching zero or more classes in the current list
of defined classes. The regular expression is not anchored
(See [Anchored vs. unanchored regular expressions](#Anchored-vs_002e-unanchored-regular-expressions)).

The function returns the list of classes matched.
