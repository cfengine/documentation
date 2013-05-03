---
layout: default
title: Function-regcmp
categories: [Special-functions,Function-regcmp]
published: true
alias: Special-functions-Function-regcmp.html
tags: [Special-functions,Function-regcmp]
---

### Function regcmp

**Synopsis**: regcmp(arg1,arg2) returns type **class**

\
 *arg1* : Regular expression, *in the range* .\* \
 *arg2* : Match string, *in the range* .\* \

True if arg1 is a regular expression matching that matches string arg2

**Example**:\
 \

~~~~ {.verbatim}
bundle agent subtest(user)

{
classes:

  "invalid" not => regcmp("[a-z]{4}","$(user)");

reports:

 !invalid::

  "User name $(user) is valid at exactly 4 letters";

 invalid::

  "User name $(user) is invalid";
}
~~~~

**Notes**:\
 \

Compares a string to a regular expression.

**ARGUMENTS**:

regex

A regular expression to match the content. The regular expression is
anchored, meaning it must match the complete content (See [Anchored vs.
unanchored regular
expressions](#Anchored-vs_002e-unanchored-regular-expressions)). \

string

Test data for the regular expression.

If there are multiple-lines in the data, it is necessary to code these
explicitly, as regular expressions do not normally match the end of line
as a regular character (they only match end of string). You can do this
using either standard regular expression syntax or using the additional
features of PCRE (where `(?ms)` changes the way that ., \^ and \$
behave), e.g.

~~~~ {.smallexample}
     
     body common control
     {
     bundlesequence = { "example" };
     }
     
     bundle agent example
     {
     vars:
     
       "x" string = "
     NAME: apache2 - Apache 2.2 web server
     CATEGORY: application
     ARCH: all
     VERSION: 2.2.3,REV=2006.09.01
     BASEDIR: /
     VENDOR: http://httpd.apache.org/ packaged for CSW by Cory Omand
     PSTAMP: comand@thor-20060901022929
     INSTDATE: Dec 14 2006 16:05
     HOTLINE: http://www.blastwave.org/bugtrack/
     EMAIL: comand@blastwave.org
     STATUS: completely installed
     ";
     
     classes:
     
       "pkg_installed" expression = regcmp("(.*\n)*STATUS:\s+completely installed\n(.*\n)*",$(x));
     
       "base_is_root" expression = regcmp("(?ms).*^BASEDIR:\s+/$.*", $(x));
     
     reports:
     
       pkg_installed::
     
         "installed";
     
       base_is_root::
     
         "in root";
     }
     
     
~~~~
