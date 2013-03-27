## Copy single files

This is a standalone policy example that will copy single files, locally (`local_cp`) and from a remote site (`secure_cp`). The CFEngine Standard Library (cfengine_stdlib.cf) should be included in the `/var/cfengine/inputs/libraries/` directory and input as below.

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

This policy can be found in `/var/cfengine/share/doc/examples/unit_copy_copbl.cf`. You can test it locally by copying it into `/var/cfengine/inputs` and running:

	/var/cfengine/bin/cf-agent -f /var/cfengine/inputs/unit_copy_copbl.cf

Alternatively you can integrate it into your main policy:

1. Copy the above content into a file called `/var/cfengine/masterfiles/unit_copy_copbl.cf` or copy the file from `/var/cfengine/share/doc/examples/unit_copy_copbl.cf` to `/var/cfengine/masterfiles`.

2. Delete the `body common control` section in `/var/cfengine/masterfiles/unit_copy_copbl.cf`:

		body common control

		{
		bundlesequence  => { "mycopy" };
		inputs => { "libraries/cfengine_stdlib.cf" };
		}

3. Insert the bundle name in the `bundlesequence` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

	    bundlesequence => {
		                    ...
		                    "mycopy",
		                    ...
		                  };

4. Insert the policy file name in the `inputs` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

            inputs => {
                        ...
                        "unit_copy_copbl.cf",
                        ...
                      };

This policy snippet will now be executed every five minutes along with the rest of your main policy.
