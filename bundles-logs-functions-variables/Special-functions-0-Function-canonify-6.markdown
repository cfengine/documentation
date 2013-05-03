---
layout: default
title: Function-canonify-6
categories: [Special-functions,Function-canonify-6]
published: true
alias: Special-functions-Function-canonify-6.html
tags: [Special-functions,Function-canonify-6]
---

### Function canonify

**Synopsis**: canonify(arg1) returns type **string**

\
 *arg1* : String containing non-identifier characters, *in the range*
.\* \

Convert an arbitrary string into a legal class name

**Example**:\
 \

~~~~ {.verbatim}
commands:

   "/var/cfengine/bin/$(component)"

       ifvarclass => canonify("start_$(component)");
~~~~

**Notes**:\
 \

This is for use in turning arbitrary text into class data (See [Function
classify](#Function-classify)).
