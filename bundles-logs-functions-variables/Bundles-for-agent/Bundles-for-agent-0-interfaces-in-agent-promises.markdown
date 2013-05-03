---
layout: default
title: interfaces-in-agent-promises
categories: [Bundles-for-agent,interfaces-in-agent-promises]
published: true
alias: Bundles-for-agent-interfaces-in-agent-promises.html
tags: [Bundles-for-agent,interfaces-in-agent-promises]
---

### `interfaces` promises in agent

\

Interfaces promises describe the configurable aspects relating to
network interfaces. Most workstations and servers have only a single
network interface, but routers and multi-homed hosts often have multiple
interfaces. Interface promises include attributes such as the IP address
identity, assumed netmask and routing policy in the case of multi-homed
hosts. For virtual machines and hosts, the list of interfaces can be
quite large.

~~~~ {.smallexample}
     
      interfaces:
     
        "interface name"
     
          tcp_ip = tcp_ip_body,
          ...;
     
~~~~

\

For future use.

\

For future use.

-   [tcp\_ip in interfaces](#tcp_005fip-in-interfaces)

#### `tcp_ip` (body template)

**Type**: (ext body)

`ipv4_address`

**Type**: string

**Allowed input range**: `[0-9.]+/[0-4]+`

**Synopsis**: IPv4 address for the interface

**Example**:\
 \

~~~~ {.verbatim}
     
     body tcp_ip example
     {
     ipv4_address => "123.456.789.001";
     }
     
~~~~

**Notes**:\
 \

The address will be checked and if necessary set. Today few hosts will
be managed in this way. Address management will be handled by other
services like DHCP. \

`ipv4_netmask`

**Type**: string

**Allowed input range**: `[0-9.]+/[0-4]+`

**Synopsis**: Netmask for the interface

**Example**:\
 \

~~~~ {.verbatim}
     
     body tcp_ip example
     {
     ipv4_netmask => "255.255.254.0";
     }
     
~~~~

**Notes**:\
 \

In many cases the CIDR form of address will show the netmask as /23, but
this offers and \`old style' alternative. \

`ipv6_address`

**Type**: string

**Allowed input range**: `[0-9a-fA-F:]+/[0-9]+`

**Synopsis**: IPv6 address for the interface

**Example**:\
 \

~~~~ {.verbatim}
     
       "eth0"
     
          ipv6_address => "2001:700:700:3:211:63ff:feeb:5d18/64";
     
~~~~

**Notes**:\
 \
