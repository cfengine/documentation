---
layout: default
title: Variable-context-edit
categories: [Special-Variables,Variable-context-edit]
published: true
alias: Special-Variables-Variable-context-edit.html
tags: [Special-Variables,Variable-context-edit]
---

### Variable context `edit`

\

This context edit is used to access information about editing promises
during their execution. It is context dependent and not universally
meaningful or available. For example:

~~~~ {.verbatim}
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
~~~~

**\$(edit.filename)**

This variable points to the filename of the file currently making an
edit promise. If the file has been arrived at through a search, this
could be different from the files promiser.

-   [Variable edit.filename](#Variable-edit_002efilename)

#### Variable edit.filename

\

This variable points to the filename of the file currently making an
edit promise. If the file has been arrived at through a search, this
could be different from the files promiser.
