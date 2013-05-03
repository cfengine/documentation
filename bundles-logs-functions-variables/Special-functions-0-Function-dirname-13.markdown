---
layout: default
title: Function-dirname-13
categories: [Special-functions,Function-dirname-13]
published: true
alias: Special-functions-Function-dirname-13.html
tags: [Special-functions,Function-dirname-13]
---

### Function dirname

**Synopsis**: dirname(arg1) returns type **string**

\
 *arg1* : File path, *in the range* .\* \

Return the parent directory name for given path

**Example**:\
 \

~~~~ {.verbatim}
vars:
  "apache_dir" string => dirname("/etc/apache2/httpd.conf");
~~~~

**Notes**:\
 \
 *History*: Was introduced in 3.3.0, Nova 2.2.0 (2011)

This function returns directory name for the argument. If directory name
is provided, name of parent directory is returned.
