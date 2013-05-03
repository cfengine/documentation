---
layout: default
title: Function-and-5
categories: [Special-functions,Function-and-5]
published: true
alias: Special-functions-Function-and-5.html
tags: [Special-functions,Function-and-5]
---

### Function and

**Synopsis**: and(...) returns type **string**

\

Calculate whether all arguments evaluate to true

**Example**:\
 \

~~~~ {.verbatim}
commands:
  "/usr/bin/generate_config $(config)"
    ifvarclass => and(not(fileexists("/etc/config/$(config)")), "generating_configs");
~~~~

**Notes**:\
 \
 *History*: Was introduced in 3.2.0, Nova 2.1.0 (2011)
