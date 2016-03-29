---
layout: default
title: dirname
published: true
tags: [reference, files functions, functions, dirname]
---

[%CFEngine_function_prototype(path)%]

**Description:** Return the parent directory name for given `path`.

This function returns the directory name for `path`. If `path` is a
directory, then the name of its parent directory is returned.

[%CFEngine_function_attributes(path)%]

**Example:**

[%CFEngine_include_snippet(dirname.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(dirname.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**

**History:** Was introduced in 3.3.0, Nova 2.2.0 (2011)

**See also:** [`lastnode()`][lastnode], [`filestat()`][filestat],
[`splitstring()`][splitstring].
