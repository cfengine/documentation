---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Special-functions-0-Function-hostrange-34.markdown.html
tags: [xx]
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

**Notes**:\
 \

This is a pattern matching function for non-regular (enumerated)
expressions.
