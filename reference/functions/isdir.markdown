---
layout: default
title: isdir
categories: [Reference, Functions, isdir]
published: true
alias: reference-functions-isdir.html
tags: [reference, functions, isdir]
---

**Prototype**: `isdir(filename)`

**Return type**: `class`

**Description:** Returns whether the named object `filename` is a directory.

The CFEngine process must have access to `filename` in order for this to work.

**Arguments**:

* `filename` : File object name, in the range `"?(/.*)`

**Example:**

```cf3
bundle agent example
{     
classes:

  "isdir" expression => isdir("/etc");

reports:

  isdir::

    "Directory exists..";

}
```
