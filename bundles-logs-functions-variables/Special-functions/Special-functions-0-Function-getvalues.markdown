---
layout: default
title: Function-getvalues
categories: [Special-functions,Function-getvalues]
published: true
alias: Special-functions-Function-getvalues.html
tags: [Special-functions,Function-getvalues]
---

### Function getvalues

**Synopsis**: getvalues(arg1) returns type **slist**

\
 *arg1* : Cfengine array identifier, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+ \

Get a list of values corresponding to the right hand sides in an array
whose id is the argument and assign to variable

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

  "parameter_name" slist => getvalues("v");

reports:

  Yr2008::

   "Found index: $(parameter_name)";

}
~~~~

**Notes**:\
 \

Make sure you specify the correct scope when supplying the name of the
variable. If the array contains list elements on the right hand side,
then all of the list elements are flattened into a single list to make
the return value a list.
