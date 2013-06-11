---
layout: default
title: islink
categories: [Reference, Functions, islink]
published: true
alias: reference-functions-islink.html
tags: [reference, files functions, functions, islink]
---

**Prototype:** `islink(filename)`

**Return type:** `class`

**Description:** Returns whether the named object `filename` is a symbolic 
link.

The link node must both exist and be a symbolic link. Hard links cannot
be detected using this function.

**Arguments**:

* `filename` : File object name, in the range `"?(/.*)`

**Example:**

```cf3
bundle agent example
{     
classes:

  "islink" expression => islink("/tmp/link");

reports:

  islink::

    "It's a link.";

}
```
