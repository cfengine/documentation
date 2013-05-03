---
layout: default
title: Function-not-56
categories: [Special-functions,Function-not-56]
published: true
alias: Special-functions-Function-not-56.html
tags: [Special-functions,Function-not-56]
---

### Function not

**Synopsis**: not(arg1) returns type **string**

\
 *arg1* : Class value, *in the range* .\* \

Calculate whether argument is false

**Example**:\
 \

~~~~ {.verbatim}
commands:
  "/usr/bin/generate_config $(config)"
    ifvarclass => not(fileexists("/etc/config/$(config)"));
~~~~

**Notes**:\
 \
 *History*: Was introduced in 3.2.0, Nova 2.1.0 (2011)
