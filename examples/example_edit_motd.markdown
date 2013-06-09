---
layout: default
title: Customize Message of the Day
categories: [Examples, Customize Message of the Day]
published: true
alias: examples-customize-message-of-the-day.html
tags: [Examples, motd, file editing, files]
reviewed: 2013-06-08
reviewed-by: atsaloli
---

The Message of the Day is displayed when you log in or connect to a server. It typically shows information about the operating system, license information, last login, etc.

It is often useful to customize the Message of the Day to inform your users about some specifics of the system they are connecting to. In this example we will look at a bundle which adds three lines to the `/etc/motd` file to inform about some system characteristics and that the system is managed by CFEngine.

The bundle is defined like this:

```cf3
body common control
{
bundlesequence => { "edit_motd" };
inputs => { "libraries/cfengine_stdlib.cf" };
}

bundle agent edit_motd
{
files:
  "/tmp/motd"   # This is for testing, replace with "/etc/motd" to put in production
    edit_line     => my_motd,  # The bundle my_motd details what content we want
                               # in the file using CFEngine's built-in line-editor
    edit_defaults => empty,    # Baseline memory model of file to zero/empty before 
                               # populating the model using edit_line my_motd 
    create        => "true";   # Create the file if it does not exist
}

# Describe the content we want
bundle edit_line my_motd
{
vars:
  "interfaces_str"  string => join(", ","sys.interfaces");  # convert array to string
  "ipaddresses_str" string => join(", ","sys.ip_addresses"); 

insert_lines:
  "Welcome to $(sys.fqhost)!
This system is managed by CFEngine.
The policy was last updated on $(sys.last_policy_update).
The system has $(sys.cpus) cpus.
Network interfaces on this system are $(interfaces_str),
and the ip-addresses assigned are $(ipaddresses_str).";
}

body edit_defaults empty
{
empty_file_before_editing => "true";
} 
```

You can find this bundle in the file `/var/cfengine/share/doc/examples/motd.cf`

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
