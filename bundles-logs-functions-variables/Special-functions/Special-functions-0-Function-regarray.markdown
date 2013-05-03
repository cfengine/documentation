---
layout: default
title: Function-regarray
categories: [Special-functions,Function-regarray]
published: true
alias: Special-functions-Function-regarray.html
tags: [Special-functions,Function-regarray]
---

### Function regarray

**Synopsis**: regarray(arg1,arg2) returns type **class**

\
 *arg1* : Cfengine array identifier, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+ \
 *arg2* : Regular expression, *in the range* .\* \

True if arg1 matches any item in the associative array with id=arg2

**Example**:\
 \

~~~~ {.verbatim}
body common control

{
bundlesequence  => { "testbundle"  };
}

###########################################

bundle agent testbundle
{
vars:

  "myarray[0]" string => "bla1";
  "myarray[1]" string => "bla2";
  "myarray[3]" string => "bla";
  "myarray"    string => "345";  
  "not"        string => "345";  

classes:

  "ok" expression => regarray("myarray","b.*2");

reports:

 ok::

    "Found in list";

 !ok::

    "Not found in list";

}
~~~~

**Notes**:\
 \

Tests whether an associative array contains elements matching a certain
regular expression. The result is a class.

**ARGUMENTS**:

array\_name

The name of the array, with no \$() surrounding it, etc. \

regex

A regular expression to match the content. The regular expression is
anchored, meaning it must match the complete array element (See
[Anchored vs. unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)).
