---
layout: default
title: System Administration Examples 
published: true
sorting: 12
tags: [Examples,System Administration]
---

* [Centralized Management][System Administration#Centralized Management]
* [All hosts the same][System Administration#All hosts the same]
* [Variation in hosts][System Administration#Variation in hosts]
* [Updating from a central hub][System Administration#Updating from a central hub]
* [Laptop support configuration][System Administration#Laptop support configuration]
* [Process management][System Administration#Process management]
* [Kill process][CFEngine Basic Examples#Kill process]
* [Restart process][CFEngine Basic Examples#Restart process]
* [Mount a filesystem][CFEngine Basic Examples#Mount a filesystem]
* [Manage a system process][System Administration#Manage a system process]
* [Ensure running][System Administration#Ensure running]
* [Ensure not running][System Administration#Ensure not running]
* [Prune processes][System Administration#Prune processes]
* [Set up HPC clusters][System Administration#Set up HPC clusters]
* [Set up name resolution][System Administration#Set up name resolution]
* [Set up sudo][System Administration#Set up sudo]
* [Environments (virtual)][System Administration#Environments (virtual)]
* [Environment variables][System Administration#Environment variables]
* [Tidying garbage files][System Administration#Tidying garbage files]
* Customize Message of the Day
* Ensure a process is not running
* Restart a Process
* Set up sudo
* Set up time management through NTP
* Set up name resolution with DNS

## Centralized Management ##
## All hosts the same ##
## Variation in hosts ##
## Updating from a central hub ##
## Laptop support configuration ##
## Process management ##

## Kill process ##

```cf3
body common control
{
bundlesequence => { "test" };
}



bundle agent test
{
processes:

 "sleep"

   signals => { "term", "kill" };

}
```

## Restart process ##

A basic pattern for restarting processes:

```cf3
body common control
{
bundlesequence => { "process_restart" };
}

#########################################################


bundle agent process_restart
{
processes:

  "/usr/bin/daemon" 
        restart_class => "launch";

commands:

  launch::

   "/usr/bin/daemon";

}
```

This can be made more sophisticated to handle generic lists:

```cf3
body common control
{
bundlesequence => { "process_restart" };
}

#########################################################


bundle agent process_restart
{
vars:

  "component" slist => {
                       "cf-monitord", 
                       "cf-serverd", 
                       "cf-execd" 
                       };
processes:

  "$(component)" 
        restart_class => canonify("start_$(component)");

commands:

   "/var/cfengine/bin/$(component)"
       ifvarclass => canonify("start_$(component)");

}
```

Why? Separating this into two parts gives a high level of control and conistency to CFEngine. There are many options for command execution, like the ability to run commands in a sandbox or as `setuid'. These should not be reproduced in processes.

## Mount a filesystem ##

```cf3
#

# cfengine 3

#

# cf-agent -f ./cftest.cf -K

#


body common control

{
bundlesequence => { "mounts" };
}

#


bundle agent mounts

{
storage:

  "/mnt" mount  => nfs("slogans.iu.hio.no","/home");

}

######################################################################


body mount nfs(server,source)

{
mount_type => "nfs";
mount_source => "$(source)";
mount_server => "$(server)";
#mount_options => { "rw" };

edit_fstab => "true";
unmount => "true";
}
```


## Manage a system process ##
## Ensure running ##
## Ensure not running ##
## Prune processes ##
## Set up HPC clusters ##
## Set up name resolution ##
## Set up sudo ##

## Environments (virtual)

```cf3

#######################################################

#

# Virtual environments

#

#######################################################


body common control

{
bundlesequence  => { "my_vm_cloud" };   
}

#######################################################


bundle agent my_vm_cloud

{
vars:

  "vms[atlas]" slist => { "guest1", "guest2", "guest3" };

environments:

 scope||any::  # These should probably be in class "any" to ensure uniqueness

   "$(vms[$(sys.host)])"

       environment_resources => virt_xml("$(xmlfile[$(this.promiser)])"),
       environment_interface => vnet("eth0,192.168.1.100/24"),
       environment_type      => "test",
       environment_host      => "atlas";

      # default environment_state => "create" on host, and "suspended elsewhere"

}

#######################################################


body environment_resources virt_xml(specfile)
{
env_spec_file => "$(specfile)";
}

#######################################################


body environment_interface vnet(primary)
{
env_name      => "$(this.promiser)";
env_addresses => { "$(primary)" };

host1::

  env_network => "default_vnet1";

host2::

  env_network => "default_vnet2";

}
```

## Environment variables

```cf3
#######################################################

#

# Virtual environments

#

#######################################################


body common control

{
bundlesequence  => { "my_vm_cloud" };   
}

#######################################################


bundle agent my_vm_cloud

{
environments:

   "centos5"

       environment_resources => virt_xml,
       environment_type      => "xen",
       environment_host      => "ursa-minor";

      # default environment_state => "create" on host, and "suspended elsewhere"

}

#######################################################


body environment_resources virt_xml
{
env_spec_file => "/srv/xen/centos5-libvirt-create.xml";
}
```

## Tidying garbage files ##