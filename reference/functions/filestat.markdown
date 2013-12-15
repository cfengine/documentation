---
layout: default
title: filestat
categories: [Reference, Functions, filestat]
published: true
alias: reference-functions-filestat.html
tags: [reference, files functions, functions, filestat]
---

[%CFEngine_function_prototype(filename, field)%]

**Description:** Returns the requested file field `field` for the file object 
`filename`.

If the file object does not exist, the function call fails and the
variable does not expand.

**Arguments**:

* `filename` : the file or directory name to inspect, in the range: "?(/.*)
* `field` : the requested field, with the following allowed values:
    * `size` : size in bytes
    * `gid` : group ID
    * `uid` : owner ID
    * `ino` : inode number
    * `nlink` : number of *hard* links
    * `ctime` : creation time in Unix epoch format
    * `atime` : last access time in Unix epoch format
    * `mtime` : last modification time in Unix epoch format
    * `mode` : file mode as a decimal number
    * `modeoct` : file mode as an octal number, e.g. `10777`
    * `permstr` : permission string, e.g. `-rwx---rwx` (not available on Windows)
    * `permoct` : permissions as an octal number, e.g. `644` (not available on Windows)
    * `type` : file type (not available on Windows): `block device`,`character device`, `directory`, `FIFO/pipe`, `symlink`, `regular file`, `socket`, or `unknown`
    * `devno` : device number (drive letter on Windows, e.g. `C:`)
    * `dev_minor` : minor device number (not available on Windows)
    * `dev_major` : major device number (not available on Windows)
    * `basename` : the file name minus the directory
    * `dirname` : the directory portion of the file name
    * `linktarget` : if the file is a `symlink`, its *final* target.  The target is chased up to 32 levels of recursion.  On Windows, this returns the file name itself.
    * `linktarget_shallow` :  if the file is a `symlink`, its *first* target.  On Windows, this returns the file name itself.

**Example:**

```cf3
body common control
{
      bundlesequence => { "example" };
}

bundle agent example
{
  vars:
      "file" string => "$(sys.resolv)";
  methods:
      "fileinfo" usebundle => fileinfo("$(file)");
}
bundle agent fileinfo(f)
{
  vars:
      "fields" slist => splitstring("size,gid,uid,ino,nlink,ctime,atime,mtime,mode,modeoct,permstr,permoct,type,devno,dev_minor,dev_major,basename,dirname,linktarget,linktarget_shallow", ",", 999);

      "stat[$(f)][$(fields)]" string => filestat($(f), $(fields));

  reports:
      "$(this.bundle): file $(f) has $(fields) = $(stat[$(f)][$(fields)])";
}
```

Output:

```
R: fileinfo: file /etc/resolv.conf has size = 45
R: fileinfo: file /etc/resolv.conf has gid = 0
R: fileinfo: file /etc/resolv.conf has uid = 0
R: fileinfo: file /etc/resolv.conf has ino = 2884988
R: fileinfo: file /etc/resolv.conf has nlink = 1
R: fileinfo: file /etc/resolv.conf has ctime = 1370031523
R: fileinfo: file /etc/resolv.conf has atime = 1387021332
R: fileinfo: file /etc/resolv.conf has mtime = 1370031523
R: fileinfo: file /etc/resolv.conf has mode = 33188
R: fileinfo: file /etc/resolv.conf has modeoct = 100644
R: fileinfo: file /etc/resolv.conf has permstr = -rw-r--r--
R: fileinfo: file /etc/resolv.conf has permoct = 644
R: fileinfo: file /etc/resolv.conf has type = regular file
R: fileinfo: file /etc/resolv.conf has devno = 2049
R: fileinfo: file /etc/resolv.conf has dev_minor = 1
R: fileinfo: file /etc/resolv.conf has dev_major = 8
R: fileinfo: file /etc/resolv.conf has basename = resolv.conf
R: fileinfo: file /etc/resolv.conf has dirname = /etc
R: fileinfo: file /etc/resolv.conf has linktarget = /etc/resolv.conf
R: fileinfo: file /etc/resolv.conf has linktarget_shallow = /etc/resolv.conf
```

**Notes:**  
   
The list of fields may be extended as needed.

**History:** Was introduced in version 3.5.0,Enterprise 3.1 (2013).  `linktarget` and `linktarget_shallow` were added in version 3.6.

**See also:** `lastnode()`, `dirname()`, `splitstring()`.
