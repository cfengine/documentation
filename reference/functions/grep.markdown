---
layout: default
title: grep
categories: [Reference, Functions, grep]
published: true
alias: reference-functions-grep.html
tags: [reference, functions, grep]
---

**Prototype**: `grep(regex, list)`

**Return type**: `slist`

**Description**: Returns the sub-list if items  in `list` matching the regular expression `regex`.

**Arguments**:

* `regex` : Regular expression, *in the range* .\*

The regex is [anchored][anchored].

* `list` : list identifier, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+

**Example**:

```cf3
bundle agent test
{
vars:

  "mylist" slist => { "One", "Two", "Three", "Four", "Five" };
  "sublist" slist => grep("T.*","mylist");
  "empty_list" slist => grep("ive","mylist");

reports:

 linux::

  "Item: $(sublist)";

}
```
