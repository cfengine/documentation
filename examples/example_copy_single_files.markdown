---
layout: default
title: Copy single files
categories: [Examples, Copy single files]
published: true
alias: examples-copy-single-files.html
tags: [Examples, copy files]
---

This is a standalone policy example that will copy single files, locally (`local_cp`) and from a remote site (`secure_cp`). The CFEngine Standard Library (cfengine_stdlib.cf) should be included in the `/var/cfengine/inputs/libraries/` directory and input as below.

```cf3
	body common control
	{
	bundlesequence  => { "mycopy" };
	inputs => { "libraries/cfengine_stdlib.cf" };  # Include the CFEngine Standard Library
	}

	bundle agent mycopy
	{
	files:

	  "/home/mark/tmp/test_plain"        # Path and name of the file we wish to copy to

	    copy_from => local_cp("$(sys.workdir)/bin/file"); # Copy locally from path/filename

	  "/home/mark/tmp/test_remote_plain" # Path and name of the file we wish to copy to

	    copy_from => secure_cp("$(sys.workdir)/bin/file","serverhost"); # Copy remotely from path/filename and specified host
                                                                            # Change to actual host name or IP address
	}
```

This policy can be found in `/var/cfengine/share/doc/examples/unit_copy_copbl.cf`.
