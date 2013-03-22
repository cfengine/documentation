## Check filesystem space

This is a standalone policy that will check how much space (in KB) is available on a directory's current partition.

	body common control

	{
	bundlesequence  => { "example" };
	}

	###########################################################

	bundle agent example

	{
	vars:

	  "free" int => diskfree("/tmp");

	reports:

	  cfengine_3::

	    "Freedisk $(free)";

	}

This policy can be found in `/var/cfengine/share/doc/examples/unit_diskfree.cf`. You can test it locally by copying it into `/var/cfengine/inputs` and running:

	/var/cfengine/bin/cf-agent -f /var/cfengine/inputs/unit_diskfree.cf

Alternatively you can integrate it into your main policy:

1. Copy the above content into a file called `/var/cfengine/masterfiles/unit_diskfree.cf` or copy the file from `/var/cfengine/share/doc/examples/unit_diskfree.cf` to `/var/cfengine/masterfiles`.

2. Delete the `body common control` section in `/var/cfengine/masterfiles/unit_diskfree.cf`:

		body common control
		{
		bundlesequence  => { "example" };
		}

3. Insert the bundle name in the `bundlesequence` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

	    bundlesequence => {
		                    ...
		                    "example",
		                    ...
		                  };

3. Insert the policy file name in the `inputs` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

            inputs => {
                        ...
                        "unit_diskfree.cf",
                        ...
                      };

This policy snippet will now be executed every five minutes along with the rest of your main policy.
