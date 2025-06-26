---
layout: default
title: findfiles
---

[%CFEngine_function_prototype(glob1, glob2, ...)%]

**Description:** Return the list of files that match any of the given glob patterns.

This function searches for the given glob patterns in the local
filesystem, returning files or directories that match. Note that glob
patterns are not regular expressions. They match like Unix shells:

* `*` matches any filename or directory at one level, e.g. `*.cf` will
match all files in one directory that end in `.cf` but it won't search
across directories. `*/*.cf` on the other hand will look two levels
deep.
* `**` recursively matches up to six subdirectories.
* `?` matches a single letter.
* `[abc]` matches `a`, `b` or `c`.
* `[!abc]` matches any letters other than `a`, `b` or `c`.
* `[a-z]` matches any letter from `a` to `z`.
* `[!a-z]` matches any letter not from `a` to `z`.
* `{foo,bar}` matches `foo` or `bar`.

This function, used together with the `bundlesmatching` function,
allows you to do dynamic inputs and a dynamic bundle call chain.

**Example:**

[%CFEngine_include_snippet(findfiles.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(findfiles.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:**

- Brace expression (i.e., `{foo,bar}`) and negative bracket expressions (i.e., `[!abc]`) were introduced in 3.24.

**See also:** `bundlesmatching()`, `findfiles_up()`.
