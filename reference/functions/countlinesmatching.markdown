---
layout: default
title: countlinesmatching
categories: [Reference, Functions, countlinesmatching]
published: true
alias: reference-functions-countlinesmatching.html
tags: [reference, functions, countlinesmatching]
---

**Prototype**: `countlinesmatching(regex, filename)`

**Return type**: `int`

**Description**: Count the number of lines in file `filename` matching 
`regex`.

This function matches lines in the named file, using a regular expression that should match the whole line, and returns the number of lines matched.

**Arguments**:

* `regex`, *in the range* .\*

A regular expression matching zero or more lines. The regular expression is 
[anchored][anchored],

* *filename*, *in the range* "?(/.\*)

The name of the file to be examined.

**Example**:

```cf3
    bundle agent example
    {     
      vars:

        "no" int => countlinesmatching("m.*","/etc/passwd");

      reports:

        cfengine_3::

          "Found $(no) lines matching";
    }
```
