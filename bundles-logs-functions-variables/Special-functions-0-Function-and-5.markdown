---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Special-functions-0-Function-and-5.markdown.html
tags: [xx]
---

### Function and

**Synopsis**: and(...) returns type **string**

\

Calculate whether all arguments evaluate to true

**Example**:\
 \

    commands:
      "/usr/bin/generate_config $(config)"
        ifvarclass => and(not(fileexists("/etc/config/$(config)")), "generating_configs");

**Notes**:\
 \
 *History*: Was introduced in 3.2.0, Nova 2.1.0 (2011)
