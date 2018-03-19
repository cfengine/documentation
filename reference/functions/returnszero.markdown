---
layout: default
title: returnszero
published: true
tags: [reference, utility functions, functions, returnszero, cached function]
---

[%CFEngine_function_prototype(command, shell)%]

**Description:** Runs `command` and returns whether it has returned with exit
status zero.

This is the complement of `execresult()`, but it returns a class result
rather than the output of the command.

[%CFEngine_function_attributes(command, shell)%]

**Example:**

[%CFEngine_include_snippet(returnszero.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(returnszero.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

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

**See also:** `execresult()`.
