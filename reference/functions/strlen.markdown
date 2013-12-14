---
layout: default
title: strlen
categories: [Reference, Functions, strlen]
published: true
alias: reference-functions-strlen.html
tags: [reference, text functions, functions, text, strlen, substring]
---

[%CFEngine_function_prototype(data)%]

**Description:** Returns the byte length of `data`.

[%CFEngine_function_attributes(data)%]

**Example:**

```cf3
bundle agent example
{
    vars:
      "length" int =>  strlen("abc"); # will contain "3"
    reports:
      "length of string abc = $(length}";
}
```

**History:** Introduced in CFEngine 3.6

**See also:** `head()`, `tail()`, `reversestring()`.
