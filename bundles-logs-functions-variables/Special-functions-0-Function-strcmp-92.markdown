---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Special-functions-0-Function-strcmp-92.markdown.html
tags: [xx]
---

### Function strcmp

**Synopsis**: strcmp(arg1,arg2) returns type **class**

\
 *arg1* : String, *in the range* .\* \
 *arg2* : String, *in the range* .\* \

True if the two strings match exactly

**Example**:\
 \

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

**Notes**:\
 \
