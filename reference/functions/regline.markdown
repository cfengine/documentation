---
layout: default
title: regline
categories: [Reference, Functions, regline]
published: true
alias: reference-functions-regline.html
tags: [reference, functions, regline]
---

**Prototype**: `regline(regex, filename)`

**Return type**: `class`

**Description**: Returns whether the regular expression `regex` matches a line 
in file `filename`.

Note that `regex` must match an entire line of the file in order to give a true result.

**Arguments**:

* `regex` : Regular expression, *in the range* .\*
* `filename` : Filename to search, *in the range* .\*

**Example**:

```cf3
    bundle agent example
    {
    files:

      "/tmp/testfile" edit_line => test;
    }

    bundle edit_line test
    {
    classes:

        "ok" expression => regline(".*XYZ.*","$(edit.filename)");

    reports:

     ok::

       "File $(edit.filename) has a line with \"XYZ\" in it";

    }
```

This function is useful for `edit_line` applications, where one might want to set a class for detecting the presence of a string that does not exactly match one being inserted. For example:

```cf3
    bundle edit_line upgrade_cfexecd
      {
      classes:

        # Check there is not already a crontab line, not identical to
        # the one proposed below...

        "exec_fix" not => regline(".*cf-execd.*","$(edit.filename)");

      insert_lines:

        exec_fix::

         "0,5,10,15,20,25,30,35,40,45,50,55 * * * * /var/cfengine/bin/cf-execd -F";

      reports:

        exec_fix::

         "Added a 5 minute schedule to crontabs";
      }
```
