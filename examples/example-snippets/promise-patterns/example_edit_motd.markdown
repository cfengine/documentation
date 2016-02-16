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

Here is the mustache:

{% raw %}
[%CFEngine_include_example(mustache_template_motd.cf.mustache)%]
{% endraw %}

Example run:

```console
root@debian8:~/core/examples# cf-agent --no-lock --bundlesequence motd --define DEBUG_motd --file ./mustache_template_motd.cf
    info: Using command line specified bundlesequence
R: 3.7.2 is the detected version
R: debian8 is the detected hostname
R: 10.100.251.53 is the ipv4 address for debian8
R: Policy Client is the detected role for debian8
R: 20 packages can be updated
R: This host is managed by root@localhost
root@debian8:~/core/examples# cat /etc/motd
 WARNING Environment Unknown
      ¤¤¤
      ¤¤¤
      ¤¤¤	 Welcome into debian8

    ¤ ¤¤¤ ¤      This system is controlled by
    ¤ ¤¤¤ ¤      CFEngine 3.8.0
    ¤ ¤¤¤ ¤	 And is a Policy Client
    ¤     ¤
      ¤¤¤
      ¤ ¤	
      ¤ ¤	 Host IP 10.100.251.53
      ¤ ¤	 20 package updates available.
                 Support Contact:
                   - root@localhost
```
