---
layout: default
title: Check filesystem space
categories: [Examples, Check filesystem space]
published: true
alias: examples-check-filesystem-space.html
tags: [Examples, check, filesystem]
---

This is a standalone policy that will check how much space (in KB) is available on a directory's current partition.

```cf3
	body common control

	{
	bundlesequence  => { "example" };
	}

	###########################################################

	bundle agent example

	{
	vars:

	  "free" int => diskfree("/tmp");

	reports:

	  cfengine_3::

	    "Freedisk $(free)";

	}
```

This policy can be found in `/var/cfengine/share/doc/examples/unit_diskfree.cf`.