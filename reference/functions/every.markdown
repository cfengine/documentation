---
layout: default
title: every
categories: [Reference, Functions, every]
published: true
alias: reference-functions-every.html
tags: [reference, data functions, functions, every]
---

[%CFEngine_function_prototype(regex, list)%]

**Description:** Returns whether every element in the variable `list` matches
the [unanchored][unanchored] `regex`.

**Arguments**:

* `regex` : Regular expression to find, in the range `.*`

* `list` : The name of the list variable to check, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`

**Example:**

[%CFEngine_include_snippet(every.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(every.cf, #\+begin_src\s+example_output\s*[ ,.0-9]+, .*end_src)%]

**See also:** [`filter()`][filter], [`some()`][some], and [`none()`][none].
