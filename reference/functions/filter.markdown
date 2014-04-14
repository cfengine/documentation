---
layout: default
title: filter
published: true
tags: [reference, data functions, functions, filter]
---

[%CFEngine_function_prototype(filter, list, is_regex, invert, max_return)%]

**Description:** Transforms a list or data container into a list subset thereof.

This is a generic filtering function that returns a list of up to `max_return` 
elements in `list` that match the filtering rules specified in `filter`, 
`is_regex` and `invert`.

**Arguments**:

* filter : [Anchored][anchored] regular expression or static string to find, in the range `.*`
* list : The name of the list variable or data container to check, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`
* is_regex_ : Boolean

Treat `filter` as a regular expression or as a static string.

* `invert` : Boolean

Invert filter.

* `max_return` : Maximum number of elements to return in the range `0,999999999`

**Example:**  


[%CFEngine_include_snippet(filter.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(filter.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** [`grep()`][grep], [`every()`][every], [`some()`][some], and 
[`none()`][none].
