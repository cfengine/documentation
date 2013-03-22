## Kill process

This is a standalone policy that will kill the `sleep` process. You can adapt it to make sure that any undesired process is not running.

	body common control
	{
	bundlesequence => { "process_kill" };
	}



	bundle agent process_kill
	{
	processes:

	 "sleep"

	   signals => { "term", "kill" }; #Signals are presented as an ordered list to the process.
	                                  #On windows, only the kill signal is supported, which terminates the process.

	}

This policy can be found in `/var/cfengine/share/doc/examples/unit_process_kill.cf`. You can test it locally by copying it into `/var/cfengine/inputs` and running:

	/var/cfengine/bin/cf-agent -f /var/cfengine/inputs/unit_process_kill.cf

Alternatively you can integrate it into your main policy:

1. Copy the above content into a file called `/var/cfengine/masterfiles/unit_process_kill.cf` or copy the file from `/var/cfengine/share/doc/examples/unit_process_kill.cf` to `/var/cfengine/masterfiles`.

2. Delete the `body common control` section in `/var/cfengine/masterfiles/unit_process_kill.cf`:

		body common control
		{
		bundlesequence  => { "process_kill" };
		}

3. Insert the bundle name in the `bundlesequence` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

	    bundlesequence => {
		                    ...
		                    "process_kill",
		                    ...
		                  };

3. Insert the policy file name in the `inputs` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

            inputs => {
                        ...
                        "unit_process_kill.cf",
                        ...
                      };

This policy snippet will now be executed every five minutes along with the rest of your main policy.
