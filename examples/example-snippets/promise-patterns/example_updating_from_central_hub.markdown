---
layout: default
title: Updating from a central policy server
published: true
tags: [Examples, Policy, updating, policy server]
reviewed: 2013-06-09
reviewed-by: atsaloli
---

This is a conceptual example without any test policy associated with it.

The default policy shipped with CFEngine contains a centralized updating of policy that
covers more subtleties than this example, and handles fault tolerance. Here is the main
idea behind it. For simplicity, we assume that all hosts are on network 10.20.30.* and that
the central policy server is 10.20.30.123.

```cf3
bundle agent update
{
vars:

 "master_location" string => "/var/cfengine/masterfiles";

 "policy_server"   string => "10.20.30.123";
                   comment => "IP address to locate your policy host.";

files:

  "$(sys.workdir)/inputs"

    perms => system("600"),
    copy_from => remote_cp("$(master_location)",$(policy_server)),
    depth_search => recurse("inf"); # This ensures recursive copying of all subdirectories

  "$(sys.workdir)/bin"

    perms => system("700"),
    copy_from => remote_cp("/usr/local/sbin","localhost"),
    depth_search => recurse("inf"); # This ensures recursive copying of all subdirectories
}
```

In addition the server needs to grant access to the clients, this is done in the `body server control`:

```cf3
body server control

{
allowconnects         => { "127.0.0.1" , "10.20.30.0/24" };
allowallconnects      => { "127.0.0.1" , "10.20.30.0/24" };
trustkeysfrom         => { "127.0.0.1" , "10.20.30.0/24" };
}
```

Since we assume that all hosts are on network 10.20.30.* they will be granted access. In the default policy this is set to `$(sys.policy_hub)/16`, i.e. all hosts in the same class B network as the hub will gain access. You will need to modify the access control list in `body server control` if you have clients outside of the policy server's class B network.

Granting access to files and folders needs to be done in `bundle server access_rules()`:

```cf3
bundle server access_rules()
{
access:

 10_20_30_123::

  "/var/cfengine/masterfiles"

    admit   => { "127.0.0.1", "10.20.30.0/24" };
}

```
