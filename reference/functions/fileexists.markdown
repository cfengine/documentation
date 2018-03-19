---
layout: default
title: fileexists
published: true
tags: [reference, files functions, functions, fileexists]
---

[%CFEngine_function_prototype(filename)%]

**Description:** Returns whether the file `filename` can be accessed.

The file must exist, and the user must have access permissions to the file for
this function to return true.

**Notes:**

- `fileexists()` does **not** resolve symlinks. If a broken symlink exists, the
  file is seen to exist. For this functionality use `filestat("myfile", "link target")`
  to see if a file resolves to a the expected target, and check if the
  link target exists. Alternatively use `test` with `returnszero()`, for example
  `returnszero("/bin/test -f myfile")`.

[%CFEngine_function_attributes(filename)%]

**Example:**

[%CFEngine_include_snippet(fileexists.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(fileexists.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See Also:** `filestat()`, `isdir()`, `islink()`, `isplain()`, `returnszero()`
