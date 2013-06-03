---
layout: default
title: isvariable
categories: [Reference, Functions, isvariable]
published: true
alias: reference-functions-isvariable.html
tags: [reference, functions, isvariable]
---

**Prototype**: `isvariable(var)`

**Return type**: `class`

**Description**: Returns whether a variable named `var` is defined.

The variable need only exist. This says nothing about its value. Use
`regcmp` to check variable values.

**Arguments**:

* `var` : Variable identifier, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+

**Example**:

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
