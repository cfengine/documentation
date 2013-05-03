---
layout: default
title: Function-getfields
categories: [Special-functions,Function-getfields]
published: true
alias: Special-functions-Function-getfields.html
tags: [Special-functions,Function-getfields]
---

### Function getfields

**Synopsis**: getfields(arg1,arg2,arg3,arg4) returns type **int**

\
 *arg1* : Regular expression to match line, *in the range* .\* \
 *arg2* : Filename to read, *in the range* "?(/.\*) \
 *arg3* : Regular expression to split fields, *in the range* .\* \
 *arg4* : Return array name, *in the range* .\* \

Get an array of fields in the lines matching regex arg1 in file arg2,
split on regex arg3 as array name arg4

**Example**:\
 \

~~~~ {.verbatim}
bundle agent example

{     
vars:

  "no" int => getfields("mark:.*","/etc/passwd",":","userdata");

reports:

  cfengine_3::

    "Found $(no) lines matching";
    "Mark's homedir = $(userdata[6])";

}
~~~~

**Notes**:\
 \

This function matches lines (using a regular expression) in the named
file, and splits the *first* matched line into fields (using a second
regular expression), placing these into a named array whose elements are
`array[1],array[2],..`. This is useful for examining user data in the
Unix password or group files.

regex

A regular expression matching one or more lines. The regular expression
is anchored, meaning it must match the entire line (see [Anchored vs.
unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). \

filename

The name of the file to be examined. \

split

A regex pattern that is used to parse the field separator(s) to split up
the file into items \

array\_lval

The base name of the array that returns the values.

The function returns the number of lines matched. This function is most
useful when you want only the first matching line (e.g., to mimic the
behavior of the *getpwnam(3)* on the file /etc/passwd). If you want to
examine *all* matching lines, use [Function
readstringarray](#Function-readstringarray), instead.
