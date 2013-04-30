---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Special-functions-0-Function-readfile-69.markdown.html
tags: [xx]
---

### Function readfile

**Synopsis**: readfile(arg1,arg2) returns type **string**

\
 *arg1* : File name, *in the range* "?(/.\*) \
 *arg2* : Maximum number of bytes to read, *in the range* 0,99999999999
\

Read max number of bytes from named file and assign to variable

**Example**:\
 \

    vars:

     "xxx"   

        string => readfile( "/home/mark/tmp/testfile" , "33" );

**Notes**:\
 \

The file (fragment) is read into a single scalar variable.
