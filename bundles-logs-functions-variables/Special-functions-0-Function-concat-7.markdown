---
layout: default
title: Function-concat-7
categories: [Special-functions,Function-concat-7]
published: true
alias: Special-functions-Function-concat-7.html
tags: [Special-functions,Function-concat-7]
---

### Function concat

**Synopsis**: concat(...) returns type **string**

\

Concatenate all arguments into string

**Example**:\
 \

~~~~ {.verbatim}
commands:
  "/usr/bin/generate_config $(config)"
    ifvarclass => concat("have_config_", canonify("$(config)"));
~~~~

**Notes**:\
 \
 *History*: Was introduced in 3.2.0, Nova 2.1.0 (2011)
