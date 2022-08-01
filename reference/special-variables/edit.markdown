---
layout: default
title: edit
published: true
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

### edit.empty_before_use

This variable holds the value of `empty_file_before_editing` from
`edit_defaults` bodies. It's useful for altering behavior within an `edit_line`
bundle depending if the files prior content will or won't have any effect.

**See also:**

* [empty_file_before_editing][files#empty_file_before_editing] in [edit_defaults bodies][files#edit_defaults].

**History:**

* 3.21.0, 3.18.3 added

