---
layout: default
title: lastnode
aliases:
  - "/reference-functions-lastnode.html"
---

{{< CFEngine_function_prototype(string, separator) >}}

**Description:** Returns the part of `string` after the last `separator`.

This function returns the final node in a chain, given a regular
expression to split on. This is mainly useful for finding leaf-names of
files, from a fully qualified path name.

{{< CFEngine_function_attributes(string, separator) >}}

**Example:**

{{< CFEngine_include_snippet(lastnode.cf, #\+begin_src cfengine3, .*end_src) >}}

Output:

{{< CFEngine_include_snippet(lastnode.cf, #\+begin_src\s+example_output\s*, .*end_src) >}}

**See also:** [`filestat()`][filestat], [`dirname()`][dirname],
[`splitstring()`][splitstring].
