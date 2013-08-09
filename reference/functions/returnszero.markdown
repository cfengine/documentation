---
layout: default
title: returnszero
categories: [Reference, Functions, returnszero]
published: true
alias: reference-functions-returnszero.html
tags: [reference, utility functions, functions, returnszero]
---

[%CFEngine_function_prototype(command, shell)%]

**Description:** Runs `command` and returns whether it has returned with exit 
status zero.

This is the complement of `execresult()`, but it returns a class result
rather than the output of the command.

[%CFEngine_function_attributes(command, shell)%]

**Example:**

```cf3
bundle agent example
{     
classes:

  "my_result" expression => returnszero("/usr/local/bin/mycommand","noshell");

reports:

  !my_result::

    "Command failed";

}
```

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

**See also:** [`execresult()`][execresult].
