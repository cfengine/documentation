---
layout: default
title: Function-getindices
categories: [Special-functions,Function-getindices]
published: true
alias: Special-functions-Function-getindices.html
tags: [Special-functions,Function-getindices]
---

### Function getindices

**Synopsis**: getindices(arg1) returns type **slist**

\
 *arg1* : Cfengine array identifier, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+ \

Get a list of keys to the array whose id is the argument and assign to
variable

**Example**:\
 \

~~~~ {.verbatim}
body common control

{
any::

  bundlesequence  => { "testsetvar" };   
}


#######################################################

bundle agent testsetvar

{
vars:

  "v[index_1]" string => "value_1";
  "v[index_2]" string => "value_2";

  "parameter_name" slist => getindices("v");

reports:

  Yr2008::

   "Found index: $(parameter_name)";

}
~~~~

**Notes**:\
 \

Make sure you specify the correct scope when supplying the name of the
variable.
