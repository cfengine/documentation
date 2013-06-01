---
layout: default
title: accessedbefore
categories: [Reference, Functions, accessedbefore]
published: true
alias: reference-functions-accessedbefore.html
tags: [reference, functions, accessedbefore]
---

**Prototype**: `accessedbefore(newer, older)`

**Return type**: `class`

**Description**: Compares the `atime` fields of two files.

Return true if `newer` was accessed before `older`.

**Arguments**:

* `newer` : Newer filename, *in the range* "?(/.\*)
* `older` : Older filename, *in the range* "?(/.\*)

**Example**:  


```cf3
    body common control
    {
      bundlesequence  => { "example" };
    }

    bundle agent example
    {     
      classes:

        "do_it" and => { accessedbefore("/tmp/earlier","/tmp/later"), "linux" }; 

      reports:

        do_it::

          "The secret changes have been accessed after the reference time";
    }
```

Example output:

```
    touch /tmp/reference
    touch /tmp/secretfile

    /var/cfengine/bin/cf-agent -f ./unit_accessed_before.cf -K
    R: The secret changes have been accessed after the reference time
```
