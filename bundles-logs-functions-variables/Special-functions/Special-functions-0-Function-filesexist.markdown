---
layout: default
title: Function-filesexist
categories: [Special-functions,Function-filesexist]
published: true
alias: Special-functions-Function-filesexist.html
tags: [Special-functions,Function-filesexist]
---

### Function filesexist

**Synopsis**: filesexist(arg1) returns type **class**

\
 *arg1* : Array identifier containing list, *in the range*
@[(][a-zA-Z0-9]+[)] \

True if the named list of files can ALL be accessed

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

  "mylist" slist => { "/tmp/a", "/tmp/b", "/tmp/c" };

classes:

  "exists" expression => filesexist("@(mylist)");

reports:

  exists::

    "Files exist";

  !exists::

    "Do not exist";

}


~~~~

**Notes**:\
 \

The user must have access permissions to the file for this to work
faithfully.
