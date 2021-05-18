---
layout: default
title: findfiles_up
published: true
tags: [reference, file functions, functions, findfiles_up, files, glob]
---

[%CFEngine_function_prototype(path, glob, level)%]

**Description:** Return a data array of files that match a given glob pattern
by searching up the directory tree.

This function searches for files matching a given glob pattern `glob` in the
local filesystem by searching up the directory tree from a given absolute
path `path`. The function searches at moast `level` levels of directories or
until the root directory is reached. Argument `level` defaults to `inf` if
not specified. The function returnes a list of files as a data array where
the first element _(element 0)_ and the last element _(element N)_ is first
and last file or directory found respectivly.

Note that glob patterns are not regular expressions. They match like Unix
shells:

* `*` matches any filename or directory
* `?` matches a single letter
* `[a-z]` matches any letter from `a` to `z`

**Notes:**

- Brace expansion is not currently supported, `{x,y,anything}` will not match `x` or `y` or `anything`.

[%CFEngine_function_attributes(path, glob, level)%]

**Example:**

[%CFEngine_include_snippet(findfiles_up.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(findfiles_up.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**History:** Introduced in 3.18.

**See also:** [`findfiles()`][findfiles].
