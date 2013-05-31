---
layout: default
title: classmatch
categories: [Reference, Functions, classmatch]
published: true
alias: reference-functions-classmatch.html
tags: [reference, functions, classmatch]
---

**Synopsis**: `classmatch(regex)`

**Return type**: `class`

**Description**: Tests whether `regex` matches any currently set class.

Returns true if the regular expression matches any currently defined class, 
otherwise returns false.

**Arguments**:

* `regex` : Regular expression, *in the range* .\*

A regular expression matched against the current list of set classes. The 
regular expression must match a complete class for the expression to be true 
(i.e. the regex is 
[anchored](manuals-language-concepts-pattern-matching-and-referencing.html#Anchored-vs-unanchored-regular-expressions)).

**Example**:  
   

```cf3
    body common control
    {
      bundlesequence  => { "example" };
    }

    bundle agent example
    {     
      classes:

        "do_it" and => { classmatch(".*_cfengine_com"), "linux" }; 

      reports:

        do_it::

          "Host matches pattern";
    }
```

