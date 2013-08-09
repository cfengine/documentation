---
layout: default
title: isplain
categories: [Reference, Functions, isplain]
published: true
alias: reference-functions-isplain.html
tags: [reference, files functions, functions, isplain]
---

[%CFEngine_function_prototype(filename)%]

**Description:** Returns whether the named object `filename` is a 
plain/regular file.

[%CFEngine_function_attributes(filename)%]

**Example:**

```cf3
bundle agent example
{
classes:

  "isplain" expression => isplain("/etc/passwd");

reports:

  isplain::

    "File exists..";

}
```
