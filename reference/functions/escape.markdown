---
layout: default
title: escape
categories: [Reference, Functions, escape]
published: true
alias: reference-functions-escape.html
tags: [reference, data functions, functions, escape]
---

[%CFEngine_function_prototype(text)%]

**Description:** Escape regular expression characters in `text`.

This function is useful for making inputs readable when a regular
expression is required, but the literal string contains special
characters. The function simply 'escapes' all the regular expression
characters, so that you do not have to.

[%CFEngine_function_attributes(path)%]

**Example:**  


```cf3
    bundle server control
    {
      allowconnects => { "127\.0\.0\.1", escape("192.168.2.1") };
    }
```

In this example, the string "192.168.2.1" is "escaped" to be equivalent to 
"192\\.168\\.2\\.1", because without the backslashes, the regular expression 
"192.168.2.1" will also match the IP ranges "192.168.201", "192.168.231", etc 
(since the dot character means "match any character" when used in a regular 
expression).

**Notes:**  

**History:** This function was introduced in CFEngine version 3.0.4 (2010)
