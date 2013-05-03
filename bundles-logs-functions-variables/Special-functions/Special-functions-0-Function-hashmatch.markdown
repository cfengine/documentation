---
layout: default
title: Function-hashmatch
categories: [Special-functions,Function-hashmatch]
published: true
alias: Special-functions-Function-hashmatch.html
tags: [Special-functions,Function-hashmatch]
---

### Function hashmatch

**Synopsis**: hashmatch(arg1,arg2,arg3) returns type **class**

\
 *arg1* : Filename to hash, *in the range* "?(/.\*) \
 *arg2* : Hash or digest algorithm, *in the range*
md5,sha1,crypt,cf\_sha224,cf\_sha256,cf\_sha384,cf\_sha512 \
 *arg3* : ASCII representation of hash for comparison, *in the range*
[a-zA-Z0-9\_\$(){}\\[\\].:]+ \

Compute the hash of arg1, of type arg2 and test if it matches the value
in arg3

**Example**:\
 \

~~~~ {.verbatim}
bundle agent example

{     
classes:

  "matches" expression => hashmatch("/etc/passwd","md5","c5068b7c2b1707f8939b283a2758a691");

reports:

  matches::

    "File has correct version";

}
~~~~

**Notes**:\
 \

~~~~ {.example}
     
     (class) hashmatch(file,md5|sha1|crypt,hash-comparison);
     
~~~~

This function may be used to determine whether a system has a particular
version of a binary file (e.g. software patch).

**ARGUMENTS**:

-   The file concerned
-   The type of hash
-   A string of the hash to which we expect the file to conform.
