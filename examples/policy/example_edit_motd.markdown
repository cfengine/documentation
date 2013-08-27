---
layout: default
title: Customize Message of the Day
categories: [Examples, Policy, Customize Message of the Day]
published: true
alias: examples-policy-customize-message-of-the-day.html
tags: [Examples, Policy, motd, file editing, files]
reviewed: 2013-06-08
reviewed-by: atsaloli
---

The Message of the Day is displayed when you log in or connect to a server. It typically shows information about the operating system, license information, last login, etc.

It is often useful to customize the Message of the Day to inform your users about some specifics of the system they are connecting to. In this example we will look at a bundle which adds three lines to the `/etc/motd` file to inform about some system characteristics and that the system is managed by CFEngine.

The bundle is defined like this:

[%CFEngine_include_example(motd.cf)%]

Example run:

```
# ls /tmp/motd
ls: cannot access /tmp/motd: No such file or directory
# cf-agent -f motd.cf
# cat /tmp/motd
Welcome to tashkent!
This system is managed by CFEngine.
The policy was last updated on Sat Jun  8 15:16:00 2013.
The system has 4 cpus.
Network interfaces on this system are eth0, eth1,
and the ip-addresses assigned are 127.0.0.1, 10.10.23.68, 192.168.183.208.
# 
```
