---
layout: default
title: isdir
published: true
tags: [reference, files functions, functions, isdir]
---

[%CFEngine_function_prototype(filename)%]

**Description:** Returns whether the named object `filename` is a directory.

The CFEngine process must have access to `filename` in order for this to work.

[%CFEngine_function_attributes(filename)%]

**Example:**

[%CFEngine_include_snippet(isdir.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(isdir.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** `fileexists()`, `filestat()`, `islink()`, `isplain()`, `returnszero()`
