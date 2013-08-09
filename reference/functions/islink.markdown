---
layout: default
title: islink
categories: [Reference, Functions, islink]
published: true
alias: reference-functions-islink.html
tags: [reference, files functions, functions, islink]
---

[%CFEngine_function_prototype(filename)%]

**Description:** Returns whether the named object `filename` is a symbolic 
link.

The link node must both exist and be a symbolic link. Hard links cannot
be detected using this function.

[%CFEngine_function_attributes(filename)%]

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
