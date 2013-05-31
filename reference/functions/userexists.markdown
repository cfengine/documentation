---
layout: default
title: userexists
categories: [Reference, Functions, userexists]
published: true
alias: reference-functions-userexists.html
tags: [reference, functions, userexists]
---



**Synopsis**: userexists(arg1) returns type **class**

  
 *arg1* : User name or identifier, *in the range* .\*   

True if user name or numerical id exists on this host

**Example**:  
   

```cf3

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

```

**Notes**:  
   

Checks whether the user is in the password database for the current
host. The argument must be a user name or user id.
