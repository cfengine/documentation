## Set up sudo

Setting up sudo is straightforward, we recommend managing it by copying trusted files from a repository. The following bundle will copy a master sudoers file to `/etc/sudoers`:

	bundle agent sudoers
	{

	# Define the master location of the sudoers file
	vars:

	  "master_location" string => "/home/user/examples";


	# Copy the master sudoers file to /etc/sudoers
	files:

	  "/etc/sudoers"

	     comment => "Make sure the sudo configuration is secure and up to date",
	       perms => mog("440","root","root"),
	   copy_from => secure_cp("$(master_location)/sudoers","$(policy_server)");

	}

We recommend editing the master sudoers file using `visudo` or a similar tool. It is possible to use CFEngine's file editing capabilities to do this directly, but this does not guarantee syntax correctness of the sudoers file and you might end up being locked out of you system.

The following usage of this bundle presumes that you integrate it into the main policy file, `promises.cf`, and that the CFEngine standard library is included in `promises.cf`. To use this policy:

1. Copy the above content into `/var/cfengine/masterfiles/example_sudoers.cf` or copy the file from <path/to/example_sudoers.cf> to `/var/cfengine/masterfiles`.

2. Insert the bundle name in the `bundlesequence` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

	    bundlesequence => {
		                    ...
		                    "sudoers",
		                    ...
		                  };

3. Insert the policy file name in the `inputs` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

            inputs => {
                        ...
                        "example_sudoers.cf",
                        ...
                      };

For reference we include an example of a simple sudoers file:

	# /etc/sudoers
	#
	# This file MUST be edited with the 'visudo' command as root.
	#
	# See the man page for details on how to write a sudoers file.
	#

	Defaults        env_reset

	# Host alias specification

	# User alias specification

	# Cmnd alias specification

	# User privilege specification
	root    ALL=(ALL) ALL

	# Allow members of group sudo to execute any command after they have
	# provided their password
	# (Note that later entries override this, so you might need to move
	# it further down)
	%sudo ALL=(ALL) ALL
	#
	#includedir /etc/sudoers.d

	# Members of the admin group may gain root privileges
	%admin ALL=(ALL) ALL
	john  ALL=(ALL)       ALL

