---
layout: default
title: Function-splitstring
categories: [Special-functions,Function-splitstring]
published: true
alias: Special-functions-Function-splitstring.html
tags: [Special-functions,Function-splitstring]
---

### Function splitstring

**Synopsis**: splitstring(arg1,arg2,arg3) returns type **slist**

\
 *arg1* : A data string, *in the range* .\* \
 *arg2* : Regex to split on, *in the range* .\* \
 *arg3* : Maximum number of pieces, *in the range* 0,99999999999 \

Convert a string in arg1 into a list of max arg3 strings by splitting on
a regular expression in arg2

**Example**:\
 \

~~~~ {.verbatim}
bundle agent test

{
vars:

  "split1" slist => splitstring("one:two:three",":","10");
  "split2" slist => splitstring("one:two:three",":","1");
  "split3" slist => splitstring("alpha:xyz:beta","xyz","10");

reports:

 linux::

  "split1: $(split1)";  # will list "one", "two", and "three"
  "split2: $(split2)";  # will list "one" and "two:three"
  "split3: $(split3)";  # will list "alpha:" and ":beta"

}
~~~~

**Notes**:\
 \

Returns a list of strings from a string.

**ARGUMENTS**:

string

The string to be split. \

regex

A regex pattern which is used to parse the field separator(s) to split
up the file into items. The regex is unanchored (See [Anchored vs.
unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). \

maxent

The maximum number of splits to perform.

If the maximum number of splits is insufficient to accommodate all
entries, the final entry in the slist that is generated will contain the
rest of the unsplit string.
