---
layout: default
title: userexists
categories: [Reference, Functions, userexists]
published: true
alias: reference-functions-userexists.html
tags: [reference, functions, userexists]
---

**Prototype**: `userexists(user)`

**Return type**: `class`

**Description**: Return whether `user` name or numerical id exists on this 
host.

Checks whether the user is in the password database for the current host. The
argument must be a user name or user id.

**Arguments**:

* `user` : User name or identifier, *in the range* .\*

**Example**:

```cf3
    bundle agent example
    {     
      classes:

          "ok" expression => userexists("root");

      reports:

        ok::

          "Root exists";

        !ok::

          "Root does not exist";
    }
```

