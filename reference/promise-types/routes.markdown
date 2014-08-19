---
layout: default
title: routes
published: true
tags: [reference, bundle agent, routes, promises, promise types, networking, Cumulus]
---


Routes promises are for defining pathways to known IP network addresses
via local interfaces.

A routing promise tells a host that it can reach network destinations along
certain IP configured interfaces. Interface configuration is thus a pre-requisite.
(A static route is not the same as a routing service (like OSPF or BGP) which advertises
and distributes route information. Routes are held by each device in order to know
which of its interfaces it should use to forward data to destination.)

The promiser is a network address, written in CIDR notation, or the general
wildcard "default" (0.0.0.0/32). 

**Example:**

```cf3
bundle agent main()
{
routes:

  "default"
     reachable_through => gateway("199.243.22.4", "eth0");

  "10.11.12.0/23"
     reachable_through => gateway("128.39.73.1", "eth1");

}

body reachable_through gateway(gw,if)
{
gateway_ip => "$(gw)";
gateway_interface => "$(if)";
}
```

### Attributes ###

### reachable_through
**Description:** A body assigning a forwarding agent (body)
**Type:** `body reachable_through`

#### gateway_ip
**Allowed input range:** 
**Description:** IP address on gateway to next hop 
**Type:** `IP address` without CIDR netmask

#### gateway_interface
**Allowed input range:** 
**Description:** Interface name of gateway to next hop
**Type:** `string`

#### delete_route
**Allowed input range:**  true/false
**Description:** If this route exists, remove it
**Type:** `boolean`


