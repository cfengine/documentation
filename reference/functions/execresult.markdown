---
layout: default
title: execresult
categories: [Reference, Functions, execresult]
published: true
alias: reference-functions-execresult.html
tags: [reference, functions, execresult]
---

**Prototype**: `execresult(command,shell)` 

**Return type**: `string`

**Description**: Execute `command` and return output as `string`.

If the command is not found, the result will be the empty string.

**Arguments**:

* `command` : Fully qualified command path, *in the range* "?(/.\*)   
* `shell` : Shell encapsulation option, *in the range* useshell,noshell

Decides whether a shell will be used to encapsulate the command. This is 
necessary in order to combine commands with pipes etc, but remember that each 
command requires a new process that reads in files beyond CFEngine's control. 
Thus using a shell is both a performance hog and a potential security issue.

**Example**:

```cf3
body common control
{
bundlesequence  => { "example" };
}

bundle agent example

{     
vars:

  "my_result" string => execresult("/bin/ls /tmp","noshell");

reports:

  linux::

    "Variable is $(my_result)";

}
```

**Notes**: you should never use this function to execute commands that make
changes to the system, or perform lengthy computations. Such an
operation is beyond CFEngine's ability to guarantee convergence, and on
multiple passes and during syntax verification these function calls are
executed, resulting in system changes that are 'covert'. Calls to
`execresult` should be for discovery and information extraction only.

**Change:** policy change in CFEngine 3.0.5. Previously newlines were
changed for spaces, now newlines are preserved.
