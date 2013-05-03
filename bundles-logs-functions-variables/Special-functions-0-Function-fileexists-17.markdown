---
layout: default
title: Function-fileexists-17
categories: [Special-functions,Function-fileexists-17]
published: true
alias: Special-functions-Function-fileexists-17.html
tags: [Special-functions,Function-fileexists-17]
---

### Function fileexists

**Synopsis**: fileexists(arg1) returns type **class**

\
 *arg1* : File object name, *in the range* "?(/.\*) \

True if the named file can be accessed

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

  "exists" expression => fileexists("/etc/passwd");

reports:

  exists::

    "File exists";

}
~~~~

**Notes**:\
 \

The user must have access permissions to the file for this to work
faithfully.
