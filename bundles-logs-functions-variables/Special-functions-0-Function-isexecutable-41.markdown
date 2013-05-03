---
layout: default
title: Function-isexecutable-41
categories: [Special-functions,Function-isexecutable-41]
published: true
alias: Special-functions-Function-isexecutable-41.html
tags: [Special-functions,Function-isexecutable-41]
---

### Function isexecutable

**Synopsis**: isexecutable(arg1) returns type **class**

\
 *arg1* : File object name, *in the range* "?(/.\*) \

True if the named object has execution rights for the current user

**Example**:\
 \

~~~~ {.verbatim}
classes:

  "yes" expression => isexecutable("/bin/ls");
~~~~

**Notes**:\
 \

*History*: Was introduced in version 3.1.0b1,Nova 2.0.0b1 (2010)
