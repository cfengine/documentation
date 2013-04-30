---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Special-functions-0-Function-maplist-55.markdown.html
tags: [xx]
---

### Function maplist

**Synopsis**: maplist(arg1,arg2) returns type **slist**

\
 *arg1* : Pattern based on \$(this) as original text, *in the range* .\*
\
 *arg2* : The name of the list variable to map, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+ \

Return a list with each element modified by a pattern based \$(this)

**Example**:\
 \

    bundle agent test
    {
    vars:

      "oldlist" slist => { "a", "b", "c" };
      "newlist" slist => maplist("Element ($(this))","oldlist");

    reports:
     linux::
      "Transform: $(newlist)";
    }

**Notes**:\
 \

*History*: Was introduced in 3.3.0, Nova 2.2.0 (2011)

This is essentially like the map() function in Perl, and applies to
lists.
