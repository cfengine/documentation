---
layout: default
title: Example - Customize Message of the Day
categories: [Examples, Customize Message of the Day]
published: true
alias: examples-customize-message-of-the-day.html
tags: [Examples, motd, file editing, files]
---

The Message of the Day is diplayed when you log in or connect to a server. It typically shows information about the operating system, license information, last login, etc.

It is often useful to customize the Message of the Day to inform your users about some specifics of the system they are connecting to. In this example we will look at a bundle which adds three lines to the `/etc/motd` file to inform about some system characteristics and that the system is managed by CFEngine.

The bundle is defined like this:

```cf3
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
```

You can find this bundle in the file `/var/cfengine/share/doc/examples/edit_motd.cf`
