## Software and patch installation

This is a standalone policy that will install a list of packages on a yum based system. CFEngine interfaces with the package manager and lets it do the job. The CFEngine Standard Library (cfengine_stdlib.cf) should be included in the `/var/cfengine/inputs/libraries/` directory and input as below.

	body common control
	{
	bundlesequence => { "packages" };
	inputs => { "libraries/cfengine_stdlib.cf" };
	}

	#############################################

	bundle agent packages
	{
	vars:

	 # Test the simplest case -- leave everything to the yum smart manager

	 "match_package" slist => {                   # List of packages to install
		                  "apache2",
		                  "apache2-mod_php5",
		                  "apache2-prefork",
		                  "php5"
		                  };
	packages:

	  "$(match_package)"

	     package_policy => "add",                 # Install the packages
	     package_method => yum;                   # Use yum to install

	}

CFEngine will download the necessary packages from the default repositories if they are not present on the local machine, then install them if they are not already installed.

This policy can be found in `/var/cfengine/share/doc/examples/unit_package_yum.cf`. You can test it locally by copying it into `/var/cfengine/inputs` and running:

	/var/cfengine/bin/cf-agent -f /var/cfengine/inputs/unit_package_yum.cf

Alternatively you can integrate it into your main policy:

1. Copy the above content into a file called `/var/cfengine/masterfiles/unit_package_yum.cf` or copy the file from `/var/cfengine/share/doc/examples/unit_package_yum.cf` to `/var/cfengine/masterfiles`.

2. Delete the `body common control` section in `/var/cfengine/masterfiles/unit_package_yum.cf`:

		body common control
		{
		bundlesequence  => { "packages" };
		}

3. Insert the bundle name in the `bundlesequence` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

	    bundlesequence => {
		                    ...
		                    "packages",
		                    ...
		                  };

3. Insert the policy file name in the `inputs` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

            inputs => {
                        ...
                        "unit_package_yum.cf",
                        ...
                      };

This policy snippet will now be executed every five minutes along with the rest of your main policy.

Similar policy examples are available in `/var/cfengine/share/doc/examples/` for:

 - Debian (unit_package_apt.cf)
 - MSI for Windows (unit_package_msi_file.cf)
 - Solaris (unit_package_solaris.cf)
 - SuSE Linux (unit_package_zypper.cf)
