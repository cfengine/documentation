---
layout: default
title: Function-isnewerthan-45
categories: [Special-functions,Function-isnewerthan-45]
published: true
alias: Special-functions-Function-isnewerthan-45.html
tags: [Special-functions,Function-isnewerthan-45]
---

### Function isnewerthan

**Synopsis**: isnewerthan(arg1,arg2) returns type **class**

\
 *arg1* : Newer file name, *in the range* "?(/.\*) \
 *arg2* : Older file name, *in the range* "?(/.\*) \

True if arg1 is newer (modified later) than arg2 (mtime)

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

  "do_it" and => { isnewerthan("/tmp/later","/tmp/earlier"), "linux" }; 

reports:

  do_it::

    "The derived file needs updating";

}
~~~~

**Notes**:\
 \

This function compares the modification time of the file, referring to
changes of content only.
