---
layout: default
title: classmatch
categories: [Reference, Functions, classmatch]
published: true
alias: reference-functions-classmatch.html
tags: [reference, utility functions, functions, classmatch]
---

[%CFEngine_function_prototype(regex)%]

**Description:** Tests whether `regex` matches any currently set class.

Returns true if the [anchored][anchored] regular expression matches any 
currently defined class, otherwise returns false.

[%CFEngine_function_attributes(text)%]

**Example:**

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

