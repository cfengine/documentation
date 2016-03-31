---
layout: default
title: peerleader
published: true
tags: [reference, communication functions, functions, peerleader]
---

[%CFEngine_function_prototype(filename, regex, groupsize)%]

**Description:** Returns the current host's partition peer leader.

So given `groupsize` 3 and the file

```
a
b
c
# this is a comment d
e
```

The peer leader of host `b` will be host `a`.

Given a list of host names in `filename`, one per line, and excluding
comment lines starting with the [unanchored][unanchored] regular
expression `regex`, CFEngine partitions the host list into groups of
up to `groupsize`. Each group's peer leader is the first host in the
group.

The `comment` field is a multiline regular expression and will strip out
unwanted patterns from the file being read, leaving unstripped characters to be
split into fields. Using the empty string (`""`) indicates no comments.

The current host (unqualified or fully qualified) should belong to
this file if it is expected to interact with the others. The function
fails otherwise.

If the current host name (fully qualified or unqualified) is the peer
leader, the string `localhost` is used instead of the host name.

[%CFEngine_function_attributes(filename, regex, groupsize)%]

`groupsize` must be between 2 and 64 to avoid nonsensical promises.

**Example:**

Prepare:

[%CFEngine_include_snippet(peerleader.cf, #\+begin_src prep, .*end_src)%]

Run:

[%CFEngine_include_snippet(peerleader.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(peerleader.cf, #\+begin_src\s+example_output\s*, .*end_src)%]
