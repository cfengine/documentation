---
layout: default
title: peerleaders
published: true
tags: [reference, communication functions, functions, peerleaders]
---

[%CFEngine_function_prototype(filename, regex, groupsize)%]

**Description:** Returns a list of partition peer leaders from a file of host names.

Given a list of host names in `filename`, one per line, and excluding
comment lines starting with the [unanchored][unanchored] regular
expression `regex`, CFEngine partitions the host list into groups of
up to `groupsize`. Each group's peer leader is the first host in the
group.

So given `groupsize` 2 and the file

```
a
b
c
# this is a comment d
e
```

The peer leaders will be `a` and `c`.

The current host name does not need to belong to this file.  If it's
found (fully qualified or unqualified), the string `localhost` is used
instead of the host name.

The `comment` field is a multiline regular expression and will strip out
unwanted patterns from the file being read, leaving unstripped characters to be
split into fields. Using the empty string (`""`) indicates no comments.

[%CFEngine_function_attributes(filename, regex, groupsize)%]

`groupsize` must be between 2 and 64 to avoid nonsensical promises.

**Example:**

Prepare:

[%CFEngine_include_snippet(peerleaders.cf, #\+begin_src prep, .*end_src)%]

Run:

[%CFEngine_include_snippet(peerleaders.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(peerleaders.cf, #\+begin_src\s+example_output\s*, .*end_src)%]
