## Create files and directories

The following is a standalone policy that will create the file `/home/mark/tmp/test_plain` and the directory `/home/mark/tmp/test_dir/` and set permissions on both.

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

This policy can be found in `/var/cfengine/share/doc/examples/unit_create_filedir.cf`. You can test it locally by running:

	/var/cfengine/bin/cf-agent -f /var/cfengine/share/doc/examples/unit_create_filedir.cf

Alternatively you can integrate it into your main policy:

1. Copy the above content into `/var/cfengine/masterfiles/unit_create_filedir.cf` or copy the file from `/var/cfengine/share/doc/examples/unit_create_filedir.cf` to `/var/cfengine/masterfiles`.

2. Delete the `body common control` section in `/var/cfengine/masterfiles/unit_create_filedir.cf`:

		body common control

		{
		bundlesequence  => { "testbundle"  };
		}

3. Insert the bundle name in the `bundlesequence` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

	    bundlesequence => {
		                    ...
		                    "testbundle",
		                    ...
		                  };

4. Insert the policy file name in the `inputs` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

            inputs => {
                        ...
                        "unit_create_filedir.cf",
                        ...
                      };

This policy snippet will now be executed every five minutes along with the rest of your main policy.
