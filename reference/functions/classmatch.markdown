---
layout: default
title: classmatch
categories: [Reference, Functions, classmatch]
published: true
alias: reference-functions-classmatch.html
tags: [reference, functions, classmatch]
---

**Synopsis**: `classmatch(arg1)`

**Return type**: `class`

**Description**: Tests whether `arg1` matches any currently set class.

The regular expression `arg1` is matched against the current list of defined
classes. The regular expression must match a complete class for the expression 
to be true (i.e. the regex is [anchored](manuals-language-concepts-pattern-matching-and-referencing.html#Anchored-vs-unanchored-regular-expressions)).

Returns true if the regular expression matches any currently defined class, 
otherwise returns false.

**Arguments**:

*  *arg1* : Regular expression, *in the range* .\*   

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

