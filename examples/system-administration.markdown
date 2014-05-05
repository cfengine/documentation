---
layout: default
title: System Administration Examples 
published: true
sorting: 12
tags: [Examples][System Administration]
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
## Manage a system process ##
## Ensure running ##
## Ensure not running ##
## Prune processes ##
## Set up HPC clusters ##
## Set up name resolution ##
## Set up sudo ##
## Environments (virtual) ##
## Environment variables ##
## Tidying garbage files ##