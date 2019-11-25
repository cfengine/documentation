---
layout: default
title: nth
published: true
tags: [reference, data functions, functions, nth, inline_json]
---

[%CFEngine_function_prototype(list_or_container, position_or_key)%]

**Description:** Returns the element of `list_or_container` at zero-based `position_or_key`.

If an invalid position (above the size of the list minus 1) or missing key is
requested, this function does not return a valid value.

[This function can accept many types of data parameters.][Functions#collecting functions]

`list_or_container` can be an slist or a data container.  If it's a
slist, the offset is simply the position in the list.  If it's a data
container, the meaning of the `position_or_key` depends on its
top-level contents: for a list like `[1,2,3,4]` you will get the list
element at `position_or_key`.  For a key-value map like
`{ a: 100, b: 200 }`, a `position_or_key` of `a` returns `100`.

Since 3.15, Nth supports negative indices when indexing lists, starting from
the other end of the list. With a `position_or_key` of `-1`, you will get `4`
from the list `[1,2,3,4]`.

[%CFEngine_function_attributes(list_or_container, position_or_key)%]

**Example:**

[%CFEngine_include_snippet(nth.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(nth.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:**  
The [collecting function][Functions#collecting functions] behavior was added in 3.9.  
The ability to use negative indices was added in 3.15.

**See also:** `length()`, [about collecting functions][Functions#collecting functions], and `data` documentation.
