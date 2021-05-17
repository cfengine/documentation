---
layout: default
title: int
published: true
tags: [reference, functions, int]
---

[%CFEngine_function_prototype(string)%]

**Description:** Convert numeric string to int.

[%CFEngine_function_attributes(string)%]

If `string` represents a floating point number then the decimals are *truncated*.

**Example:**

[%CFEngine_include_example(int.cf)%]

**See Also:** [`string()`][string]

**History:**

* Introduced in 3.18.0
