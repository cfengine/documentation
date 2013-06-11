---
layout: default
title: returnszero
categories: [Reference, Functions, returnszero]
published: true
alias: reference-functions-returnszero.html
tags: [reference, utility functions, functions, returnszero]
---

**Prototype:** `returnszero(command, shell)`

**Return type:** `class`

**Description:** Runs `command` and returns whether it has returned with exit 
status zero.

This is the complement of `execresult()`, but it returns a class result
rather than the output of the command.

**Arguments**:

* `command` : Fully qualified command path, in the range `"?(/.*)`
* `shelll` : Shell encapsulation option, in the range `useshell`,`noshell`

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
