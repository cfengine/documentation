---
layout: default
title: maplist
published: true
tags: [reference, data functions, functions, maplist, inline_json]
---

[%CFEngine_function_prototype(pattern, list)%]

**Description:** Return a list with each element in `list` modified by a
pattern.

[This function can accept many types of data parameters.][Functions#collecting functions]

[This function can delay the evaluation of its first parameter, which can therefore be a function call.][Functions#delayed evaluation functions]

The `$(this)` variable expands to the currently processed entry from `list`.
This is essentially like the map() function in Perl, and applies to
lists.

[%CFEngine_function_attributes(pattern, list)%]

**Example:**

[%CFEngine_include_snippet(maplist.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(maplist.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Was introduced in 3.3.0, Nova 2.2.0 (2011). The [collecting function][Functions#collecting functions] behavior was added in 3.9. The delayed evaluation behavior was introduced in 3.10.

**See also:** `maplist()`, `maparray()`, [about collecting functions][Functions#collecting functions], and `data` documentation.
