---
layout: default
title: Set up sudo
published: true
tags: [Examples, Policy, sudo, file editing]
reviewed: 2013-06-08
reviewed-by: atsaloli
---

Setting up sudo is straightforward, we recommend managing it by copying trusted files from a repository. The following bundle will copy a master sudoers file to `/etc/sudoers` (`/tmp/sudoers` in this example - change it to `/etc/sudoers` to use in production).

```cf3

body common control
{
bundlesequence => { "sudoers" };
inputs => { "libraries/cfengine_stdlib.cf" };
}


bundle agent sudoers
{

# Define the master location of the sudoers file
vars:

  "master_location" string => "/var/cfengine/masterfiles";


# Copy the master sudoers file to /etc/sudoers
files:

  "/tmp/sudoers"  # change to /etc/sudoers to use in production

     comment => "Make sure the sudo configuration is secure and up to date",
       perms => mog("440","root","root"),
   copy_from => secure_cp("$(master_location)/sudoers","$(sys.policy_hub)");

}
```

We recommend editing the master sudoers file using `visudo` or a similar tool. It is possible to use CFEngine's file editing capabilities to edit sudoers directly, but this does not guarantee syntax correctness and you might end up locked out.

Example run:

```
# cf-agent -f temp.cf -KI
2013-06-08T19:13:21-0700     info: This agent is bootstrapped to '192.168.183.208'
2013-06-08T19:13:22-0700     info: Running full policy integrity checks
2013-06-08T19:13:23-0700     info: Copying from '192.168.183.208:/var/cfengine/masterfiles/sudoers'
2013-06-08T19:13:23-0700     info: /sudoers/files/'/tmp/sudoers': Object '/tmp/sudoers' had permission 0600, changed it to 0440
#
```

For reference we include an example of a simple sudoers file:

	# /etc/sudoers
	#
	# This file MUST be edited with the 'visudo' command as root.
	#

	Defaults        env_reset

	# User privilege specification
	root    ALL=(ALL) ALL

	# Allow members of group sudo to execute any command after they have
	# provided their password
	%sudo ALL=(ALL) ALL

	# Members of the admin group may gain root privileges
	%admin ALL=(ALL) ALL
	john  ALL=(ALL)       ALL
