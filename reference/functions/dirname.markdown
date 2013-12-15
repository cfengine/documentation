---
layout: default
title: dirname
categories: [Reference, Functions, dirname]
published: true
alias: reference-functions-dirname.html
tags: [reference, files functions, functions, dirname]
---

[%CFEngine_function_prototype(path)%]

**Description:** Return the parent directory name for given `path`.

This function returns the directory name for `path`. If `path` is a 
directory, then the name of its parent directory is returned.

[%CFEngine_function_attributes(path)%]

**Example:**  

```cf3
body common control
{
      bundlesequence => { "example" };
}

bundle agent example
{
  vars:
      "apache_dir" string => dirname("/etc/apache2/httpd.conf");
  reports:
      "apache conf dir = $(apache_dir)";
}
```

Output:

```
R: apache conf dir = /etc/apache2
```

**Notes:**

**History:** Was introduced in 3.3.0, Nova 2.2.0 (2011)

**See also:** [`lastnode()`][lastnode], [`filestat()`][filestat], 
[`splitstring()`][splitstring].
