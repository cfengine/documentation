---
layout: default
title: Manage processes and services
published: true
sorting: 3
tags: [getting started, tutorial]
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/cAMKemZ6A9w" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Ensuring a particular process is running on a system is a common task for a
system administrator, as processes are what provide all services available on a
computer system.

Using CFEngine to ensure certain processes are running is extremely easy.

1. Create the policy

Create a new file called `ensure_process.cf`:

```cf3
body file control
{
      inputs => { "$(sys.libdir)/stdlib.cf" };
}

bundle agent main
{
  processes:
      "/usr/sbin/ntpd"
        restart_class => "ntpd_not_running";

  commands:
    ntpd_not_running::
      "/etc/init.d/ntp start";
}
```

This example is designed to be run on an Ubuntu 12.04 system, and assumes the ntp package is already installed).

Let us quickly explain this code:

The `body file control` construct, which instructs CFEngine to load the CFEngine
standard library.

The `processes:` tells cf-agent that the promises are related to
processes. Then a promise checks for the existence of a running process whose
name matches the string `/usr/sbin/ntpd`. If the process is found, nothing
happens. But if it is not found, the `ntpd_not_running` class (a class is a named
boolean attribute in the CFEngine policy language which can be used for decision
making) will be defined.

Finally, the `commands:` line tells cf-agent that the following promises are
related to executing commands. The `ntpd_not_running::` line restricts the context
to so that the following commands will only be run if the expression evaluates
to true.

2. Testing the policy

First, we verify that the ntpd process is not running:

```console
# ps axuww | grep ntp
```

Then we run our CFEngine policy:


```console
# cf-agent -f ./ensure_process.cf
2014-03-20T06:33:56+0000   notice: /default/main/commands/'/etc/init.d/ntp start'[0]: Q: "...init.d/ntp star":  * Starting NTP server ntpd
Q: "...init.d/ntp star":    ...done.
```

Finally, we verify that ntpd is now running on the system:


```console
# ps axuww | grep ntp
ntp       5756  0.3  0.1  37696  2172 ?        Ss   06:33   0:00 /usr/sbin/ntpd -p /var/run/ntpd.pid -g -u 104:110
```

Congratulations!

That’s it! Every time CFEngine runs the policy, it will check for the process,
and if it’s not there, will start it. This is how CFEngine maintains your system
in the correct, desired state.

