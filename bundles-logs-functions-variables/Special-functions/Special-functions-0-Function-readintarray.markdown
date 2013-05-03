---
layout: default
title: Function-readintarray
categories: [Special-functions,Function-readintarray]
published: true
alias: Special-functions-Function-readintarray.html
tags: [Special-functions,Function-readintarray]
---

### Function readintarray

**Synopsis**: readintarray(arg1,arg2,arg3,arg4,arg5,arg6) returns type
**int**

\
 *arg1* : Array identifier to populate, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+ \
 *arg2* : File name to read, *in the range* "?(/.\*) \
 *arg3* : Regex matching comments, *in the range* .\* \
 *arg4* : Regex to split data, *in the range* .\* \
 *arg5* : Maximum number of entries to read, *in the range*
0,99999999999 \
 *arg6* : Maximum bytes to read, *in the range* 0,99999999999 \

Read an array of integers from a file and assign the dimension to a
variable

**Example**:\
 \

~~~~ {.verbatim}
vars:

  "dim_array" 

     int =>  readintarray("array_name","/tmp/array","#[^\n]*",":",10,4000);
~~~~

**ARGUMENTS**:

array\_name

The name to be used for the container array (the array is filled by this
routine). \

filename

The name of a text file containing the text to be split up as a list. \

comment

A regex pattern which specifies comments to be ignored in the file. The
`comment` field will strip out unwanted patterns from the file being
read, leaving unstripped characters to be split into fields. Using the
empty string (`""`) indicates no comments. The regex is unanchored (See
[Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). \

split

A regex pattern which is used to parse the field separator(s) to split
up the file into items. The `split` regex is also unanchored. \

maxent

The maximum number of list items to read from the file \

maxsize

The maximum number of bytes to read from the file

**Notes**:\
 \

Reads a two dimensional array from a file. One dimension is separated by
the character specified in the argument, the other by the the lines in
the file. The first field of the lines names the first array argument.

~~~~ {.smallexample}
     
     1: 5:7:21:13
     2:19:8:14:14
     3:45:1:78:22
     4:64:2:98:99
~~~~

Results in

~~~~ {.smallexample}
     array_name[1][0]   1
     array_name[1][1]   5
     array_name[1][2]   7
     array_name[1][3]   21
     array_name[1][4]   13
     array_name[2][0]   2
     array_name[2][1]   19
     array_name[2][2]   8
     array_name[2][3]   14
     array_name[2][4]   14
     array_name[3][0]   3
     array_name[3][1]   45
     array_name[3][2]   1
     array_name[3][3]   78
     array_name[3][4]   22
     array_name[4][0]   4
     array_name[4][1]   64
     array_name[4][2]   2
     array_name[4][3]   98
     array_name[4][4]   99
~~~~
