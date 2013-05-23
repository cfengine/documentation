---
layout: default
title: Example - Ensure a process is not running
categories: [Examples, Ensure a process is not running]
published: true
alias: examples-ensure-process-not-running.html
tags: [Examples, process, kill]
---

This is a standalone policy that will kill the `sleep` process. You can adapt
it to make sure that any undesired process is not running.

```cf3
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
```

This policy can be found in `/var/cfengine/share/doc/examples/unit_process_kill.cf`.
