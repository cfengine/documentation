---
layout: default
title: filestat
categories: [Reference, Functions, filestat]
published: true
alias: reference-functions-filestat.html
tags: [reference, functions, filestat]
---

### Function filestat

**Synopsis**: filestat(arg1, arg2) returns type **string**

  
 *arg1* : File object name, *in the range* "?(/.\*)   
 *arg2* : Name of field to retrieve, *in the range*
size,gid,uid,ino,nlink,ctime,atime,mtime,mode,modeoct,permstr,permoct,type,devno,dev_minor,dev_major,basename,dirname   

Returns the requested file field

**Example**:  
   

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

**Notes**:  
   
The list of fields may be extended as needed.

*History*: Was introduced in version 3.5.0,Enterprise 3.1 (2013)

If the file object does not exist, the function call fails and the
variable does not expand.
