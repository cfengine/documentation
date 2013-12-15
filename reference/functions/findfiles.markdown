---
layout: default
title: findfiles
categories: [Reference, Functions, findfiles]
published: true
alias: reference-functions-findfiles.html
tags: [reference, file functions, functions, findfiles, files, glob]
---

[%CFEngine_function_prototype(glob1, glob2, ...)%]

**Description:** Return the list of files that match any of the given glob patterns.

This function searches for the given glob patterns in the local
filesystem, returning files or directories that match.  Note that glob
patterns are not regular expressions.  They match like Unix shells:

* `*` matches any filename or directory at one level, e.g. `*.cf` will
match all files in one directory that end in `.cf` but it won't search
across directories.  `*/*.cf` on the other hand will look two levels
deep.
* `?` matches a single letter
* `[a-z]` matches any letter from `a` to `z`
* `{x,y,anything}` will match `x` or `y` or `anything`.

This function, used together with the `bundlesmatching` function,
allows you to do dynamic inputs and a dynamic bundle call chain.


**Example:**  


```cf3
body common control
{
      bundlesequence => { run };
}

bundle agent run
{
  vars:
      "all_root" slist => findfiles("/*");
  reports:
      "All files under root = $(all_root)";
}

```

Output:

```
R: All files under root = /bin
R: All files under root = /boot
R: All files under root = /dev
R: All files under root = /etc
R: All files under root = /home
R: All files under root = /initrd.img
R: All files under root = /lib
R: All files under root = /lib64
R: All files under root = /lost+found
R: All files under root = /media
R: All files under root = /mnt
R: All files under root = /opt
R: All files under root = /proc
R: All files under root = /root
R: All files under root = /run
R: All files under root = /sbin
R: All files under root = /selinux
R: All files under root = /srv
R: All files under root = /sys
R: All files under root = /tmp
R: All files under root = /usr
R: All files under root = /var
R: All files under root = /vmlinuz
```

**See also:** [`bundlesmatching()`][bundlesmatching].
