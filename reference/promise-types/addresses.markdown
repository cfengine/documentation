---
layout: default
title: addresses
published: true
tags: [reference, bundle agent, adresses, promises, promise types, networking, Cumulus]
---


Addresses promises are used to allow a form of ARP teleportation for
layer 2 tunnelling, where address spaces do not automatically map
across the tunnel.  VxLAN is an example of this. Layer 2 MAC addresses
need to be integrated across the tunnel end-points, but require
registration.  This promise type is for mainly specialized usage.

### Attributes ###

### link_address

**Description:** The link level (MAC) address of the promiser

**Type:** `MAC address`

### delete_link

**Description:** If this link mapping exists, remove it

**Type:** `boolean`

### interface

**Description:** Interface for neighbour discovery

**Type:** `string`


## Example ##

```cf3
vars:

  #     LAN IP  LOCATION                  LAN MAC BINDING
  "arp[10.1.1.1][switch1]"    string => "00:00:10:00:00:0A";
  "arp[10.1.1.2][switch1]"    string => "00:00:10:00:00:0B";
  "arp[10.1.1.3][switch2]"    string => "00:00:10:00:00:0C";
  "arp[10.1.1.4][cflu-10004]" string => "00:00:10:00:00:0D";  
  "arp[10.1.1.5][cflu-10004]" string => "00:00:10:00:00:0E";
  "arp[10.1.1.6][switch4]"    string => "00:00:10:00:00:0F";

addresses:

   # Host ARP bindings

   "$(ip_address)"
          comment => "Teleport a static ARP binding for the VxLAN",
     link_address => "$(arp[$(ip_address)][$(sys.uqhost)])",
        interface => "eth0";
```
