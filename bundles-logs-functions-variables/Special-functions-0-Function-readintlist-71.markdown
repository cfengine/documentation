---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Special-functions-0-Function-readintlist-71.markdown.html
tags: [xx]
---

### Function readintlist

**Synopsis**: readintlist(arg1,arg2,arg3,arg4,arg5) returns type
**ilist**

\
 *arg1* : File name to read, *in the range* "?(/.\*) \
 *arg2* : Regex matching comments, *in the range* .\* \
 *arg3* : Regex to split data, *in the range* .\* \
 *arg4* : Maximum number of entries to read, *in the range*
0,99999999999 \
 *arg5* : Maximum bytes to read, *in the range* 0,99999999999 \

Read and assign a list variable from a file of separated ints

**Example**:\
 \


    body common control

    {
    bundlesequence  => { "example" };
    }

    ###########################################################

    bundle agent example

    {     
    vars:

      "mylist" ilist => { readintlist("/tmp/listofint","#.*","[\n]",10,400) };

    reports:

      Yr2008::

        "List entry: $(mylist)";

    }

**ARGUMENTS**:

filename

The name of a text file containing text to be split up as a list. \

comment

A regex pattern which specifies comments to be ignored in the file. The
`comment` field will strip out unwanted patterns from the file being
read, leaving unstripped characters to be split into fields. Using the
empty string (`""`) indicates no comments. The regex is unanchored (See
Anchored vs. unanchored regular expressions). \

split

A regex pattern which is used to parse the field separator(s) to split
up the file into items. The `split` regex is also unanchored. \

maxent

The maximum number of list items to read from the file \

maxsize

The maximum number of bytes to read from the file

**Notes**:\
 \
