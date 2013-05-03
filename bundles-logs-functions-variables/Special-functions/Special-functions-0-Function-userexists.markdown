---
layout: default
title: Function-userexists
categories: [Special-functions,Function-userexists]
published: true
alias: Special-functions-Function-userexists.html
tags: [Special-functions,Function-userexists]
---

### Function userexists

**Synopsis**: userexists(arg1) returns type **class**

\
 *arg1* : User name or identifier, *in the range* .\* \

True if user name or numerical id exists on this host

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

  "ok" expression => userexists("root");

reports:

  ok::

    "Root exists";

 !ok::

    "Root does not exist";
}

~~~~

**Notes**:\
 \

Checks whether the user is in the password database for the current
host. The argument must be a user name or user id.
