---
layout: default
title: Function-readstringarrayidx
categories: [Special-functions,Function-readstringarrayidx]
published: true
alias: Special-functions-Function-readstringarrayidx.html
tags: [Special-functions,Function-readstringarrayidx]
---

### Function readstringarrayidx

**Synopsis**: readstringarrayidx(arg1,arg2,arg3,arg4,arg5,arg6) returns
type **int**

\
 *arg1* : Array identifier to populate, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+ \
 *arg2* : A string to parse for input data, *in the range* "?(/.\*) \
 *arg3* : Regex matching comments, *in the range* .\* \
 *arg4* : Regex to split data, *in the range* .\* \
 *arg5* : Maximum number of entries to read, *in the range*
0,99999999999 \
 *arg6* : Maximum bytes to read, *in the range* 0,99999999999 \

Read an array of strings from a file and assign the dimension to a
variable with integer indeces

**Example**:\
 \

~~~~ {.verbatim}
vars:

  "dim_array" 

     int =>  readstringarrayidx("array_name","/tmp/array","\s*#[^\n]*",":",10,4000);
~~~~

Returns an integer number of keys in the array (i.e., the number of
lines matched). If you only want the fields in the first matching line
(e.g., to mimic the behavior of the *getpwnam(3)* on the file
/etc/passwd), see [Function getfields](#Function-getfields), instead.

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
empty string (`""`) indicates no commments. The regex is unanchored (See
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
the file. The array arguments are both integer indexes, allowing for
non-identifiers at first field (e.g. duplicates or names with spaces),
unlike `readstringarray`.

~~~~ {.smallexample}
     
     at spaced:x:25:25:Batch jobs daemon:/var/spool/atjobs:/bin/bash
     duplicate:x:103:105:User for Avahi:/var/run/avahi-daemon:/bin/false    # Disallow login
     beagleindex:x:104:106:User for Beagle indexing:/var/cache/beagle:/bin/bash
     duplicate:x:1:1:bin:/bin:/bin/bash
     # Daemon has the default shell
     daemon:x:2:2:Daemon:/sbin:
     
~~~~

Results in a systematically indexed map of the file. Some samples are
show below to illustrate the pattern.

~~~~ {.smallexample}
     array_name[0][0]       at spaced
     array_name[0][1]       x
     array_name[0][2]       25
     array_name[0][3]       25
     array_name[0][4]       Batch jobs daemon
     array_name[0][5]       /var/spool/atjobs
     array_name[0][6]       /bin/bash
     array_name[1][0]       duplicate
     array_name[1][1]       x
     array_name[1][2]       103
     array_name[1][3]       105
     array_name[1][4]       User for Avahi
     array_name[1][5]       /var/run/avahi-daemon
     array_name[1][6]       /bin/false
     ...
     
~~~~
