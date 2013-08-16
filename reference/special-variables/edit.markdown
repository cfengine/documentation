---
layout: default
title: edit
categories: [Reference, Special Variables, edit]
published: true
alias: reference-special-variables-context-edit.html
tags: [reference, variables, edit, edit_line, files promises]
---

This context is used to access information about editing promises during 
their execution. It is context dependent and not universally meaningful or 
available.

```cf3
    bundle agent testbundle
    {
    files:

      "/tmp/testfile"
         edit_line => test;
    }

    #

    bundle edit_line test
    {
    classes:
        "ok" expression => regline(".*mark.*","$(edit.filename)");

    reports:

      ok::
       "File matched $(edit.filename)";
    }
```

### edit.filename

This variable points to the filename of the file currently making an
edit promise. If the file has been arrived at through a search, this
could be different from the files promiser.
