---
layout: default
title: Filenames and Paths
categories: [Reference, Syntax, Filenames and Paths]
published: true
alias: reference-syntax-filenames-and-paths.html
tags: [reference, syntax, directory, paths, filesystem]
---

Filenames in Unix-like operating systems use the forward slash '/'
character for their directory separator. All references to file
locations must be absolute pathnames in CFEngine, i.e. they must
begin with a complete specification of which directory they are in.
For example:

         /etc/passwd
         /var/cfengine/masterfiles/distfile

The only place where it makes sense to refer to a file without a
complete directory specification is when searching through
directories for different kinds of file, e.g. in pattern matching

    leaf_name => { "tmp_.*", "output_file", "core" };

Here, one can write core without a path, because one is looking for
any file of that name in a number of directories.

The Windows operating systems traditionally use a different
filename convention. The following are all valid absolute file
names under Windows:

          c:\winnt
          "c:\spaced name"
          c:/winnt
          /var/cfengine/inputs
          //fileserver/share2/dir

The 'drive' name "C:" in Windows refers to a partition or device.
Unlike Unix, Windows does not integrate these seamlessly into a
single file-tree. This is not a valid absolute filename:

         \var\cfengine\inputs

Paths beginning with a backslash are assumed to be win32 paths.
They must begin with a drive letter or double-slash server name.

Note in recent versions of Cygwin you can decide to use the
`/cygdrive` to specify a path to windows file E.g
/cygdrive/c/myfile means c:\\myfile or you can do it straight away
in CFEngine as `c:\myfile`.

