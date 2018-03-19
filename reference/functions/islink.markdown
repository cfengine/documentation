---
layout: default
title: islink
published: true
tags: [reference, files functions, functions, islink]
---

[%CFEngine_function_prototype(filename)%]

**Description:** Returns whether the named object `filename` is a symbolic
link.

The link node must both exist and be a symbolic link. Hard links cannot
be detected using this function.

**Notes:**

- `islink()` does **not** resolve symlinks as part of it's test. If a broken
  symlink exists, the file is still seen to be a symlink. Use
  `filestat("myfile", "link target")` to see if a file resolves to a the
  expected target, and check if the link target exists. Alternatively use `test`
  with `returnszero()`, for example `returnszero("/bin/test -f myfile")`.

[%CFEngine_function_attributes(filename)%]

**Example:**

Prepare:

[%CFEngine_include_snippet(islink.cf, #\+begin_src prep, .*end_src)%]

Run:

[%CFEngine_include_snippet(islink.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(islink.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See Also:** `fileexists()`, `filestat()`, `isdir()`, `isplain()`, `returnszero()`
