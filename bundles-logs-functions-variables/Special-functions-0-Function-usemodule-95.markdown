---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Special-functions-0-Function-usemodule-95.markdown.html
tags: [xx]
---

### Function usemodule

**Synopsis**: usemodule(arg1,arg2) returns type **class**

\
 *arg1* : Name of module command, *in the range* .\* \
 *arg2* : Argument string for the module, *in the range* .\* \

Execute cfengine module script and set class if successful

**Example**:\
 \

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

**Notes**:\
 \

Modules must reside in WORKDIR/modules but no longer require a special
naming convention.

**ARGUMENTS**:

Module name

The name of the module without its leading path, since it is assumed to
be in the registered modules directory. \

Argument string

Any command link arguments to pass to the module.
