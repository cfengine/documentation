---
layout: default
title: Function-isvariable-47
categories: [Special-functions,Function-isvariable-47]
published: true
alias: Special-functions-Function-isvariable-47.html
tags: [Special-functions,Function-isvariable-47]
---

### Function isvariable

**Synopsis**: isvariable(arg1) returns type **class**

\
 *arg1* : Variable identifier, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+ \

True if the named variable is defined

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
vars:

  "bla" string => "xyz..";

classes:

  "exists" expression => isvariable("bla");

reports:

  exists::

    "Variable exists: \"$(bla)\"..";

}
~~~~

**Notes**:\
 \

The variable need only exist. This says nothing about its value. Use
`regcmp` to check variable values.
