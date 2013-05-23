---
layout: default
title: Example - Create files and directories
categories: [Examples, Create files and directories]
published: true
alias: examples-create-files-and-directories.html
tags: [Examples, create, files and directories]
---

The following is a standalone policy that will create the file `/home/mark/tmp/test_plain` and the directory `/home/mark/tmp/test_dir/` and set permissions on both.

```cf3
    body common control
	{
	bundlesequence  => { "testbundle"  };
	}


	bundle agent testbundle

	{
	files:

	  "/home/mark/tmp/test_plain"  # Path and name of the file we wish to create

	       perms => system,        # Set the permissions of the file as defined in the body "system" below
	       create => "true";       # Make sure the file exists, create if not

	  "/home/mark/tmp/test_dir/."  # Note the trailing "/." (this tells CFEngine it's a directory)

	       perms => system,        # Set the permissions of the directory as defined in the body "system" below
	       create => "true";       # Make sure the directory exists, create if not

	}


	body perms system

	{
	mode  => "0640";               # Set permissions to "0640"
	}
```

This policy can be found in `/var/cfengine/share/doc/examples/unit_create_filedir.cf`.
