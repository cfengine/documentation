---
layout: default
title: Network examples
sorting: 9
---

- [Find MAC address][Network examples#Find MAC address]
- [Client-server example][Network examples#Client-server example]
- [Read from a TCP socket][Network examples#Read from a TCP socket]
- [Set up a PXE boot server][Network examples#Set up a PXE boot server]
- [Resolver management][Network examples#Resolver management]
- [Mount NFS filesystem][Network examples#Mount NFS filesystem]
- [Unmount NFS filesystem][Network examples#Unmount NFS filesystem]
- Find the MAC address
- Mount NFS filesystem

## Find MAC address

Finding the ethernet address can be hard, but on Linux it is straightforward.

{{< CFEngine_include_snippet(find_mac_address.cf, .* ) >}}

## Client-server example

{{< CFEngine_include_snippet(client-server_example.cf, .* ) >}}

## Read from a TCP socket

{{< CFEngine_include_snippet(read_from_a_tcp_socket.cf, .* ) >}}

## Set up a PXE boot server

Use CFEngine to set up a PXE boot server.

{{< CFEngine_include_snippet(set_up_a_pxe_boot_server.cf, .* ) >}}

## Resolver management

{{< CFEngine_include_snippet(resolver_management.cf, .* ) >}}

## Mount NFS filesystem

{{< CFEngine_include_snippet(mount_nfs_filesystem.cf, .* ) >}}

## Unmount NFS filesystem

{{< CFEngine_include_snippet(unmount_nfs_filesystem.cf, .* ) >}}
