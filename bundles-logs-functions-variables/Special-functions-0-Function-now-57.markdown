---
layout: default
title: Function-now-57
categories: [Special-functions,Function-now-57]
published: true
alias: Special-functions-Function-now-57.html
tags: [Special-functions,Function-now-57]
---

### Function now

**Synopsis**: now() returns type **int**

\

Convert the current time into system representation

**Example**:\
 \

~~~~ {.verbatim}
body file_select zero_age
{
mtime       => irange(ago(1,0,0,0,0,0),now);
file_result => "mtime";
}
~~~~

**Notes**:\
 \
