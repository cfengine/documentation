---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Special-functions-0-Function-diskfree-14.markdown.html
tags: [xx]
---

### Function diskfree

**Synopsis**: diskfree(arg1) returns type **int**

\
 *arg1* : File system directory, *in the range* "?(/.\*) \

Return the free space (in KB) available on the directory's current
partition (0 if not found)

**Example**:\
 \

    bundle agent example
    {     
    vars:

      "free" int => diskfree("/tmp"); 

    reports:

      cfengine_3::

        "Freedisk $(free)";

    }

**Notes**:\
 \

Values returned in kilobytes.
