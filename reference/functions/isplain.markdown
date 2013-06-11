---
layout: default
title: isplain
categories: [Reference, Functions, isplain]
published: true
alias: reference-functions-isplain.html
tags: [reference, functions, isplain]
---

**Prototype**: `isplain(filename)`

**Return type**: `class`

**Description:** Returns whether the named object `filename` is a 
plain/regular file.

**Arguments**:

* `arg1` : File object name, in the range `"?(/.*)`

**Example:**

```cf3
bundle agent example
{
classes:

  "isplain" expression => isplain("/etc/passwd");

reports:

  isplain::

    "File exists..";

}
```
