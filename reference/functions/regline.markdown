---
layout: default
title: regline
published: true
tags: [reference, io functions, functions, regline]
---

[%CFEngine_function_prototype(regex, filename)%]

**Description:** Returns whether the [anchored][anchored] regular expression
`regex` matches a line in file `filename`.

Note that `regex` must match an entire line of the file in order to give a
true result.

[%CFEngine_function_attributes(regex, filename)%]

**Examples:**

This example shows a way to determine if IPV4 forwarding is enabled or not.

[%CFEngine_include_snippet(regline.cf, #\+begin_src cfengine3, .*end_src)%]

[%CFEngine_include_snippet(regline.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

For `edit_line` applications it may be useful to set a class for detecting the
presence of a string that does not exactly match one being inserted. For
example:

```cf3
bundle edit_line upgrade_cfexecd
{
  classes:

    # Check there is not already a crontab line, not identical to
    # the one proposed below...

    "exec_fix"
      not => regline(".*cf-execd.*","$(edit.filename)"),
      scope => "bundle"; # Unless you need the class outside of the bundle you
                         # should always scope it to the bundle. This can
                         # prevent issues when the bundle is used multiple
                         # times, and the classes promise is expected to be
                         # re-evaluated. If the class is namespace scoped the
                         # class will be available to other bundles and persist
                         # until it is explicitly canceled or until the end of
                         # the agent run.

  insert_lines:

    exec_fix::

     "0,5,10,15,20,25,30,35,40,45,50,55 * * * * /var/cfengine/bin/cf-execd -F";

  reports:

    exec_fix::

     "Added a 5 minute schedule to crontabs";
}
```
