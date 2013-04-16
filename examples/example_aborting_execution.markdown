## Aborting execution

Sometimes it is useful to abort a bundle execution if certain conditions are not met, for example when validating input to a bundle. The following policy uses a list of regular expressions for classes, or class expressions that `cf-agent` will watch out for. If any of these classes becomes defined, it will cause the current bundle to be aborted.

    body common control

    {
    bundlesequence  => { "testbundle"  };

    version => "1.2.3";
    }

    ###########################################

    body agent control

    {
    abortbundleclasses => { "invalid" };            # Abort bundle execution if this class is set
    }

    ###########################################

    bundle agent testbundle
    {
    vars:

     "userlist" slist => { "xyz", "mark", "jeang", "jonhenrik", "thomas", "eben" };

    methods:

     "any" usebundle => subtest("$(userlist)");

    }

    ###########################################

    bundle agent subtest(user)

    {
    classes:

      "invalid" not => regcmp("[a-z][a-z][a-z][a-z]","$(user)"); # The class 'invalid' is set if the user name does not
                                                                 # contain exactly four un-capitalized letters (bundle
                                                                 # execution will be aborted if set)

    reports:

     !invalid::

      "User name $(user) is valid at 4 letters";

     invalid::

      "User name $(user) is invalid";
    }

This policy can be found in `/var/cfengine/share/doc/examples/unit_abort.cf`. You can test it locally by copying it into `/var/cfengine/inputs` and running:

	/var/cfengine/bin/cf-agent -f /var/cfengine/inputs/unit_abort.cf

Alternatively you can integrate it into your main policy:

1. Copy the above content into a file called `/var/cfengine/masterfiles/unit_abort.cf` or copy the file from `/var/cfengine/share/doc/examples/unit_abort.cf` to `/var/cfengine/masterfiles`.

2. Delete the `body common control` section in `/var/cfengine/masterfiles/unit_abort.cf`:

		body common control
		{
		bundlesequence  => { "testbundle" };
		}

3. There cannot be two `body agent control` in the main policy. Copy and paste `abortbundleclasses => { "invalid" };` into /var/cfengine/masterfiles/controls/cf_agent.cf. If you add it to the end of the file it should look something like this:

        ...
        #  dryrun => "true";
        
        abortbundleclasses => { "invalid" };
        }

Delete the `body agent control`section from section from /var/cfengine/masterfiles/unit_abort.cf.

4. Insert the bundle name in the `bundlesequence` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

	    bundlesequence => {
		                    ...
		                    "testbundle",
		                    ...
		                  };

5. Insert the policy file name in the `inputs` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

            inputs => {
                        ...
                        "unit_abort.cf",
                        ...
                      };

This policy snippet will now be executed every five minutes along with the rest of your main policy.
