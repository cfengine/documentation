---
layout: default
title: Function-countlinesmatching
categories: [Special-functions,Function-countlinesmatching]
published: true
alias: Special-functions-Function-countlinesmatching.html
tags: [Special-functions,Function-countlinesmatching]
---

### Function countlinesmatching

**Synopsis**: countlinesmatching(arg1,arg2) returns type **int**

\
 *arg1* : Regular expression, *in the range* .\* \
 *arg2* : Filename, *in the range* "?(/.\*) \

Count the number of lines matching regex arg1 in file arg2

**Example**:\
 \

~~~~ {.verbatim}
bundle agent example
{     
vars:

  "no" int => countlinesmatching("m.*","/etc/passwd");

reports:

  cfengine_3::

    "Found $(no) lines matching";

}
~~~~

**Notes**:\
 \

This function matches lines in the named file, using a regular
expression that should match the whole line.

regex

A regular expression matching zero or more lines. The regular expression
is anchored, meaning it must match a complete line (see [Anchored vs.
unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). \

filename

The name of the file to be examined.

The function returns the number of lines matched.
