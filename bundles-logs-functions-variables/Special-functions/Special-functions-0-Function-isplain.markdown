---
layout: default
title: Function-isplain
categories: [Special-functions,Function-isplain]
published: true
alias: Special-functions-Function-isplain.html
tags: [Special-functions,Function-isplain]
---

### Function isplain

**Synopsis**: isplain(arg1) returns type **class**

\
 *arg1* : File object name, *in the range* "?(/.\*) \

True if the named object is a plain/regular file

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

  "isplain" expression => isplain("/etc/passwd");

reports:

  isplain::

    "File exists..";

}
~~~~

**Notes**:\
 \
