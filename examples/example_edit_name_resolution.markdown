## Set up name resolution (DNS)

There are many ways to do name resolution setup. A simple and straightforward approach is to implement this as a simple editing promise for the /etc/resolv.conf file.

	bundle agent edit_name_resolution
	{

	files:

	  "/tmp/resolv.conf"   # This is for testing, change to "$(sys.resolv)" to put in production

	     comment       => "Add lines to the resolver configuration",
	     create        => "true",     # Make sure the file exists, create it if not
	     edit_line     => resolver,   # Call the resolver bundle defined below to do the editing
	     edit_defaults => std_defs;   # Standard library body that ...

	}

	#######################################################


	bundle edit_line resolver

	{
	delete_lines:

	  # delete any old search domains or name servers we no longer need
	  "search.*";
	  "nameserver 80.65.58.31";
	  "nameserver 80.65.58.32";

	insert_lines:

	 any::   # Class/context where you use the below nameservers. Change to appropriate class
		 # for your system (if not all::, for example server_group::, ubuntu::, etc.)

	  # insert the search domain or name servers we want
	  "search mydomain.tld" location => start;  # Replace mydomain.tld with your domain name
	  "nameserver 128.39.89.8";
	  "nameserver 128.39.74.66";

	}

The following usage of this bundle presumes that you integrate it into the main policy file, `promises.cf`, and that the CFEngine standard library is included in `promises.cf`. To use this bundle:

1. Copy the above content into `/var/cfengine/masterfiles/example_edit_name_resolution.cf` or copy the file from `<path/to/example_edit_name_resolution.cf>` to `/var/cfengine/masterfiles`.

2. Insert the bundle name in the `bundlesequence` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

	    bundlesequence => {
		                    ...
		                    "edit_name_resolution",
		                    ...
		                  };

3. Insert the policy file name in the `inputs` section of the main policy file (`/var/cfengine/masterfiles/promises.cf`) on the policy server:

            inputs => {
                        ...
                        "example_edit_name_resolution.cf",
                        ...
                      };

Note: DNS is not the only name service, of course. Unix has its older `/etc/hosts` file which can also be managed using file editing. A similar policy can easily be made for `/etc/hosts` with corresponding content, i.e.:

	bundle agent system_files
	{
	files:

	   "/etc/hosts"

	     comment => "Add hosts to the /etc/hosts file",
	   edit_line => fix_etc_hosts;
	}

	bundle edit_line fix_etc_hosts
	{
	vars:

	 "names[127.0.0.1]"    string => "localhost localhost.CFEngine.com";
	 "names[128.39.89.12]" string => "myhost myhost.CFEngine.com";
	 "names[128.39.89.13]" string => "otherhost otherhost.CFEngine.com";

	 # etc


	 "i" slist => getindices("names");

	insert_lines:

	 "$(i)     $(names[$(i)])";

	}

