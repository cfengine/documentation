---
layout: default
title: now
categories: [Reference, Functions, now]
published: true
alias: reference-functions-now.html
tags: [reference, system functions, functions, now]
---

[%CFEngine_function_prototype()%]

**Description:** Return the current time in system representation.

**Example:**

```cf3
    body file_select zero_age
    {
      mtime       => irange(ago(1,0,0,0,0,0),now);
      file_result => "mtime";
    }
```
