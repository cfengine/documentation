---
layout: default
title: filestat
published: true
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
    * `xattr` : a string with newline-separated extended attributes and SELinux contexts in `key=value<NEWLINE>key2=value2<NEWLINE>tag1<NEWLINE>tag2` format.

On Mac OS X, you can list and set extended attributes with the `xattr` utility.

On SELinux, the contexts are the same as what you see with `ls -Z`.

**Example:**

Prepare:

[%CFEngine_include_snippet(filestat.cf, #\+begin_src prep, .*end_src)%]

Run:

[%CFEngine_include_snippet(filestat.cf, #\+begin_src cfengine3, .*end_src)%]

Output:

[%CFEngine_include_snippet(filestat.cf, #\+begin_src\s+example_output\s*, .*end_src)%]

**Notes:**

* `linktarget` will prepend the directory name to *relative symlink targets*, in order to be able to resolve them. Use `linktarget_shallow` to get the exact link as-is in case it is a relative link.
* The list of fields may be extended as needed by CFEngine.

**History:** Was introduced in version 3.5.0,Enterprise 3.1 (2013).  `linktarget` and `linktarget_shallow` were added in version 3.6.

**See also:** `lastnode()`, `dirname()`, `splitstring()`.
