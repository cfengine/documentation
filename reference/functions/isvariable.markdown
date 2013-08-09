---
layout: default
title: isvariable
categories: [Reference, Functions, isvariable]
published: true
alias: reference-functions-isvariable.html
tags: [reference, utility functions, functions, isvariable]
---

[%CFEngine_function_prototype(var)%]

**Description:** Returns whether a variable named `var` is defined.

The variable need only exist. This says nothing about its value. Use
`regcmp` to check variable values.

[%CFEngine_function_attributes(var)%]

**Example:**

```cf3
bundle agent example
{     
vars:

  "bla" string => "xyz..";

classes:

  "exists" expression => isvariable("bla");

reports:

  exists::

    "Variable exists: \"$(bla)\"..";

}
```
