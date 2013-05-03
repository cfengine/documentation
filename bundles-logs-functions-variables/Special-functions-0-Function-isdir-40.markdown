---
layout: default
title: Function-isdir-40
categories: [Special-functions,Function-isdir-40]
published: true
alias: Special-functions-Function-isdir-40.html
tags: [Special-functions,Function-isdir-40]
---

### Function isdir

**Synopsis**: isdir(arg1) returns type **class**

\
 *arg1* : File object name, *in the range* "?(/.\*) \

True if the named object is a directory

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

  "isdir" expression => isdir("/etc");

reports:

  isdir::

    "Directory exists..";

}
~~~~

**Notes**:\
 \

The CFEngine process must have access to the object concerned in order
for this to work.
