---
layout: default
title: Network Examples 
published: true
sorting: 9
tags: [Examples]
---

* [Find MAC address][Network Examples#Find MAC address]
* [Client-server example][Network Examples#Client-server example]
* [Read from a TCP socket][Network Examples#Read from a TCP socket]
* [Set up a PXE boot server][Network Examples#Set up a PXE boot server]
* [Resolver management][Network Examples#Resolver management]
* [Mount NFS filesystem][Network Examples#Mount NFS filesystem]
* [Unmount NFS filesystem][Network Examples#Unmount NFS filesystem]
* Find the MAC address
* Mount NFS filesystem

## Find MAC address

Finding the ethernet address can be hard, but on Linux it is straightforward.


[%CFEngine_include_snippet(find_mac_address.cf, [\s]*--[a-z], ^$)%]

## Client-server example

[%CFEngine_include_snippet(client-server_example.cf, [\s]*--[a-z], ^$)%]

## Read from a TCP socket


[%CFEngine_include_snippet(read_from_a_tcp_socket.cf, [\s]*--[a-z], ^$)%]

## Set up a PXE boot server

Use CFEngine to set up a PXE boot server.


[%CFEngine_include_snippet(set_up_a_pxe_boot_server.cf, [\s]*--[a-z], ^$)%]

## Resolver management


[%CFEngine_include_snippet(resolver_management.cf, [\s]*--[a-z], ^$)%]

## Mount NFS filesystem


[%CFEngine_include_snippet(mount_nfs_filesystem.cf, [\s]*--[a-z], ^$)%]

## Unmount NFS filesystem

[%CFEngine_include_snippet(unmount_nfs_filesystem.cf, [\s]*--[a-z], ^$)%]
