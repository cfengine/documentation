---
layout: default
title: some
published: true
tags: [reference, data functions, functions, some]
---

[%CFEngine_function_prototype(regex, list)%]

**Description:** Return whether any element of `list` matches the
[Unanchored][unanchored] regular expression `regex`.

`list` can be a data container or a regular list.

[%CFEngine_function_attributes(regex, list)%]

`some()` will return as soon as any element matches.

It's convenient to set a class to `not => some(".*", mylist)` in order
to check if `mylist` is empty. Since `some()` returns as soon as
possible, that is better than using `length()` or `every()` or
`none()` which all must traverse the entire list.

**Example:**

[%CFEngine_include_snippet(some.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(some.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** [`filter()`][filter], [`every()`][every], and [`none()`][none].
