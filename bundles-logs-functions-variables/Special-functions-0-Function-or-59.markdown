---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Special-functions-0-Function-or-59.markdown.html
tags: [xx]
---

### Function or

**Synopsis**: or(...) returns type **string**

\

Calculate whether any argument evaluates to true

**Example**:\
 \

    commands:
      "/usr/bin/generate_config $(config)"
        ifvarclass => or(not(fileexists("/etc/config/$(config)")), "force_configs");

**Notes**:\
 \
 *History*: Was introduced in 3.2.0, Nova 2.1.0 (2011)
