---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Special-functions-0-Function-isdir-40.markdown.html
tags: [xx]
---

### Function isdir

**Synopsis**: isdir(arg1) returns type **class**

\
 *arg1* : File object name, *in the range* "?(/.\*) \

True if the named object is a directory

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

      "isdir" expression => isdir("/etc");

    reports:

      isdir::

        "Directory exists..";

    }

**Notes**:\
 \

The CFEngine process must have access to the object concerned in order
for this to work.
