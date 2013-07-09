---
layout: default
title: grep
categories: [Reference, Functions, grep]
published: true
alias: reference-functions-grep.html
tags: [reference, data functions, functions, grep]
---

[%CFEngine_function_prototype(regex, list)%]

**Description:** Returns the sub-list if items  in `list` matching the 
[anchored][anchored] regular expression `regex`.

[%CFEngine_function_attributes(regex, list)%]

**Example:**

```cf3
bundle agent test
{
vars:

  "mylist" slist => { "One", "Two", "Three", "Four", "Five" };
  "sublist" slist => grep("T.*","mylist");
  "empty_list" slist => grep("ive","mylist");

reports:
  "Item: $(sublist)";
}
```
