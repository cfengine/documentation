---
layout: default
title: lastnode
categories: [Reference, Functions, lastnode]
published: true
alias: reference-functions-lastnode.html
tags: [reference, data functions, functions, lastnode]
---

[%CFEngine_function_prototype(string, separator)%]

**Description:** Returns the part of `string` after the last `separator`.

This function returns the final node in a chain, given a regular
expression to split on. This is mainly useful for finding leaf-names of
files, from a fully qualified path name.

[%CFEngine_function_attributes(string, separator)%]

**Example:**

```cf3
bundle agent yes
{
vars:

  "path1" string => "/one/two/last1";
  "path2" string => "one:two:last2";

  "last1" string => lastnode("$(path1)","/");
  "last2" string => lastnode("$(path2)",":");

  "last3" string => lastnode("$(path2)","/");

reports:
  "Last = $(last1),$(last2),$(last3)";

}
```

**See also:** [`filestat()`][filestat], [`dirname()`][dirname],
[`splitstring()`][splitstring].
