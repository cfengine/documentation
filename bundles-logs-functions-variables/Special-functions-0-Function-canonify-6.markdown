---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Special-functions-0-Function-canonify-6.markdown.html
tags: [xx]
---

### Function canonify

**Synopsis**: canonify(arg1) returns type **string**

\
 *arg1* : String containing non-identifier characters, *in the range*
.\* \

Convert an arbitrary string into a legal class name

**Example**:\
 \

    commands:

       "/var/cfengine/bin/$(component)"

           ifvarclass => canonify("start_$(component)");

**Notes**:\
 \

This is for use in turning arbitrary text into class data (See Function
classify).
