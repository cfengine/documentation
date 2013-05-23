---
layout: default
title: Example - Mount NFS filesystem
categories: [Examples, Mount NFS filesystem]
published: true
alias: examples-mount-nfs-filesystem.html
tags: [Examples, mount, nfs, filesystem]
---

Mounting an NFS filesystem is straightforward using CFEngine's storage promises. The following bundle specifies the name of a remote file system server, the path of the remote file system and the mount point directory on the local machine:

```cf3
	bundle agent mounts

	{
	storage:

	  "/mnt" mount  => nfs("slogans.iu.hio.no","/home");  # "/mnt" is the local moint point
	                                                      # "slogans.ui.hio.no" is the remote files system server
	                                                      # "/home" is the path to the remote file system

	}

	######################################################################


	body mount nfs(server,source)

	{
	mount_type => "nfs";           # Protocol type of remote file system
	mount_source => "$(source)";   # Path of remote file system
	mount_server => "$(server)";   # Name or IP of remote file system server
	#mount_options => { "rw" };    # List of option strings to add to the file system table ("fstab")

	edit_fstab => "true";          # True/false add or remove entries to the file system table ("fstab")
	unmount => "true";             # True/false unmount a previously mounted filesystem
	}
```

This policy can be found in `/var/cfengine/share/doc/examples/example_mount_nfs.cf`
