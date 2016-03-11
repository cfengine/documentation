---
layout: default
title: nth
published: true
tags: [reference, data functions, functions, nth, inline_json]
---

[%CFEngine_function_prototype(list_or_container, position_or_key)%]

**Description:** Returns the element of `list_or_container` at zero-based `position_or_key`.

If an invalid position (below 0 or above the size of the list minus 1)
or missing key is requested, this function does not return a valid
value.

This is a [Collecting Functions][collecting function] so it can accept many types of data parameters.

`list_or_container` can be an slist or a data container.  If it's a
slist, the offset is simply the position in the list.  If it's a data
container, the meaning of the `position_or_key` depends on its
top-level contents: for a list like `[1,2,3,4]` you will get the list
element at `position_or_key`.  For a key-value map like
`{ a: 100, b: 200 }`, a `position_or_key` of `a` returns `100`.

[%CFEngine_function_attributes(list_or_container, position_or_key)%]

**Example:**

[%CFEngine_include_snippet(nth.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(nth.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** The [Collecting Functions][collecting function] behavior was added in 3.9.

**See also:** `length()`, [Collecting Functions][about collecting functions], and `data` documentation.
