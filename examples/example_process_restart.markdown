---
layout: default
title: Example - Restart a Process
categories: [Examples, Restart a Process]
published: true
alias: examples-restart-a-process.html
tags: [Examples, process, restart]
---

This is a standalone policy that will restart three CFEngine processes if they are not running. 

```cf3
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
```

Notes: The `canonify` function translates illegal characters to underscore, e.g. `start_cf-monitord` becomes `start_cf_monitord`.

This policy can be found in `/var/cfengine/share/doc/examples/unit_process_restart.cf`.
