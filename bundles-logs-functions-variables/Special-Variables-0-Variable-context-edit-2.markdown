---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Special-Variables-0-Variable-context-edit-2.markdown.html
tags: [xx]
---

### Variable context `edit`

\

This context edit is used to access information about editing promises
during their execution. It is context dependent and not universally
meaningful or available. For example:

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

**\$(edit.filename)**

This variable points to the filename of the file currently making an
edit promise. If the file has been arrived at through a search, this
could be different from the files promiser.

-   Variable edit.filename

#### Variable edit.filename

\

This variable points to the filename of the file currently making an
edit promise. If the file has been arrived at through a search, this
could be different from the files promiser.
