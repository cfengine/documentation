---
layout: default
title: findfiles
published: true
tags: [reference, file functions, functions, findfiles, files, glob]
---

[%CFEngine_function_prototype(glob1, glob2, ...)%]

**Description:** Return the list of files that match any of the given glob patterns.

This function searches for the given glob patterns in the local
filesystem, returning files or directories that match.  Note that glob
patterns are not regular expressions.  They match like Unix shells:

* `*` matches any filename or directory at one level, e.g. `*.cf` will
match all files in one directory that end in `.cf` but it won't search
across directories.  `*/*.cf` on the other hand will look two levels
deep.
* `?` matches a single letter
* `[a-z]` matches any letter from `a` to `z`

This function, used together with the `bundlesmatching` function,
allows you to do dynamic inputs and a dynamic bundle call chain.

**Notes:**

- Brace expansion is not currently supported, `{x,y,anything}` will not match `x` or `y` or `anything`.

**Example:**


[%CFEngine_include_snippet(findfiles.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(findfiles.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**See also:** [`bundlesmatching()`][bundlesmatching], [`findfiles_up()`][findfiles_up].
