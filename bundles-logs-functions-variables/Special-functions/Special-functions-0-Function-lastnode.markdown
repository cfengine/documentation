---
layout: default
title: Function-lastnode
categories: [Special-functions,Function-lastnode]
published: true
alias: Special-functions-Function-lastnode.html
tags: [Special-functions,Function-lastnode]
---

### Function lastnode

**Synopsis**: lastnode(arg1,arg2) returns type **string**

\
 *arg1* : Input string, *in the range* .\* \
 *arg2* : Link separator, e.g. /,:, *in the range* .\* \

Extract the last of a separated string, e.g. filename from a path

**Example**:\
 \

~~~~ {.verbatim}
bundle agent yes
{
vars:

  "path1" string => "/one/two/last1";
  "path2" string => "one:two:last2";

  "last1" string => lastnode("$(path1)","/");
  "last2" string => lastnode("$(path2)",":");

  "last3" string => lastnode("$(path2)","/");

reports:

  Yr2009::

    "Last = $(last1),$(last2),$(last3)";

}
~~~~

**Notes**:\
 \

This function returns the final node in a chain, given a regular
expression to split on. This is mainly useful for finding leaf-names of
files, from a fully qualified path name.
