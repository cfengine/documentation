---
layout: default
title: strcmp
categories: [Reference, Functions, strcmp]
published: true
alias: reference-functions-strcmp.html
tags: [reference, data functions, functions, strcmp]
---

[%CFEngine_function_prototype(string1, string2)%]

**Description:** Returns whether the two strings `string1` and `string2` match 
exactly.

[%CFEngine_function_attributes(string1, string2)%]

**Example:**

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
