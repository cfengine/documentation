---
layout: default
title: Ensure a service is enabled and running
published: true
tags: [examples, services]
reviewed: 2016-06-28
reviewed-by: nickanderson
---

This example shows how to ensure services are started or stopped appropriately.

[%CFEngine_include_example(services.cf)%]

**Note:** Not all services behave in the standard way. Some services may require
custom handling. For example it is not uncommon for some services to not provide
correct return codes for status checks.

**See Also:**

* [Services promise type reference][services]
* [Services bundles and bodies in the standard library][lib/services.cf]

## Example usage on systemd

We can see that before the policy run `sysstat` is *inactive*, `apache2` is
*active*, `cups` is *active*, `ssh` is *active* and `cron` is *inactive*.

```console
root@ubuntu:# systemctl is-active sysstat apache2 cups ssh cron
inactive
active
active
active
inactive
```

Now we run the policy to converge the system to the desired state.

```console
root@ubuntu:# cf-agent --no-lock --inform --file ./services.cf
    info: Executing 'no timeout' ... '/bin/systemctl --no-ask-password --global --system -q stop apache2'
    info: Completed execution of '/bin/systemctl --no-ask-password --global --system -q stop apache2'
    info: Executing 'no timeout' ... '/bin/systemctl --no-ask-password --global --system -q stop cups'
    info: Completed execution of '/bin/systemctl --no-ask-password --global --system -q stop cups'
    info: Executing 'no timeout' ... '/bin/systemctl --no-ask-password --global --system -q start cron'
    info: Completed execution of '/bin/systemctl --no-ask-password --global --system -q start cron'
```

After the policy run we can see that `systat`, `apache2`, and `cups` are
*inactive*. `ssh` and `cron` are *active* as specified in the policy.

```console
root@ubuntu:/home/nickanderson/CFEngine/core/examples# systemctl is-active sysstat apache2 cups ssh cron
inactive
inactive
inactive
active
active
```

## Example usage with System V

We can see that before the policy run `sysstat` is not reporting status
correctly , `httpd` is *running*, `cups` is *running*, `sshd` is *running* and
`crond` is *not running*.

```console
[root@localhost examples]# service sysstat status; echo $?
3
[root@localhost examples]# service httpd status; echo $?
httpd (pid  3740) is running...
0
[root@localhost examples]# service cups status; echo $?
cupsd (pid  3762) is running...
0
[root@localhost examples]# service sshd status; echo $?
openssh-daemon (pid  3794) is running...
0
[root@localhost examples]# service crond status; echo $?
crond is stopped
3
```

Now we run the policy to converge the system to the desired state.

```console
[root@localhost examples]# cf-agent -KIf ./services.cf
    info: Executing 'no timeout' ... '/etc/init.d/crond start'
    info: Completed execution of '/etc/init.d/crond start'
    info: Executing 'no timeout' ... '/etc/init.d/httpd stop'
    info: Completed execution of '/etc/init.d/httpd stop'
    info: Executing 'no timeout' ... '/etc/init.d/cups stop'
    info: Completed execution of '/etc/init.d/cups stop'
```

After the policy run we can see that `systat` is still not reporting status correctly (some services do not respond to standard checks), `apache2`, and `cups` are
*inactive*. `ssh` and `cron` are *active* as specified in the policy.


```console
[root@localhost examples]# service sysstat status; echo $?
3
[root@localhost examples]# service httpd status; echo $?
httpd is stopped
3
[root@localhost examples]# service cups status; echo $?
cupsd is stopped
3
[root@localhost examples]# service sshd status; echo $?
openssh-daemon (pid  3794) is running...
0
[root@localhost examples]# service crond status; echo $?
crond (pid  3929) is running...
0
```
