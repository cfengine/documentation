---
layout: default
title: Function-hostrange
categories: [Special-functions,Function-hostrange]
published: true
alias: Special-functions-Function-hostrange.html
tags: [Special-functions,Function-hostrange]
---

### Function hostrange

**Synopsis**: hostrange(arg1,arg2) returns type **class**

\
 *arg1* : Hostname prefix, *in the range* .\* \
 *arg2* : Enumerated range, *in the range* .\* \

True if the current host lies in the range of enumerated hostnames
specified

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

  "compute_nodes" expression => hostrange("cpu-","01-32");

reports:

  compute_nodes::

    "No computer is a cluster";

}
~~~~

**Notes**:\
 \

This is a pattern matching function for non-regular (enumerated)
expressions.
