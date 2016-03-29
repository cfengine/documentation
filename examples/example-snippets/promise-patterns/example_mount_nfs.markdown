---
layout: default
title: Mount NFS filesystem
published: true
tags: [Examples, Policy, mount, nfs, filesystem]
reviewed: 2013-06-08
reviewed-by: atsaloli
---

Mounting an NFS filesystem is straightforward using CFEngine's storage promises. The following bundle specifies the name of a remote file system server, the path of the remote file system and the mount point directory on the local machine:

```cf3
body common control
{
bundlesequence => { "mounts" };
}


bundle agent mounts
{
storage:

  "/mnt" mount  => nfs("fileserver","/home");  # "/mnt" is the local moint point
                                               # "fileserver" is the remote fileserver
                                               # "/home" is the path to the remote file system
}


body mount nfs(server,source)
{
mount_type => "nfs";           # Protocol type of remote file system
mount_source => "$(source)";   # Path of remote file system
mount_server => "$(server)";   # Name or IP of remote file system server
mount_options => { "rw" };     # List of option strings to add to the file system table ("fstab")
edit_fstab => "true";          # True/false add or remove entries to the file system table ("fstab")
}
```

This policy can be found in `/var/cfengine/share/doc/examples/example_mount_nfs.cf`

Here is an example run.  At start, the filesystem is not in /etc/fstab and is not mounted:

```
# grep mnt /etc/fstab # filesystem is not in /etc/fstab
# df |grep mnt # filesystem is not mounted
```

Now we run CFEngine to mount the filesystem and add it to /etc/fstab:

```
# cf-agent -f example_mount_nfs.cf
2013-06-08T17:48:42-0700    error: Attempting abort because mount went into a retry loop.
# grep mnt /etc/fstab
fileserver:/home 	 /mnt 	 nfs 	 rw
# df |grep mnt
fileserver:/home 149912064 94414848  47882240  67% /mnt
#
```

Note: CFEngine errors out after it mounts the filesystem and updates
/etc/fstab.  There is a ticket https://cfengine.com/dev/issues/2937
open on this issue.
