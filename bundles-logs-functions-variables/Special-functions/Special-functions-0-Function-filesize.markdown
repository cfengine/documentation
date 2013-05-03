---
layout: default
title: Function-filesize
categories: [Special-functions,Function-filesize]
published: true
alias: Special-functions-Function-filesize.html
tags: [Special-functions,Function-filesize]
---

### Function filesize

**Synopsis**: filesize(arg1) returns type **int**

\
 *arg1* : File object name, *in the range* "?(/.\*) \

Returns the size in bytes of the file

**Example**:\
 \

~~~~ {.verbatim}
bundle agent example
{     
vars:

  "exists" int => filesize("/etc/passwd");
  "nexists" int => filesize("/etc/passwdx");

reports:

  !xyz::

    "File size $(exists)";
    "Does not exist $(nexists)";

}
~~~~

**Notes**:\
 \

*History*: Was introduced in version 3.1.3,Nova 2.0.2 (2010)

If the file object does not exist, the function call fails and the
variable does not expand.
