---
layout: default
title: countlinesmatching
categories: [Reference, Functions, countlinesmatching]
published: true
alias: reference-functions-countlinesmatching.html
tags: [reference, io functions, functions, countlinesmatching]
---

[%CFEngine_function_prototype(regex, filename)%]

**Description:** Count the number of lines in file `filename` matching 
`regex`.

This function matches lines in the named file, using an [anchored][anchored] 
regular expression that should match the whole line, and returns the number of 
lines matched.

[%CFEngine_function_attributes(regex, filename)%]

**Example:**

```cf3
    bundle agent example
    {     
      vars:

        "no" int => countlinesmatching("m.*","/etc/passwd");

      reports:
        "Found $(no) lines matching";
    }
```
