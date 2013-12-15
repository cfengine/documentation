---
layout: default
title: getusers
categories: [Reference, Functions, getusers]
published: true
alias: reference-functions-getusers.html
tags: [reference, system functions, functions, getusers]
---

[%CFEngine_function_prototype(exclude_names, exclude_ids)%]

**Description:** Returns a list of all users defined, except those names in `exclude_names` and uids in `exclude_ids`

[%CFEngine_function_attributes(exclude_names, exclude_ids)%]

**Example:**

```cf3
body common control
{
      bundlesequence => { "example" };
}

bundle agent example
{
  vars:
      "allusers" slist => getusers("zenoss,mysql,at","12,0");

  reports:
      "Found user $(allusers)";
}
```

Output:

```
R: Found user daemon
R: Found user bin
R: Found user sys
R: Found user sync
R: Found user games
R: Found user man
R: Found user lp
R: Found user mail
R: Found user news
R: Found user uucp
R: Found user proxy
R: Found user www-data
R: Found user backup
R: Found user list
R: Found user irc
R: Found user gnats
R: Found user nobody
R: Found user libuuid
R: Found user Debian-exim
R: Found user statd
R: Found user sshd
R: Found user tero
R: Found user messagebus
R: Found user minecraft
R: Found user nagios
R: Found user colord
R: Found user libvirt-qemu
R: Found user saned
R: Found user vde2-net
R: Found user mark
```

**Notes:**
This function is currently only available on Unix-like systems.

**History:** Was introduced in version 3.1.0b1,Nova 2.0.0b1 (2010).

