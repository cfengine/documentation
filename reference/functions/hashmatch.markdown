---
layout: default
title: hashmatch
categories: [Reference, Functions, hashmatch]
published: true
alias: reference-functions-hashmatch.html
tags: [reference, data functions, functions, hashmatch]
---

[%CFEngine_function_prototype(filename, algorithm, hash)%]

**Description:** Compute the hash of file `filename` using the hash `algorithm` and test if it matches `hash`.

This function may be used to determine whether a system has a particular
version of a binary file (e.g. software patch).

[%CFEngine_function_attributes(filename, algorithm, hash)%]

`hash` is an ASCII representation of the hash for comparison.

**Example:**

```cf3
bundle agent example
{     
classes:

  "matches" expression => hashmatch("/etc/passwd","md5","c5068b7c2b1707f8939b283a2758a691");

reports:

  matches::

    "File has correct version";

}
```
