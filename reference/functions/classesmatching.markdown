---
layout: default
title: classesmatching
categories: [Reference, Functions, classesmatching]
published: true
alias: reference-functions-classesmatching.html
tags: [reference, utility functions, functions, classesmatching]
---

[%CFEngine_function_prototype(name, tag1, tag2, ...)%]

**Description:** Return the list of set classes matching `name` and any tags
given. Both `name` and tags are regular expressions. `name` is required, tags
are optional.

This function searches for the given [unanchored][unanchored] `name` and
optionally `tag1`, `tag2`, ... regular expression in the list of currently set
classes. The search order is hard, soft, then local to the current bundle.

When any tags are given, only the classes with those tags matching the given
[unanchored][unanchored] regular expressions are returned. Class tags are set
using the `meta` attribute.

[%CFEngine_function_attributes(name, tag1, tag2, ...)%]

**Example:**


[%CFEngine_include_snippet(classesmatching.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(classesmatching.cf, #\+begin_src\s+example_output\s*, .*end_src)%]


**Note**: This function replaces the `allclasses.txt` static file available
in older versions of CFEngine.

**History:** Introduced in CFEngine 3.6
