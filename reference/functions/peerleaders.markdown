---
layout: default
title: peerleaders
categories: [Reference, Functions, peerleaders]
published: true
alias: reference-functions-peerleaders.html
tags: [reference, communication functions, functions, peerleaders]
---

[%CFEngine_function_prototype(filename, regex, groupsize)%]

**Description:** Returns a list of peer leaders from the named partitioning.

Peers are defined according to a list of hosts, provided in `filename`. This 
file should contain a list (one per line), possibly with comments matching the
[unanchored][unanchored] regular expression `regex`, of fully qualified host 
names. CFEngine breaks up this list into non-overlapping groups of up to 
`groupsize`, each of which has a leader that is the first host in the group.

The current host does not need to belong to this file.

[%CFEngine_function_attributes(filename, regex, groupsize)%]

An arbitrary limit of 64 is set for `groupsize` to avoid nonsensical 
promises.

**Example:**

Example file:

```cf3
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

```cf3
    bundle agent peers
    {
    vars:

      "mygroup" slist => peers("/tmp/hostlist","#.*",4);

      "myleader" string => peerleader("/tmp/hostlist","#.*",4);

      "all_leaders" slist => peerleaders("/tmp/hostlist","#.*",4);

    reports:

       "mypeer $(mygroup)";
       "myleader $(myleader)";
       "another leader $(all_leaders)";

    }
```
