---
layout: default
title: Function-concat
categories: [Special-functions,Function-concat]
published: true
alias: Special-functions-Function-concat.html
tags: [Special-functions,Function-concat]
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
