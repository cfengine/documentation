## Customize Message of the Day (motd)

The Message of the Day is diplayed when you log in or connect to a server. It typically shows information about the operating system, license information, last login, etc.

It is often useful to customize the Message of the Day to inform your users about some specifics of the system they are connecting to. In this example we will look at a bundle which adds three lines to the `/etc/motd` file to inform about some system characteristics and that the system is managed by CFEngine.

The bundle is defined like this:

	bundle agent edit_motd
	{
	files:
	  "/tmp/motd"   # This is for testing, replace with "/etc/motd" to put in production
	    edit_line     => my_motd,  # Call the bundle my_motd to edit the file
	    edit_defaults => empty,    # Empty /etc/motd if it has any content
	    create        => "true";   # Ensure the motd file exists
	}

        # Insert content into the motd file
	bundle edit_line my_motd
	{
	vars:
	  "interfaces_str"  string => join(", ","sys.interfaces");
	  "ipaddresses_str" string => join(", ","sys.ip_addresses");

	insert_lines:
	"Welcome to $(sys.fqhost)!
	This system is managed by CFEngine.
	The policy was last updated on $(sys.last_policy_update).
	The system has $(sys.cpus) cpus.
	Network interfaces on this system are $(interfaces_str),
	and the ip-addresses assigned are $(ipaddresses_str).";
	}

You can find this bundle in the file <path/to/edit_motd.cf TBD>

The following usage of this bundle presumes that you integrate it into the main policy file, `promises.cf`, and that the CFEngine standard library is included in `promises.cf`. To use this bundle:

1. Copy the above content into `/var/cfengine/masterfiles/example_edit_motd.cf` or copy the file from `<path/to/example_edit_motd.cf>` to `/var/cfengine/masterfiles`.

2. Insert the bundle name in the `bundlesequence` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

	    bundlesequence => {
		                    ...
		                    "edit_motd",
		                    ...
		                  };

3. Insert the policy file name in the `inputs` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

            inputs => {
                        ...
                        "example_edit_motd.cf",
                        ...
                      };

This policy snippet will now be executed every five minutes along with the rest of your main policy.
