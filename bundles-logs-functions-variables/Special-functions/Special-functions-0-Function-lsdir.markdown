---
layout: default
title: Function-lsdir
categories: [Special-functions,Function-lsdir]
published: true
alias: Special-functions-Function-lsdir.html
tags: [Special-functions,Function-lsdir]
---

### Function lsdir

**Synopsis**: lsdir(arg1,arg2,arg3) returns type **slist**

\
 *arg1* : Path to base directory, *in the range* .+ \
 *arg2* : Regular expression to match files or blank, *in the range* .\*
\
 *arg3* : Include the base path in the list, *in the range*
true,false,yes,no,on,off \

Return a list of files in a directory matching a regular expression

**Example**:\
 \

~~~~ {.verbatim}
vars:
  "listfiles" slist => lsdir("/etc", "(passwd|shadow).*", "true");
~~~~

**Notes**:\
 \
 *History*: Was introduced in 3.3.0, Nova 2.2.0 (2011)

This function returns list of files in directory specified in arg1,
matched with regular expression in arg2. In case arg3 is true, full
paths are returned, otherwise only names relative to the the directory
are returned.
