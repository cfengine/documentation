---
layout: default
title: findprocesses
published: true
tags: [reference, process functions, functions, findprocesses, process, processes, ps]
---

[%CFEngine_function_prototype(regex)%]

**Description:** Return the list of processes that match the given regular expression `regex`.

This function searches for the given regular expression in the process
table. Use `.*sherlock.*` to find all the processes that match
`sherlock`. Use `.*\bsherlock\b.*` to exclude partial matches like
`sherlock123` (`\b` matches a word boundary).

[%CFEngine_function_attributes(regex)%]

The returned data container is a list of key-value maps. Each one is
guaranteed to have the key `pid` with the process ID. The key `line`
will also be available with the raw process table contents.

The process table is usually obtained with something like
`ps -eo user,pid,ppid,pgid,%cpu,%mem,vsize,ni,rss,stat,nlwp,stime,time,args`
but the exact data under the `line` key may change per platform and per CFEngine release.

**Example:**

```cf3
    vars:
      "holmes" data => findprocesses(".*sherlock.*");
```

Output:

```
    [ { "pid": "2378", "line": "...the ps output here" }, ... ]
```

**History:** Introduced in CFEngine 3.9

**See also:** [`processes`][processes] [`processexists()`][processexists].
