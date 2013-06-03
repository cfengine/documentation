---
layout: default
title: dirname
categories: [Reference, Functions, dirname]
published: true
alias: reference-functions-dirname.html
tags: [reference, functions, dirname]
---

**Prototype**: `dirname(path)`

**Return type**: `string`

**Description**: Return the parent directory name for given `path`.

This function returns the directory name for `path`. If `path` is a 
directory, then the name of its parent directory is returned.

**Arguments**:

* `path` : File path, *in the range* .\*

**Example**:  

```cf3
    vars:
      "apache_dir" string => dirname("/etc/apache2/httpd.conf");
```

**Notes**:

**History**: Was introduced in 3.3.0, Nova 2.2.0 (2011)

See also: `lastnode`, `filestat`, `splitstring`.
