---
layout: default
title: hostrange
published: true
tags: [reference, communication functions, functions, hostrange]
---

[%CFEngine_function_prototype(prefix, range)%]

**Description:** Returns whether the unqualified name of the current host lies
in the `range` of enumerated hostnames specified with `prefix`.

This is a pattern matching function for non-regular (enumerated)
expressions. The `range` specification is in the format `A-B` (using a minus
character `-`) where `A` and `B` are decimal integers, optionally prefixed with
zeroes (e.g. `01`). The unqualified name of the current host used in this
function is the same as the contents of the [`sys.uqhost`][sys.uqhost]
variable. The function is using integer comparison on `range` and the last
numeric part of the unqualified host name and string comparison of `prefix`
(lowercase) with the part of the unqualified host name until the last numeric
part.

[%CFEngine_function_attributes(prefix, range)%]

**Example:**

[%CFEngine_include_example(hostrange.cf, #\+begin_src\s+cfengine3\s*, .*end_src)%]

**Example Output:**

[%CFEngine_include_example(hostrange.cf, #\+begin_src\s+static_example_output\s*, .*end_src)%]

