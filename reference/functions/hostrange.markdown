---
layout: default
title: hostrange
published: true
tags: [reference, communication functions, functions, hostrange]
---

[%CFEngine_function_prototype(prefix, range)%]

**Description:** Returns whether the current host lies in the `range` of
enumerated hostnames specified with `prefix`.

This is a pattern matching function for non-regular (enumerated)
expressions.

[%CFEngine_function_attributes(prefix, range)%]

**Example:**

[%CFEngine_include_example(hostrange.cf, #\+begin_src\s+cfengine3\s*, .*end_src)%]

**Example Output:**

[%CFEngine_include_example(hostrange.cf, #\+begin_src\s+static_example_output\s*, .*end_src)%]

