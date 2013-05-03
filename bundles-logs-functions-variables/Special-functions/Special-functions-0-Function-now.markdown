---
layout: default
title: Function-now
categories: [Special-functions,Function-now]
published: true
alias: Special-functions-Function-now.html
tags: [Special-functions,Function-now]
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
