---
layout: default
title: Function-readrealarray
categories: [Special-functions,Function-readrealarray]
published: true
alias: Special-functions-Function-readrealarray.html
tags: [Special-functions,Function-readrealarray]
---

### Function readrealarray

**Synopsis**: readrealarray(arg1,arg2,arg3,arg4,arg5,arg6) returns type
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

Read an array of real numbers from a file and assign the dimension to a
variable

**Example**:\
 \

~~~~ {.verbatim}
vars:

  "dim_array" 

     int =>  readrealarray("array_name","/tmp/array","#[^\n]*",":",10,4000);
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

For detailed notes, See [Function readintarray](#Function-readintarray).
