---
layout: default
title: Manage local users
published: true
sorting: 3
tags: [getting started, tutorial]
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/23QHpDEvYU8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In this tutorial we will show how to use CFEngine to manage users, add them to
groups, setup their home directory and copy ssh-keys to their `~/.ssh` directory
as part of creating the user.

1. Create some files and groups that we will use

Create the files `id_rsa` and `id_rsa.pub` in `/tmp`.

```console
# touch /tmp/id_rsa /tmp/id_rsa.pub
```

Create user group security and webadmin.

```console
# sudo groupadd security 
# sudo groupadd webadmin
```

2. Create CFEngine policy called `users.cf`

Create a file `/tmp/users.cf` with the following content:

```cf3
body common control
{
  inputs => { "$(sys.libdir)/stdlib.cf" };
}

bundle agent main
{
  vars:
  "users" slist => { "adam", "eva" };
  users:
    "$(users)"
    policy => "present",
    home_dir => "/home/$(users)",
    group_primary => "users",
    groups_secondary => { "security", "webadmin" },
    shell => "/bin/bash/",
    home_bundle => setup_home_dir("$(users)");
}

bundle agent setup_home_dir(user)
{
  vars:
    "keys" slist => { "id_rsa", "id_rsa.pub" };
  files:
    "/home/$(user)/." create => "true";
    "/home/$(user)/.ssh/." create => "true";
    "/home/$(user)/.ssh/$(keys)" copy_from => local_cp("/tmp/$(keys)");
}
```

3. Test it out, and verify the result

Run CFEngine:

```console
# /var/cfengine/bin/cf-agent -fK /tmp/users.cf
```

Verify the result: Have users have been created?

```console
# grep -P "adam|eva" /etc/passwd
```

Congratulations! You should now see the users adam and eva listed.

Verify the result: Have users home directory have been created?

```console
# ls /home | grep -P "adam|eva"
```

Congratulations! You should now see adam and eva listed.

Verify the result: Have users have been added to the correct groups?

```console
# grep -P "adam|eva" /etc/group
```

Congratulations! You should now see adam and eva added to the groups security
and webadmin. **NOTE:** CFEngine's users type promise will not create groups, so
you must make sure the groups exists.

Verify the result: Have ssh-keys have been copied from `/tmp` to user’s `~/.ssh`
directory?

```console
# ls /home/adam/.ssh /home/eva/.ssh
```

Congratulations! You should now see the files `id_rsa` and `id_rsa.pub`.

Ps. If you would like play around with the policy, delete the users after each run with the command

```console
# deluser -r username
```

Mission accomplished!

