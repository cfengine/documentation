---
layout: default
title: System Administration Examples
published: true
sorting: 12
tags: [Examples,System Administration]
---

* [Centralized Management][System Administration Examples#Centralized Management]
	* [All hosts the same][System Administration Examples#All hosts the same]
	* [Variation in hosts][System Administration Examples#Variation in hosts]
	* [Updating from a central hub][System Administration Examples#Updating from a central hub]
* [Laptop support configuration][System Administration Examples#Laptop support configuration]
* [Process management][System Administration Examples#Process management]
* [Kill process][System Administration Examples#Kill process]
* [Restart process][System Administration Examples#Restart process]
* [Mount a filesystem][System Administration Examples#Mount a filesystem]
* [Manage a system process][System Administration Examples#Manage a system process]
	* [Ensure running][System Administration Examples#Ensure running]
	* [Ensure not running][System Administration Examples#Ensure not running]
	* [Prune processes][System Administration Examples#Prune processes]
* [Set up HPC clusters][System Administration Examples#Set up HPC clusters]
* [Set up name resolution][System Administration Examples#Set up name resolution]
* [Set up sudo][System Administration Examples#Set up sudo]
* [Environments (virtual)][System Administration Examples#Environments (virtual)]
* [Environment variables][System Administration Examples#Environment variables]
* [Tidying garbage files][System Administration Examples#Tidying garbage files]

## Centralized Management

These examples show a simple setup for starting with a central approach to management of servers. Centralization of management is a simple approach suitable for small environments with few requirements. It is useful for clusters where systems are all alike.

    All hosts the same
    Variation in hosts
    Updating from a central hub

### All hosts the same

This shows the simplest approach in which all hosts are the same. It is too simple for most environments, but it serves as a starting point. Compare it to the next section that includes variation.


[%CFEngine_include_snippet(all_hosts_the_same.cf, .* )%]

### Variation in hosts


[%CFEngine_include_snippet(variation_in_hosts.cf, .* )%]

### Updating from a central hub

The configuration bundled with the CFEngine source code contains an example of centralized updating of policy that covers more subtleties than this example, and handles fault tolerance. Here is the main idea behind it. For simplicity, we assume that all hosts are on network 10.20.30.* and that the central policy server/hub is 10.20.30.123.


[%CFEngine_include_snippet(updating_from_a_central_hub.cf, .* )%]

## Laptop support configuration

Laptops do not need a lot of confguration support. IP addresses are set by DHCP and conditions are changeable. But you want to set your DNS search domains to familiar settings in spite of local DHCP configuration, and another useful trick is to keep a regular backup of disk changes on the local disk. This won't help against disk destruction, but it is a huge advantage when your user accidentally deletes files while travelling or offline.


[%CFEngine_include_snippet(laptop_support_configuration.cf, .* )%]

## Process management

	
[%CFEngine_include_snippet(process_management.cf, .* )%]

## Kill process ##


[%CFEngine_include_snippet(kill_process.cf, .* )%]

## Restart process ##

A basic pattern for restarting processes:


[%CFEngine_include_snippet(restart_process.cf, .* )%]

This can be made more sophisticated to handle generic lists:

[%CFEngine_include_snippet(restart_process_1.cf, .* )%]

Why? Separating this into two parts gives a high level of control and conistency to CFEngine. There are many options for command execution, like the ability to run commands in a sandbox or as `setuid'. These should not be reproduced in processes.

## Mount a filesystem ##


[%CFEngine_include_snippet(mount_a_filesystem.cf, .* )%]


## Manage a system process

    Ensure running
    Ensure not running
    Prune processes

### Ensure running

The simplest example might look like this:


[%CFEngine_include_snippet(ensure_running.cf, .* )%]

This example shows how the CFEngine components could be started using a pattern.


[%CFEngine_include_snippet(ensure_running_1.cf, .* )%]

### Ensure not running


[%CFEngine_include_snippet(ensure_not_running.cf, .* )%]

### Prune processes

This example kills processes owned by a particular user that have exceeded 100000 bytes of resident memory.


[%CFEngine_include_snippet(prune_processes.cf, .* )%]

## Set up HPC clusters

HPC cluster machines are usually all identical, so the CFEngine configuration is very simple. HPC clients value CPU and memory resources, so we can shut down unnecessary services to save CPU. We can also change the scheduling rate of CFEngine to run less frequently, and save a little:


[%CFEngine_include_snippet(set_up_hpc_clusters.cf, .* )%]

## Set up name resolution

There are many ways to do name resolution setup1 We write a reusable bundle using the editing features.

A simple and straightforward approach is to maintain a separate modular bundle for this task. This avoids too many levels of abstraction and keeps all the information in one place. We implement this as a simple editing promise for the /etc/resolv.conf file.


[%CFEngine_include_snippet(set_up_name_resolution.cf, .* )%]

A second approach is to try to conceal the operational details behind a veil of abstraction.


[%CFEngine_include_snippet(set_up_name_resolution_1.cf, .* )%]

DNS is not the only name service, of course. Unix has its older /etc/hosts file which can also be managed using file editing. We simply append this to the system_files bundle.


[%CFEngine_include_snippet(set_up_name_resolution_1.cf, .* )%]

## Set up sudo

Setting up sudo is straightforward, and is best managed by copying trusted files from a repository.


[%CFEngine_include_snippet(set_up_sudo.cf, .* )%]

## Environments (virtual)


[%CFEngine_include_snippet(environments_(virtual).cf, .* )%]

## Environment variables


[%CFEngine_include_snippet(environment_variables.cf, .* )%]

## Tidying garbage files

Emulating the `tidy' feature of CFEngine 2.

[%CFEngine_include_snippet(tidying_garbage_files.cf, .* )%]
