---
layout: default
title: Check filesystem space
categories: [Examples, Check filesystem space]
published: true
alias: examples-check-filesystem-space.html
tags: [Examples, check, filesystem]
reviewed: 2013-05-30
reviewed-by: atsaloli
---

Check how much space (in KB) is available on a directory's current partition.

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

	    "Freedisk $(free)";

	}
```

Example output:

    # cf-agent -f unit_diskfree.cf ; df -k /tmp
    R: Freedisk 48694692
    Filesystem     1K-blocks     Used Available Use% Mounted on
    /dev/sda1      149911836 93602068  48694692  66% /
    # 

This policy can be found in `/var/cfengine/share/doc/examples/unit_diskfree.cf`.
