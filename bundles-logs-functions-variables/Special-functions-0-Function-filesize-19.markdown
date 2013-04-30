---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Special-functions-0-Function-filesize-19.markdown.html
tags: [xx]
---

### Function filesize

**Synopsis**: filesize(arg1) returns type **int**

\
 *arg1* : File object name, *in the range* "?(/.\*) \

Returns the size in bytes of the file

**Example**:\
 \

    bundle agent example
    {     
    vars:

      "exists" int => filesize("/etc/passwd");
      "nexists" int => filesize("/etc/passwdx");

    reports:

      !xyz::

        "File size $(exists)";
        "Does not exist $(nexists)";

    }

**Notes**:\
 \

*History*: Was introduced in version 3.1.3,Nova 2.0.2 (2010)

If the file object does not exist, the function call fails and the
variable does not expand.
