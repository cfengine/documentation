---
layout: default
title: Distribute ssh keys
published: true
tags: [Examples, Policy, ssh, authorized_keys, distribution]
reviewed: 2015-12-15
reviewed-by: nickanderson, enrico
---

This example shows a simple ssh key distribution implementation.

The policy was designed to work with the `services_autorun` feature in
the [Masterfiles Policy Framework][Masterfiles Policy Framework]. The
`services_autorun` feature can be enabled from the augments_file. If
you do not have a `def.json` in the root of your masterfiles directory
simply create it with the following content.

```
{
  "classes": {
               "services_autorun": [ "any" ]
             }
}
```

In the following example we will manage the `authorized_keys` file for
`bob`, `frank`, and `kelly`.

For each listed user the `ssh_key_distribution` bundle is activated if
the user exists on the system. Once activated the
`ssh_key_distribution` bundle ensures that proper permissions are set
on the users `.ssh` directory (home is assumed to be in
`/home/username`) and ensures that the users `.ssh/authorized_keys` is
a copy of the users `authorized_keys` file as found on the server as
defined in the `ssh_key_info` bundle.

Let's assume we collected all users' public keys into a single
directory on the server and that users exist on the clients (and have
corresponding home directory).

Note: special variable [`$(sys.policy_hub)`][sys.policy_hub] contains the hostname of
the policy server.

To deploy this policy simply place it in the `services/autorun`
directory of your masterfiles.

[%CFEngine_include_example(simple_ssh_key_distribution.cf)%]

Example Run:

First make sure the users exist on your system.

```
root@host001:~# useradd bob
root@host001:~# useradd frank
root@host001:~# useradd kelly
```

Then update the policy and run it:

```
root@host001:~# cf-agent -Kf update.cf; cf-agent -KI
    info: Installing cfe_internal_non_existing_package...
    info: Created directory '/home/bob/.ssh/.'
    info: Owner of '/home/bob/.ssh' was 0, setting to 1002
    info: Object '/home/bob/.ssh' had permission 0755, changed it to 0700
    info: Copying from '192.168.56.2:/srv/ssh_authorized_keys/bob'
    info: Owner of '/home/bob/.ssh/authorized_keys' was 0, setting to 1002
    info: Created directory '/home/frank/.ssh/.'
    info: Owner of '/home/frank/.ssh' was 0, setting to 1003
    info: Object '/home/frank/.ssh' had permission 0755, changed it to 0700
    info: Copying from '192.168.56.2:/srv/ssh_authorized_keys/frank'
    info: Owner of '/home/frank/.ssh/authorized_keys' was 0, setting to 1003
    info: Created directory '/home/kelly/.ssh/.'
    info: Owner of '/home/kelly/.ssh' was 0, setting to 1004
    info: Object '/home/kelly/.ssh' had permission 0755, changed it to 0700
    info: Copying from '192.168.56.2:/srv/ssh_authorized_keys/kelly'
    info: Owner of '/home/kelly/.ssh/authorized_keys' was 0, setting to 1004
```
