---
layout: default
title: peerleader
categories: [Reference, Functions, peerleader]
published: true
alias: reference-functions-peerleader.html
tags: [reference, communication functions, functions, peerleader]
---

[%CFEngine_function_prototype(filename, regex, groupsize)%]

**Description:** Returns the assigned peer-leader of the partition to which the current host belongs.

This function returns the name of a host that may be considered the
leader of a group of peers of the current host. Peers are defined
according to a list of hosts, provided as a file in `filename`.
This file should contain a list (one per line), possibly with comments 
matching the [unanchored][unanchored] regular expression `regex`, of fully 
qualified host names. CFEngine breaks this list up into non-overlapping groups 
of up to `groupsize`, each of which has a leader that is the first host in the 
group.

The current host should belong to this file if it is expected to interact with 
the others. The function returns nothing if the host does not belong to the 
list.

[%CFEngine_function_attributes(filename, regex, groupsize)%]

An arbitrary limit of 64 is set for `groupsize` to avoid nonsensical 
promises.

**Example:**

Example file:

     one
     two
     three # this is a comment
     four
     five
     six
     seven
     eight
     nine
     ten
     eleven
     twelve
     etc
```

[%CFEngine_include_snippet(peerleader.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(peerleader.cf, #\+begin_src\s+example_output\s*[ ,.0-9]+, .*end_src)%]
