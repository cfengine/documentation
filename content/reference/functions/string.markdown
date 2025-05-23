---
layout: default
title: string
date: 2025-05-22T00:00:00+00:00
---

[%CFEngine_function_prototype(arg)%]

**Description:** Convert `arg` to string.

[%CFEngine_function_attributes(arg)%]

If `arg` is a container reference it will be serialized to a string.
The reference must be indicated with `@(some_container)`.
Strings are *not* interpreted as references.

**Example:**

[%CFEngine_include_example(string.cf)%]

**See also:** [`int()`][int]

**History:**

* Introduced in 3.18.0
