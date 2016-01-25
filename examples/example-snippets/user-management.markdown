---
layout: default
title: User Management Examples
published: true
sorting: 15
tags: [Examples,User Management]
---

## Local user management

There are many approaches to managing users. You can edit system files
like `/etc/passwd` directly, you can use commands on some systems like
`useradd`.  However the easiest, and preferred way is to use
CFEngine's native `users` type promise.

### Ensuring a local user has a specific password

This example shows ensuring that the local users `root` is managed if
there is a specific password hash defined.

[%CFEngine_include_example(local_user_password.cf)%]

```console
root@debian-jessie:/core/examples# grep root /etc/shadow
root:!:16791:0:99999:7:::
root@debian-jessie:/core/examples# cf-agent -KIf ./local_user_password.cf
    info: User promise repaired
root@debian-jessie:/core/examples# grep root /etc/shadow
root:$6$1nRTeNoE$DpBSe.eDsuZaME0EydXBEf.DAwuzpSoIJhkhiIAPgRqVKlmI55EONfvjZorkxNQvK2VFfMm9txx93r2bma/4h/:16791:0:99999:7:::
```
### Ensuring local users are present

This example shows ensuring that the local users `jack` and `jill` are
present on all linux systems using the native `users` type promise.

[%CFEngine_include_example(local_users_present.cf)%]

Lets check the environment to see that the users do not currently
exist.

```console
root@debian-jessie:/CFEngine/core/examples# egrep "jack|jill" /etc/passwd
root@debian-jessie:/core/examples# ls -al /home/{jack,jill}
ls: cannot access /home/jack: No such file or directory
ls: cannot access /home/jill: No such file or directory
```

Let's run the policy and inspect the state of the system afterwards.

```console
root@debian-jessie:/core/examples# cf-agent -KIf ./users_present.cf
    info: Created directory '/home/jack/.'
    info: Copying from 'localhost:/etc/skel/.bashrc'
    info: Copying from 'localhost:/etc/skel/.profile'
    info: Copying from 'localhost:/etc/skel/.bash_logout'
    info: User promise repaired
    info: Created directory '/home/jill/.'
    info: Copying from 'localhost:/etc/skel/.bashrc'
    info: Copying from 'localhost:/etc/skel/.profile'
    info: Copying from 'localhost:/etc/skel/.bash_logout'
    info: User promise repaired
root@debian-jessie:/core/examples# egrep "jack|jill" /etc/passwd
jack:x:1001:1001::/home/jack:/bin/sh
jill:x:1002:1002::/home/jill:/bin/sh
root@debian-jessie:/core/examples# ls -al /home/{jack,jill}
/home/jack:
total 20
drwxr-xr-x 2 root root 4096 Dec 22 16:37 .
drwxr-xr-x 5 root root 4096 Dec 22 16:37 ..
-rw-r--r-- 1 root root  220 Dec 22 16:37 .bash_logout
-rw-r--r-- 1 root root 3515 Dec 22 16:37 .bashrc
-rw-r--r-- 1 root root  675 Dec 22 16:37 .profile

/home/jill:
total 20
drwxr-xr-x 2 root root 4096 Dec 22 16:37 .
drwxr-xr-x 5 root root 4096 Dec 22 16:37 ..
-rw-r--r-- 1 root root  220 Dec 22 16:37 .bash_logout
-rw-r--r-- 1 root root 3515 Dec 22 16:37 .bashrc
-rw-r--r-- 1 root root  675 Dec 22 16:37 .profile
```

### Ensuring local users are locked

This example shows ensuring that the local users `jack` and `jill` are
locked if they are present on linux systems using the native `users`
type promise.

[%CFEngine_include_example(local_users_locked.cf)%]

This output shows the state of the `/etc/shadow` file before running
the example policy:

```console
root@debian-jessie:/core/examples# egrep "jack|jill" /etc/shadow
jack:x:16791:0:99999:7:::
jill:x:16791:0:99999:7:::
root@debian-jessie:/core/examples# cf-agent -KIf ./local_users_locked.cf
    info: User promise repaired
    info: User promise repaired
root@debian-jessie:/core/examples# egrep "jack|jill" /etc/shadow
jack:!x:16791:0:99999:7::1:
jill:!x:16791:0:99999:7::1:
```

### Ensuring local users are absent

This example shows ensuring that the local users `jack` and `jill` are
absent on linux systems using the native `users` type promise.

[%CFEngine_include_example(local_users_absent.cf)%]


Before activating the example policy, lets inspect the current state
of the system.

```console
root@debian-jessie:/core/examples# egrep "jack|jill" /etc/passwd
jack:x:1001:1001::/home/jack:/bin/sh
jill:x:1002:1002::/home/jill:/bin/sh
root@debian-jessie:/core/examples# ls -al /home/{jack,jill}
/home/jack:
total 20
drwxr-xr-x 2 root root 4096 Dec 22 16:37 .
drwxr-xr-x 5 root root 4096 Dec 22 16:37 ..
-rw-r--r-- 1 root root  220 Dec 22 16:37 .bash_logout
-rw-r--r-- 1 root root 3515 Dec 22 16:37 .bashrc
-rw-r--r-- 1 root root  675 Dec 22 16:37 .profile

/home/jill:
total 20
drwxr-xr-x 2 root root 4096 Dec 22 16:37 .
drwxr-xr-x 5 root root 4096 Dec 22 16:37 ..
-rw-r--r-- 1 root root  220 Dec 22 16:37 .bash_logout
-rw-r--r-- 1 root root 3515 Dec 22 16:37 .bashrc
-rw-r--r-- 1 root root  675 Dec 22 16:37 .profile
```

From the above output we can see that the local users `jack` and
`jill` are present, and that they both have home directories.

Now lets activate the example policy and insepect the result.

```console
root@debian-jessie:/core/examples# cf-agent -KIf ./local_users_absent.cf
    info: User promise repaired
    info: User promise repaired
root@debian-jessie:/core/examples# egrep "jack|jill" /etc/passwd
root@debian-jessie:/core/examples# ls -al /home/{jack,jill}
/home/jack:
total 20
drwxr-xr-x 2 root root 4096 Dec 22 16:37 .
drwxr-xr-x 5 root root 4096 Dec 22 16:37 ..
-rw-r--r-- 1 root root  220 Dec 22 16:37 .bash_logout
-rw-r--r-- 1 root root 3515 Dec 22 16:37 .bashrc
-rw-r--r-- 1 root root  675 Dec 22 16:37 .profile

/home/jill:
total 20
drwxr-xr-x 2 root root 4096 Dec 22 16:37 .
drwxr-xr-x 5 root root 4096 Dec 22 16:37 ..
-rw-r--r-- 1 root root  220 Dec 22 16:37 .bash_logout
-rw-r--r-- 1 root root 3515 Dec 22 16:37 .bashrc
-rw-r--r-- 1 root root  675 Dec 22 16:37 .profile
```

From the above output we can see that the local users `jack` and
`jill` were removed from the system as desired. Note that their home
directories remain, and if we wanted them to be purged we would have
to have a separate promise to perform that cleanup.

## Local group management

CFEngine does not currently have a native `groups` type promsie so you
will need to either edit the necessary files using `files` type
promises, or arrange for the proper commands to be run in order to
create or delete groups.

### Ensure a local group is present

Add lines to the password file, and users to group if they are not
already there.

This example uses the native operating system commands to show
ensuring that a group is present.

[%CFEngine_include_example(local_group_present.cf)%]

First lets inspect the current state of the system.

```console
root@debian-jessie:/core/examples# grep cfengineers /etc/group
```

Now lets activate the example policy and check the resulting state of
the system.

```console
root@debian-jessie:/core/examples# cf-agent -KIf ./local_group_present.cf
    info: Executing 'no timeout' ... '/usr/sbin/groupadd cfengineers'
    info: Completed execution of '/usr/sbin/groupadd cfengineers'
root@debian-jessie:/CFEngine/core2.git/examples# grep cfengineers /etc/group
cfengineers:x:1001:
```

### Ensureing a user is a member of a secondary group

This example shows using the native `users` type promise to ensure
that a user is a member of a particular group.

[%CFEngine_include_example(local_user_secondary_group_member.cf)%]

First lets inspect the current state of the system

```console
root@debian-jessie:/core/examples# grep jill /etc/passwd
root@debian-jessie:/core/examples# grep jill /etc/group
```

Now lets actiavte the example policy and inspect the resulting state.

```console
root@debian-jessie:/core/examples# cf-agent -KIf ./local_user_secondary_group_member.cf
    info: User promise repaired
root@debian-jessie:/core/examples# grep jill /etc/passwd
jill:x:1001:1002::/home/jill:/bin/sh
root@debian-jessie:/core/examples# grep jill /etc/group
cfengineers:x:1001:jill
jill:x:1002:
```

It's important to remember we made no promise about the presence of
the `cfengineers` group in the above example. We can see what would
happen when the `cfengineers` group was not present.

```console
root@debian-jessie:/core/examples# grep cfengineers /etc/group
root@debian-jessie:/core/examples# cf-agent -KIf ./local_user_secondary_group_member.cf
usermod: group 'cfengineers' does not exist
   error: Command returned error while modifying user 'jill'. (Command line: '/usr/sbin/usermod -G "cfengineers" jill')
    info: User promise not kept
```

## Get a list of users

[%CFEngine_include_snippet(get_a_list_of_users.cf, .* )%]

