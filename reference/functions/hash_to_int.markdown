---
layout: default
title: hash_to_int
published: true
tags: [reference, functions, hash_to_int, function_returns_int]
---

[%CFEngine_function_prototype( lower, upper, string )%]

**Description:** Generates an integer between `lower` and `upper` range based on hash of `string`.

**Notes:**

This function is similar to `splayclass()` but more widely usable. Anything that
involves orchestration of many hosts could use this function, either for evenly
spreading out the scheduling, or even for static load balancing. The result
would may be coupled with an `ifelse()` clause of some sort, or just used
directly.

[%CFEngine_function_attributes(lower (inclusive), upper (exclusive), string)%]

**Example:**

[%CFEngine_include_snippet(hash_to_int.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(hash_to_int.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:**

- Introduced in 3.12.0.

**See also:** `splayclass()`
