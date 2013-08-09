---
layout: default
title: userexists
categories: [Reference, Functions, userexists]
published: true
alias: reference-functions-userexists.html
tags: [reference, system functions, functions, userexists]
---

[%CFEngine_function_prototype(user)%]

**Description:** Return whether `user` name or numerical id exists on this 
host.

Checks whether the user is in the password database for the current host. The
argument must be a user name or user id.

[%CFEngine_function_attributes(user)%]

**Example:**

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

