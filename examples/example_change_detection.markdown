## Change detection

This is a standalone policy that will look for changes recursively in a directory and log them in the promise repaired log.

    body common control

    {
    bundlesequence  => { "testbundle"  };
    }

    ########################################################

    bundle agent testbundle

    {
    files:

      "/home/mark/tmp/web" -> "me"  # Directory to monitor for changes.
                                    # The right arrow denotes a promisee,
                                    # or stakeholder, used for documentation purposes

       changes      => detect_all_change,
       depth_search => recurse("inf");
    }

    #########################################################

    body changes detect_all_change

    {
    report_changes => "all";  # This will log all changes to the repaired log (/var/cfengine/cf_repair.log)
    update_hashes  => "true"; # Update hash values immediately after change warning
    }

    #########################################################

    body depth_search recurse(d)

    {
    depth        => "$(d)";
    }

This policy can be found in `/var/cfengine/share/doc/examples/unit_change_detect.cf`. You can test it locally by copying it into `/var/cfengine/inputs` and running:

	/var/cfengine/bin/cf-agent -f /var/cfengine/inputs/unit_change_detect.cf

Alternatively you can integrate it into your main policy:

1. Copy the above content into a file called `/var/cfengine/masterfiles/unit_change_detect.cf` or copy the file from `/var/cfengine/share/doc/examples/unit_change_detect.cf` to `/var/cfengine/masterfiles`.

2. Delete the `body common control` section in `/var/cfengine/masterfiles/unit_change_detect.cf`:

		body common control
		{
		bundlesequence  => { "testbundle" };
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
                        "unit_change_detect.cf",
                        ...
                      };

This policy snippet will now be executed every five minutes along with the rest of your main policy.
