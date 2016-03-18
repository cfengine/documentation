---
layout: default
title: maplist
published: true
tags: [reference, data functions, functions, maplist, inline_json]
---

[%CFEngine_function_prototype(pattern, list)%]

**Description:** Return a list with each element in `list` modified by a 
pattern.

This is a [collecting function][Functions#collecting functions] so it can accept many types of data parameters.

The `$(this)` variable expands to the currently processed entry from `list`. 
This is essentially like the map() function in Perl, and applies to
lists.

[%CFEngine_function_attributes(pattern, list)%]

**Example:**

[%CFEngine_include_snippet(maplist.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(maplist.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Was introduced in 3.3.0, Nova 2.2.0 (2011). The [collecting function][Functions#collecting functions] behavior was added in 3.9.

**See also:** `maplist()`, `maparray()`, [about collecting functions][Functions#collecting functions], and `data` documentation.
