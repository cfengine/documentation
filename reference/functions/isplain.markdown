---
layout: default
title: isplain
published: true
tags: [reference, files functions, functions, isplain]
---

[%CFEngine_function_prototype(filename)%]

**Description:** Returns whether the named object `filename` is a
plain/regular file.

[%CFEngine_function_attributes(filename)%]

**Example:**

[%CFEngine_include_snippet(isplain.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(isplain.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** `fileexists()`, `filestat()`, `isdir()`, `islink()`, `returnszero()`
