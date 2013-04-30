---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Special-functions-0-Function-not-56.markdown.html
tags: [xx]
---

### Function not

**Synopsis**: not(arg1) returns type **string**

\
 *arg1* : Class value, *in the range* .\* \

Calculate whether argument is false

**Example**:\
 \

    commands:
      "/usr/bin/generate_config $(config)"
        ifvarclass => not(fileexists("/etc/config/$(config)"));

**Notes**:\
 \
 *History*: Was introduced in 3.2.0, Nova 2.1.0 (2011)
