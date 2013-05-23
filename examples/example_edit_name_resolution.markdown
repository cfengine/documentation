---
layout: default
title: Example - Set up name resolution with DNS
categories: [Examples, Set up name resolution with DNS]
published: true
alias: examples-setup-name-resolution-dns.html
tags: [Examples, dns, file editing, files]
---

There are many ways to do name resolution setup. A simple and straightforward approach is to implement this as a simple editing promise for the `/etc/resolv.conf` file.

```cf3
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
```

This policy can be found in `/var/cfengine/masterfiles/example_edit_name_resolution.cf`
