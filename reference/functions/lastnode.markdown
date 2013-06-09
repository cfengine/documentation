---
layout: default
title: lastnode
categories: [Reference, Functions, lastnode]
published: true
alias: reference-functions-lastnode.html
tags: [reference, functions, lastnode]
---

**Prototype**: `lastnode(string, separator)`

**Return type**: `string`

**Description**: Returns the part of `string` after the last `separator`.

This function returns the final node in a chain, given a regular
expression to split on. This is mainly useful for finding leaf-names of
files, from a fully qualified path name.

**Arguments**:

* `string` : Input string, in the range `.*`
* `separator` : Link separator, e.g. `/` or `:`, in the range `.*`

**Example**:

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

  Yr2009::

    "Last = $(last1),$(last2),$(last3)";

}
```

**Notes**:

See also: `filestat`, dirname`, `splitstring`.
