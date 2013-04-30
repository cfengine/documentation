---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Special-functions-0-Function-fileexists-17.markdown.html
tags: [xx]
---

### Function fileexists

**Synopsis**: fileexists(arg1) returns type **class**

\
 *arg1* : File object name, *in the range* "?(/.\*) \

True if the named file can be accessed

**Example**:\
 \

    body common control

    {
    bundlesequence  => { "example" };
    }

    ###########################################################

    bundle agent example

    {     
    classes:

      "exists" expression => fileexists("/etc/passwd");

    reports:

      exists::

        "File exists";

    }

**Notes**:\
 \

The user must have access permissions to the file for this to work
faithfully.
