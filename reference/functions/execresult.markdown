---
layout: default
title: execresult
published: true
tags: [reference, utility functions, functions, execresult]
---

[%CFEngine_function_prototype(command, shell)%]

**Description:** Execute `command` and return output as `string`.

If the command is not found, the result will be the empty string.

The `shell` argument decides whether a shell will be used to encapsulate the
command. This is necessary in order to combine commands with pipes etc, but
remember that each command requires a new process that reads in files beyond
CFEngine's control. Thus using a shell is both a performance hog and a
potential security issue.

[%CFEngine_function_attributes(command, shell)%]

**Example:**

Prepare:

[%CFEngine_include_snippet(execresult.cf, #\+begin_src prep, .*end_src)%]

Run:

[%CFEngine_include_snippet(execresult.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(execresult.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:** you should never use this function to execute commands that
make changes to the system, or perform lengthy computations. Such an
operation is beyond CFEngine's ability to guarantee convergence, and
on multiple passes and during syntax verification these function calls
are executed, resulting in system changes that are **covert**. Calls
to `execresult` should be for discovery and information extraction
only.  Effectively calls to this function will be also repeatedly
executed by `cf-promises` when it does syntax checking, which is
highly undesirable if the command is expensive.  Consider using
`commands` promises instead, which have locking and are not evaluated
by `cf-promises`.

**Limitations:** Only 8192 bytes (8K) of data can be returned from execresult.
Lines that exceed 8192 bytes are truncated.

**See also:** [`returnszero()`][returnszero].

**Change:** policy change in CFEngine 3.0.5. Previously newlines were
changed for spaces, now newlines are preserved.
