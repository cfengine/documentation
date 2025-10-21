---
layout: default
title: processexists
aliases:
  - "/reference-functions-processexists.html"
---

{{< CFEngine_function_prototype(regex) >}}

**Description:** Return whether a process matches the given [anchored][anchored] regular expression
`regex`.

This function searches for the given regular expression in the process
table. Use `.*sherlock.*` to find all the processes that match
`sherlock`. Use `.*\bsherlock\b.*` to exclude partial matches like
`sherlock123` (`\b` matches a word boundary).

{{< CFEngine_function_attributes(regex) >}}

The process table is usually obtained with something like `ps -eo
user,pid,ppid,pgid,%cpu,%mem,vsize,ni,rss,stat,nlwp,stime,time,args`, and the
`CMD` or `COMMAND` field (`args`) is used to match against. However the exact
data used may change per platform and per CFEngine release.

**Example:**

```cf3 {skip TODO}
classes:
  # the class "holmes" will be set if a process line contains the word "sherlock"
  "holmes" expression => processexists(".*sherlock.*");
```

**History:** Introduced in CFEngine 3.9

**See also:** [`processes`][processes] [`findprocesses()`][findprocesses].
