---
layout: default
title: Customize Message of the Day
published: true
tags: [Examples, Policy, motd, file editing, files]
reviewed: 2015-12-18
reviewed-by: enrico & nick
---

The Message of the Day is displayed when you log in or connect to a server. It
typically shows information about the operating system, license information,
last login, etc.

It is often useful to customize the Message of the Day to inform your users
about some specifics of the system they are connecting to. In this example we
render a `/etc/motd` using a mustache template and add useful information as:

* The role of the server ( staging / production )
* The hostname of the server
* The CFEngine version we are running on the host
* The CFEngine role of the server ( client / hub )
* The administrative contacts details conditionally to the environment
* The primary Ipv4 IP address
* The number of packages updates available for this host

The bundle is defined like this:

[%CFEngine_include_example(mustache_template_motd.cf)%]

**Example run:**

```console
root@debian8:~/core/examples# cf-agent -KIf ./mustache_template_motd.cf; cat /etc/motd
    info: Updated rendering of '/etc/motd' from mustache template 'inline'
    info: files promise '/etc/motd' repaired
# Managed by CFEngine
WARNING: Environment unknown (missing environment semaphores)
  ***
  ***    Welcome to nickanderson-thinkpad-w550s
  ***

* *** *      CFEngine Role: Policy Client
* *** *      CFEngine Version:3.17.0
* *** *
*     *      Host IP: 192.168.42.189
  ***        No package updates available or status unknown.
  * *
  * *
  * *
             For support contact:
               - root@localhost
```
