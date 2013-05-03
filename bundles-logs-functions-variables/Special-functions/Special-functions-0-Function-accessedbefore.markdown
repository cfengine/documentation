---
layout: default
title: Function-accessedbefore
categories: [Special-functions,Function-accessedbefore]
published: true
alias: Special-functions-Function-accessedbefore.html
tags: [Special-functions,Function-accessedbefore]
---

### Function accessedbefore

**Synopsis**: accessedbefore(arg1,arg2) returns type **class**

\
 *arg1* : Newer filename, *in the range* "?(/.\*) \
 *arg2* : Older filename, *in the range* "?(/.\*) \

True if arg1 was accessed before arg2 (atime)

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

  "do_it" and => { accessedbefore("/tmp/earlier","/tmp/later"), "linux" }; 

reports:

  do_it::

    "The secret changes have been accessed after the reference time";

}
~~~~

**Notes**:\
 \

The function accesses the `atime` fields of a file and makes a
comparison.

~~~~ {.smallexample}
     
      touch /tmp/reference
      touch /tmp/secretfile
     
      /var/cfengine/bin/cf-agent -f ./unit_accessed_before.cf -K
      R: The secret changes have been accessed after the reference time
     
~~~~
