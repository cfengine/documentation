---
layout: default
title: usemodule
categories: [Reference, Functions, usemodule]
published: true
alias: reference-functions-usemodule.html
tags: [reference, functions, usemodule]
---

**Prototype**: `usemodule(name, args)`

**Return type**: `class`

  
 *name* : Name of module command, *in the range* .\*
 *args* : Argument string for the module, *in the range* .\*

Execute cfengine module script and set class if successful

**Example**:  
   

```cf3
body common control
{
  any::
    bundlesequence  => {
                         test
                       };
}

###################################################################

bundle agent test
{
  classes:

      # returns $(user)

      "done" expression => usemodule("getusers","");

  commands:

      "/bin/echo" args => "test $(user)";
}
```

**Notes**:  
   

Modules must reside in WORKDIR/modules but no longer require a special
naming convention.

**ARGUMENTS**:

Module name

The name of the module without its leading path, since it is assumed to
be in the registered modules directory.   

Argument string

Any command link arguments to pass to the module.
