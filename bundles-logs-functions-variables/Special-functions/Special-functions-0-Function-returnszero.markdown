---
layout: default
title: Function-returnszero
categories: [Special-functions,Function-returnszero]
published: true
alias: Special-functions-Function-returnszero.html
tags: [Special-functions,Function-returnszero]
---

### Function returnszero

**Synopsis**: returnszero(arg1,arg2) returns type **class**

\
 *arg1* : Fully qualified command path, *in the range* "?(/.\*) \
 *arg2* : Shell encapsulation option, *in the range* useshell,noshell \

True if named shell command has exit status zero

**Example**:\
 \

~~~~ {.verbatim}
body common control

{
bundlesequence  => { "example" };
}

###########################################################

bundle agent example

{     
classes:

  "my_result" expression => returnszero("/usr/local/bin/mycommand","noshell");

reports:

  !my_result::

    "Command failed";

}
~~~~

**Notes**:\
 \

This is the complement of `execresult`, but it returns a class result
rather than the output of the command.
