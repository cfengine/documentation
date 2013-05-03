---
layout: default
title: Function-parseintarray
categories: [Special-functions,Function-parseintarray]
published: true
alias: Special-functions-Function-parseintarray.html
tags: [Special-functions,Function-parseintarray]
---

### Function parseintarray

**Synopsis**: parseintarray(arg1,arg2,arg3,arg4,arg5,arg6) returns type
**int**

\
 *arg1* : Array identifier to populate, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+ \
 *arg2* : A string to parse for input data, *in the range* "?(/.\*) \
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
bundle agent test(f) 
{
vars:

 #######################################
 # Define data inline for convenience
 #######################################

  "table"   string => 

"1:2
3:4
5:6";

#######################################

 "dim" int => parseintarray(
                          "items",
                  "$(table)",
                  "\s*#[^\n]*",
                  ":",
                  "1000",
                  "200000"
                  );

 "keys" slist => getindices("items");

reports:
  cfengine_3::
    "$(keys)";
}
~~~~

**Notes**:\
 \

*History*: Was introduced in version 3.1.5a1, Nova 2.1.0 (2011)

This function mirrors the exact behaviour of `readintarray()`, but reads
data from a variable instead of a file (See [Function
readintarray](#Function-readintarray)). By making data readable from a
variable, data driven policies can be kept inline. This means that they
will be visible in the CFEngine Knowledge Management portal.
