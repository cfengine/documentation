---
layout: default
title: join
categories: [Reference, Functions, join]
published: true
alias: reference-functions-join.html
tags: [reference, functions, join]
---

**Prototype**: `join(glue, list)`

**Return type**: `string`

**Description**: Join the items of `list` into a string, using the conjunction in `glue`.

Converts a string of type list into a scalar variable using the join
string in first argument.

**Arguments**:

* `glue` : Join glue-string, *in the range* .\*
* `list` : CFEngine list identifier, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+

**Example**:

```cf3
bundle agent test
{
vars:

  "mylist" slist => { "one", "two", "three", "four", "five" };

  "scalar" string => join("->","mylist");

reports:

 linux::

  "Concatenated $(scalar)";
}
```
