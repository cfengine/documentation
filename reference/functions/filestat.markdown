---
layout: default
title: filestat
categories: [Reference, Functions, filestat]
published: true
alias: reference-functions-filestat.html
tags: [reference, files functions, functions, filestat]
---

**Prototype:** `filestat(filename, field)`

**Return type:** `string`

**Description:** Returns the requested file field.

If the file object does not exist, the function call fails and the
variable does not expand.

**Arguments**:

* `filename` : File object name, in the range `"?(/.*)`
* `field` : Name of field to retrieve, in the range
    * `size`
    * `gid`
    * `uid`
    * `ino`
    * `nlink`
    * `ctime`
    * `atime`
    * `mtime`
    * `mode`
    * `modeoct`
    * `permstr`
    * `permoct`
    * `type`
    * `devno`
    * `dev_minor`
    * `dev_major`
    * `basename`
    * `dirname`

**Example:**

```cf3
    bundle agent fileinfo(f)
    {
      vars:
          "fields" slist => splitstring("size,gid,uid,ino,nlink,ctime,atime,mtime,mode,modeoct,permstr,permoct,type,devno,dev_minor,dev_major,basename,dirname", ",", 999);

          "stat[$(f)][$(fields)]" string => filestat($(f), $(fields));

      reports:
          "$(this.bundle): file $(f) has $(fields) = $(stat[$(f)][$(fields)])";
    }
```

**Notes:**  
   
The list of fields may be extended as needed.

**History**: Was introduced in version 3.5.0,Enterprise 3.1 (2013)

**See also:** [`lastnode()`][lastnode], [`dirname()`][dirname], 
[`splitstring()`][splitstring].
