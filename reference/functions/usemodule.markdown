---
layout: default
title: Function usemodule
categories: [Reference, Functions,Function usemodule]
published: true
alias: reference-functions-usemodule.html
tags: [reference, functions, function usemodule]
---

### Function usemodule

**Synopsis**: usemodule(arg1,arg2) returns type **class**

  
 *arg1* : Name of module command, *in the range* .\*   
 *arg2* : Argument string for the module, *in the range* .\*   

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
