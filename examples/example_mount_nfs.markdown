## Mount NFS filesystem

Mounting an NFS filesystem is straightforward using CFEngine's storage promises. The following bundle specifies the name of a remote file system server, the path of the remote file system and the mount point directory on the local machine:

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

The following usage of this bundle presumes that you integrate it into the main policy file, `promises.cf`. To use this policy:

1. Copy the above content into `/var/cfengine/masterfiles/example_mount_nfs.cf` or copy the file from <path/to/example_mount_nfs.cf> to `/var/cfengine/masterfiles`.

2. Insert the bundle name in the `bundlesequence` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

	    bundlesequence => {
		                    ...
		                    "mounts",
		                    ...
		                  };

3. Insert the policy file name in the `inputs` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

            inputs => {
                        ...
                        "example_mount_nfs.cf",
                        ...
                      };


