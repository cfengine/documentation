---
layout: default
title: findfiles_up
---

{{< CFEngine_function_prototype(path, glob, level) >}}

**Description:** Return a data array of files that match a given glob pattern
by searching up the directory tree.

This function searches for files matching a given glob pattern `glob` in the
local filesystem by searching up the directory tree from a given absolute
path `path`. The function searches at most `level` levels of directories or
until the root directory is reached. Argument `level` defaults to `inf` if
not specified. The function returns a list of files as a data array where
the first element _(element 0)_ and the last element _(element N)_ is first
and last file or directory found respectively.

Note that glob patterns are not regular expressions. They match like Unix
shells:

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

{{< CFEngine_function_attributes(path, glob, level) >}}

**Example:**

{{< CFEngine_include_snippet(findfiles_up.cf, #\+begin_src cfengine3, .*end_src) >}}

Output:

{{< CFEngine_include_snippet(findfiles_up.cf, #\+begin_src\s+example_output\s*, .*end_src) >}}

**History:**

- Introduced in 3.18.
- Brace expression (i.e., `{foo,bar}`) and negative bracket expressions (i.e., `[!abc]`) were introduced in 3.24.

**See also:** `findfiles()`.
