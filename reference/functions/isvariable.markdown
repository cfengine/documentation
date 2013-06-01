---
layout: default
title: isvariable
categories: [Reference, Functions, isvariable]
published: true
alias: reference-functions-isvariable.html
tags: [reference, functions, isvariable]
---

**Prototype**: isvariable(arg1) 

**Return type**: `class`

* `arg1` : Variable identifier, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+

True if the named variable is defined

**Example**:

```cf3
body common control

{
bundlesequence  => { "example" };
}

###########################################################

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

**Notes**:
The variable need only exist. This says nothing about its value. Use
`regcmp` to check variable values.
