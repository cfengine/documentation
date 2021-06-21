---
layout: default
title: execresult_as_data
published: true
tags: [reference, utility functions, functions, execresult_as_data, cached function]
---

[%CFEngine_function_prototype(command, shell, output)%]

**Description:** Execute `command` and return a data container including command output and exit code.

Functions in the same way as [`execresult()`][execresult], and takes the same parameters.
Unlike [`execresult()`][execresult], and [`returnszero()`][returnszero], this function allows
you to test, store, or inspect both exit code and output from the same command execution.

[%CFEngine_function_attributes(command, shell, output)%]

**Example:**

Policy:

[%CFEngine_include_snippet(execresult_as_data.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(execresult_as_data.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:** you should never use this function to execute commands that
make changes to the system, or perform lengthy computations. Consider using
`commands` promises instead, which have locking and are not evaluated
by `cf-promises`.

**See also:** [`execresult()`][execresult].

**History:**

* Introduced in 3.17.0
