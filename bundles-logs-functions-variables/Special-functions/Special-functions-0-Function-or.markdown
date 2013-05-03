---
layout: default
title: Function-or
categories: [Special-functions,Function-or]
published: true
alias: Special-functions-Function-or.html
tags: [Special-functions,Function-or]
---

### Function or

**Synopsis**: or(...) returns type **string**

\

Calculate whether any argument evaluates to true

**Example**:\
 \

~~~~ {.verbatim}
commands:
  "/usr/bin/generate_config $(config)"
    ifvarclass => or(not(fileexists("/etc/config/$(config)")), "force_configs");
~~~~

**Notes**:\
 \
 *History*: Was introduced in 3.2.0, Nova 2.1.0 (2011)
