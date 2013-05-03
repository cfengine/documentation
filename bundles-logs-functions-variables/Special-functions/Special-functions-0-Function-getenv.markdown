---
layout: default
title: Function-getenv
categories: [Special-functions,Function-getenv]
published: true
alias: Special-functions-Function-getenv.html
tags: [Special-functions,Function-getenv]
---

### Function getenv

**Synopsis**: getenv(arg1,arg2) returns type **string**

\
 *arg1* : Name of environment variable, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+ \
 *arg2* : Maximum number of characters to read , *in the range*
0,99999999999 \

Return the environment variable named arg1, truncated at arg2 characters

**Example**:\
 \

~~~~ {.verbatim}
bundle agent example
{
vars:

   "myvar" string => getenv("PATH","20");

classes:

  "isdefined" not => strcmp("$(myvar)","");

reports:

  isdefined::

   "The path is $(myvar)";

  !isdefined::

   "The named variable PATH does not exist";

}
~~~~

**Notes**:\
 \

Returns an empty string if the environment variable is not defined. Arg2
is used to avoid unexpectedly large return values, which could lead to
security issues. Choose a reasonable value based on the environment
variable you are querying.

**History**: This function was introduced in CFEngine version 3.0.4
(2010)
