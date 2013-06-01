---
layout: default
title: strcmp
categories: [Reference, Functions, strcmp]
published: true
alias: reference-functions-strcmp.html
tags: [reference, functions, strcmp]
---

**Prototype**: `strcmp(string1, string2)`

**Return type**: `class`

**Description**: Returns whether the two strings `string1` and `string2` match 
exactly.

**Arguments**:

* `string1` : The first string, *in the range* .\*
* `string2` : The second string, *in the range* .\*

**Example**:

```cf3
bundle agent example
{     
classes:

  "same" expression => strcmp("test","test");

reports:

  same::

    "Strings are equal";

 !same::

    "Strings are not equal";
}
```
