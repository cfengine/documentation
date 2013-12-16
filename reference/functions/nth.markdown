---
layout: default
title: nth
categories: [Reference, Functions, nth]
published: true
alias: reference-functions-nth.html
tags: [reference, data functions, functions, nth]
---

[%CFEngine_function_prototype(list, position)%]

**Description:** Returns the element of `list` at zero-based `position`.

If an invalid position (below 0 or above the size of the list minus 1)
is requested, this function does not return a valid value.

`list` can be an slist or a data container.  If it's a slist, the
offset is simply the position in the list.  If it's a data container,
the meaning of the `position` depends on its top-level contents: for
a list like `[1,2,3,4]` you will get the list element at `position`.
For a key-value map like `{ a: 100, b: 200 }` you get the value at
`position`, using the canonical JSON-style ordering of the keys.

[%CFEngine_function_attributes(list, position)%]

**Example:**

[%CFEngine_include_snippet(nth.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(nth.cf, #\+begin_src\s+example_output\s*[ ,.0-9]+, .*end_src)%]

**See also:** [`length()`][length].
