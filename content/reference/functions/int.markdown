---
layout: default
title: int
---

{{< CFEngine_function_prototype(string) >}}

**Description:** Convert numeric string to int.

{{< CFEngine_function_attributes(string) >}}

If `string` represents a floating point number then the decimals are *truncated*.

**Example:**

{{< CFEngine_include_example(int.cf) >}}

**See also:** [`string()`][string]

**History:**

* Introduced in 3.18.0
