---
layout: default
title: hashmatch
categories: [Reference, Functions, hashmatch]
published: true
alias: reference-functions-hashmatch.html
tags: [reference, functions, hashmatch]
---

**Prototype**: `hashmatch(filename, algorthm, hash)`

**Return type**: `class`

**Description:** Compute the hash of file `filename` using the hash `algorithm` and test if it matches `hash`.

This function may be used to determine whether a system has a particular
version of a binary file (e.g. software patch).

**ARGUMENTS**:

* `filename` : Filename to hash, in the range `"?(/.*)`
* `algorithm` : Hash or digest algorithm, one of
    * md5
    * sha1
    * sha256
    * sha512
    * sha384
    * crypt   
* `hash` : ASCII representation of hash for comparison, in the range
`[a-zA-Z0-9_$(){}\[\].:]+`

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
