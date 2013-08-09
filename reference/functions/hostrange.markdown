---
layout: default
title: hostrange
categories: [Reference, Functions, hostrange]
published: true
alias: reference-functions-hostrange.html
tags: [reference, communication functions, functions, hostrange]
---

[%CFEngine_function_prototype(prefix, range)%]

**Description:** Returns whether the current host lies in the `range` of 
enumerated hostnames specified with `prefix`.

This is a pattern matching function for non-regular (enumerated)
expressions.

[%CFEngine_function_attributes(prefix, range)%]

**Example:**

```cf3
bundle agent example
{     
classes:

  "compute_nodes" expression => hostrange("cpu-","01-32");

reports:

  compute_nodes::

    "No computer is a cluster";

}
```

