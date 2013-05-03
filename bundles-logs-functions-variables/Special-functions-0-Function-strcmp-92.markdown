---
layout: default
title: Function-strcmp-92
categories: [Special-functions,Function-strcmp-92]
published: true
alias: Special-functions-Function-strcmp-92.html
tags: [Special-functions,Function-strcmp-92]
---

### Function strcmp

**Synopsis**: strcmp(arg1,arg2) returns type **class**

\
 *arg1* : String, *in the range* .\* \
 *arg2* : String, *in the range* .\* \

True if the two strings match exactly

**Example**:\
 \

~~~~ {.verbatim}
body common control

{
bundlesequence  => { "example" };
}

###########################################################

bundle agent example

{     
classes:

  "same" expression => strcmp("test","test");

reports:

  same::

    "Strings are equal";

 !same::

    "Strings are not equal";
}
~~~~

**Notes**:\
 \
