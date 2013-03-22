## Restart process

This is a standalone policy that will restart three CFEngine processes if they are not running. 

	body common control
	{
	bundlesequence => { "process_restart" };
	}

	#########################################################

	bundle agent process_restart
	{
	vars:

	  "component" slist => {              # List of processes to monitor
		               "cf-monitord",
		               "cf-serverd",
		               "cf-execd"
		               };
	processes:

	  "$(component)"
		restart_class => canonify("start_$(component)"); # Set the class "start_<component>" if it is not running

	commands:

	   "/var/cfengine/bin/$(component)"
	       ifvarclass => canonify("start_$(component)"); # Evaluate the class "start_<component>", CFEngine will run 
	                                                     # the command if "start_<component> is set.

	}

Notes: The `canonify` function translates illegal characters to underscore, e.g. `start_cf-monitord` becomes `start_cf_monitord`.

This policy can be found in `/var/cfengine/share/doc/examples/unit_process_restart.cf`. You can test it locally by copying it into `/var/cfengine/inputs` and running:

	/var/cfengine/bin/cf-agent -f /var/cfengine/inputs/unit_process_restart.cf

Alternatively you can integrate it into your main policy:

1. Copy the above content into a file called `/var/cfengine/masterfiles/unit_process_restart.cf` or copy the file from `/var/cfengine/share/doc/examples/unit_process_restart.cf` to `/var/cfengine/masterfiles`.

2. Delete the `body common control` section in `/var/cfengine/masterfiles/unit_process_restart.cf`:

		body common control
		{
		bundlesequence  => { "process_restart" };
		}

3. Insert the bundle name in the `bundlesequence` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

	    bundlesequence => {
		                    ...
		                    "process_restart",
		                    ...
		                  };

3. Insert the policy file name in the `inputs` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

            inputs => {
                        ...
                        "unit_process_restart.cf",
                        ...
                      };

This policy snippet will now be executed every five minutes along with the rest of your main policy.
