---
layout: default
title: usemodule
categories: [Reference, Functions, usemodule]
published: true
alias: reference-functions-usemodule.html
tags: [reference, utility functions, functions, usemodule]
---

[%CFEngine_function_prototype(name, args)%]

**Description:** Execute CFEngine module script `name` with `args` and return 
whether successful.

**Arguments**:

* `name` : Name of module command, in the range `.*`

The name of the module without its leading path, since it is assumed to
be in the registered modules directory, WORKDIR/modules.

* `args` : Argument string for the module, in the range `.*`

**Example:**

```cf3
bundle agent test
{
  classes:

      # returns $(user)

      "done" expression => usemodule("getusers","");

  commands:

      "/bin/echo" args => "test $(user)";
}
```

