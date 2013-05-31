---
layout: default
title: dirname
categories: [Reference, Functions, dirname]
published: true
alias: reference-functions-dirname.html
tags: [reference, functions, dirname]
---



**Synopsis**: dirname(arg1) returns type **string**

  
 *arg1* : File path, *in the range* .\*   

Return the parent directory name for given path

**Example**:  
   

```cf3
vars:
  "apache_dir" string => dirname("/etc/apache2/httpd.conf");
```

**Notes**:  
   
 *History*: Was introduced in 3.3.0, Nova 2.2.0 (2011)

This function returns directory name for the argument. If directory name
is provided, name of parent directory is returned.

See also: `lastnode`, `filestat`, `splitstring`.
