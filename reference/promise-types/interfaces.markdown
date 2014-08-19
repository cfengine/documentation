---
layout: default
title: interfaces
published: true
tags: [reference, bundle agent, interfaces, promises, promise types, networking, Cumulus]
---

Interface promises are used to set physical link settings (like duplex,
data rate etc), addresses, make bridges, bonds (aggregate interfaces)
and to establish peering services for route advertisement.

An interface promise has the form

```cf3
interfaces:

   "eth0"
       attributes => values;

```

Interfaces can be physical (such as network interfaces eth0, lm0,
swp1, wlan0 etc) or virtual (such as loopbacks, bridges and tunnel
end-points, lo0, tun0, br0, eth0.1), etc.
  

***

## Attributes ##

[%CFEngine_include_markdown(common-attributes-include.markdown)%]


### bridge_interfaces 
**Allowed input range:**
**Description:** List of interfaces to bridge with IP forwarding
**Type:** `list of strings`

### bond_interfaces 
**Allowed input range:**
**Description:** List of interfaces to bond with LACP
**Type:** `list of strings`

### delete 
**Allowed input range:** true/false
**Description:** Delete an interface or bridge altogether
**Type:** `boolean`

### tagged_vlans 
**Allowed input range:**
**Description:** List of labelled (trunk) vlan identifers for this interface
**Type:** `list of strings/ints`

### untagged_vlan 
**Allowed input range:**
**Description:** Unlabelled (access) vlan
**Type:** `string/int`

### ipv4_addresses 
**Allowed input range:**
**Description:** A static IPV4 address
**Type:** `list of strings` in CIDR format

### ipv6_addresses 
**Allowed input range:**
**Description:** A static IPV6 address
**Type:** `list of strings` in CIDR format

### purge_addresses 
**Allowed input range:**
**Description:** Remove existing addresses from interface if not defined her
**Type:** `boolean`


### link_state 
**Description:** The desired state of the interface link (body) 
**Type:** `body link_state`
 
#### bonding 
**Allowed input range:** balance-rr,active-backup,balance-xor,broadcast,802.3ad,balance-tlb,balance-alb
**Description:** The Link Aggregation Control Protocol is enabled to bond interfaces in a number of different modes
**Type:** `string`

#### manager 
**Allowed input range:** cfengine,native,nativefirst
**Description:** Which source of configuration is considered authoritative?
**Type:** `string`

#### state 
              Values: 
**Allowed input range:** up,downStatus of interface
**Description:** 
**Type:** `list of strings`

#### duplex
**Allowed input range:** half,full
**Description:** Duplex wiring configuration
**Type:** `string`

#### auto_negotiation
**Allowed input range:**
**Description:** Auto-negotiation for the interface
**Type:** `boolean`

#### spanning_tree
**Allowed input range:** on,off
**Description:** Status of local spanning tree protocol
**Type:** `boolean`

#### mtu
**Allowed input range:**
**Description:** MTU setting
**Type:** `int`

#### speed - Link speed in MB/s
**Allowed input range:**
**Description:** 
**Type:** `int`

#### minimum_bond_aggregation
**Allowed input range:** 1-9999
**Description:** Smallest number of links up to allow bonding
**Type:** `int`


### link_services 
**Description:** Services configured on the interface (body)
**Type:** `body link_services`

**Example:**

```cf3

body link_services ospf_area(area)
{
ospf_area => "$(area)";
ospf_authentication_digest => "ABCDEFGHIJK";
ospf_link_type => "point-to-point";
ospf_hello_interval => "5";
}

```

#### ospf_hello_interval
**Allowed input range:** 0-9999
**Description:** OSPF Link database area number
**Type:** `int`

#### ospf_priority
**Allowed input range:** 0-9999
**Description:** OSPF Link database area number
**Type:** `int`

#### ospf_link_type
**Allowed input range:** broadcast,non-broadcast,point-to-multipoint,point-to-point
**Description:** OSPF interface type
**Type:** `menu string`

#### ospf_authentication_digest
**Description:** Authentication digest for interface
**Type:** `string`

#### ospf_passive_interface
**Allowed input range:** true/false
**Description:** No service updates over this channel
**Type:** `boolean`

#### ospf_abr_summarization
**Allowed input range:**
**Description:** Allow Area Border Router to inject summaries into a stub area via this interface
**Type:** `boolean`

#### ospf_area_type
**Allowed input range:** stub,nssa,normal
**Description:** Area type for ospf
**Type:** `int`

#### ospf_area
**Allowed input range:**
**Description:** OSPF Link database area number 
**Type:** `int`

**Example:**

```cf3
body link_services ebgp_session(directip, remoteas)
{
bgp_session_neighbor => "$(directip)"; # or use $(this.promiser) for unnumbered interface
bgp_peer_as => "$(remoteas)";
bgp_ttl_security => "1";
bgp_advertisement_interval => "0";
bgp_external_soft_reconfiguration_inbound => "true";
bgp_advertise_families => { "ipv4_unicast" };
}

```

#### bgp_session_neighbor
**Allowed input range:**
**Description:** A IP addresses of the current (numbered) interface to establish a bgp connection with a remote peer
**Type:** `string`

#### bgp_peer_as
**Allowed input range:** 1-999999
**Description:** The remote peer's AS number
**Type:** `int`

#### bgp_route_reflector
**Allowed input range:** client,server
**Description:** For iBGP, the role of this host with respect to a central route redistribuion hub
**Type:** `menu string`

#### bgp_ttl_security - Do not accept bgp frames more than this number of hops away
**Allowed input range:**
**Description:** 
**Type:** `int`

#### bgp_maximum_paths
**Allowed input range:** 1,255
**Description:** Enable bgp multipath support
**Type:** `int`

#### bgp_advertisement_interval
**Allowed input range:** 0-99999
**Description:** How long do we wait (ifelapsed) to broadcast bgp updates
**Type:** `int`

#### bgp_internal_next_hop_self
**Allowed input range:** true/false
**Description:** iBGP hops within the same AS. Router knows how to forward to prefixes it announces
**Type:** `boolean`

#### bgp_advertise_families
**Allowed input range:** ipv4_unicast,ipv6_unicast
**Description:** Share networks in these address families to neighbour
**Type:** `menu string`

#### bgp_external_soft_reconfiguration_inbound
**Allowed input range:**
**Description:** Allow updates from a neighbor without full reset of BGP session, cache policy history
**Type:** `bool`

#### bgp_ipv6_neighbor_discovery_route_advertisement
**Allowed input range:** allow,suppress
**Description:** For iBGP, a central route redistribuion hub
**Type:** `menu string`

**Example:**

```cf3
bundle agent main()
{
interfaces:
  "eth0"
      ipv4_addresses => { "172.16.2.5/24" },
       link_services =>  ospf_area("1", "stub");
  "eth1"
      ipv4_addresses => { "172.16.1.5/24" },
       link_services =>  ospf_area("0", "normal");
}

################# TEMPLATES #######################

body link_services ospf_area(area, stub)
{
ospf_area => "$(area)";
ospf_authentication_digest => "ABCDEFGHIJK";
ospf_area_type => "$(stub)";                   # Dinesh: This is an area-specific command
ospf_priority => "21";
ospf_passive_interface => "false";
}
```


### tunnel
**Description:** Tunnel and overlay configuration (body). 
**Type:** `body tunnel`

Tunnels are virtual point to point connections overlayed on physical infrastructure.
Currently only VxLAN is supported by CFEngine.

**Example:**

```cf3
body tunnel vxlan(id,vtep_ip,alien_mac_table)
{
tunnel_id => "$(id)";
tunnel_address => "$(vtep_ip)";
tunnel_multicast_group => "239.1.1.1";
tunnel_interface => "eth0";
tunnel_alien_addresses => "$(alien_mac_table)";
}
```

#### tunnel_id 
**Allowed input range:** 
**Description:**  Tunnel identifier number (VxLAN VNI etc)
**Type:** `int`

#### tunnel_address
**Allowed input range:** IP address in CIDR format
**Description:** Tunnel local management/loopback address
**Type:** `int`

#### tunnel_multicast_group
**Allowed input range:**
**Description:** IP address of multicast group for tunnel distribution
**Type:** `IP address`

#### tunnel_interface
**Allowed input range:** 
**Description:** Optional particular interface for tunnel
**Type:** `string`

#### tunnel_alien_addresses
**Allowed input range:** 
**Description:** Name of a CFEngine array variable pointing to remote hardware addresses to be mapped into the current broadcast domain.
**Type:** `string`


**Example:**

```cf3

bundle common my
{
vars:

  # LAN RouterIDs/Loopback addresses

  "router_id[switch1]"    string => "172.10.1.1";
  "router_id[switch1]"    string => "172.20.1.1";
  "router_id[cflu-10004]" string => "172.30.1.1";
  "router_id[switch4]"    string => "172.30.1.1";

  # VxLAN tunnel needs this manual set-up - L2 shortcut, bootstrapped over L3

  # Tunnel        Loopback                      MAC TABLE
  "vxlan1000_mac[172.10.1.1]" slist => { "00:00:10:00:00:0A", "00:00:10:00:00:0B" };
  "vxlan1000_mac[172.20.1.1]" slist => { "00:00:10:00:00:0C" };
  "vxlan1000_mac[172.30.1.1]" slist => { "00:00:10:00:00:0D", "00:00:10:00:00:0E" };
  "vxlan1000_mac[172.40.1.1]" slist => { "00:00:10:00:00:0F" };

  # if AM associated with switch1, choose these MAC addresses

  #     LAN IP  LOCATION                  LAN MAC BINDING
  "arp[10.1.1.1][switch1]"    string => "00:00:10:00:00:0A";
  "arp[10.1.1.2][switch1]"    string => "00:00:10:00:00:0B";
  "arp[10.1.1.3][switch2]"    string => "00:00:10:00:00:0C";
  "arp[10.1.1.4][cflu-10004]" string => "00:00:10:00:00:0D";  
  "arp[10.1.1.5][cflu-10004]" string => "00:00:10:00:00:0E";
  "arp[10.1.1.6][switch4]"    string => "00:00:10:00:00:0F";
}

##############################################################

bundle agent main()
{
vars:
   "ip_address" slist => getindices("my.arp");

interfaces:

  "vtep1000"
     ipv4_addresses => { "192.1.2.3/24" },
             tunnel => vxlan("1000","$(my.router_id[$(sys.uqhost)])", "my.vxlan1000_mac");

addresses:

   # Host ARP bindings

   "$(ip_address)"
          comment => "Teleport a static ARP binding for the VxLAN",
     link_address => "$(my.arp[$(ip_address)][$(sys.uqhost)])",
        interface => "eth0",
       ifvarclass => isvariable("my.arp[$(ip_address)][$(sys.uqhost)]");

reports:

   "Add ARP for $(ip_address) and $(my.arp[$(ip_address)][$(sys.uqhost)])"
       ifvarclass => isvariable("my.arp[$(ip_address)][$(sys.uqhost)]");
}

##############################################################

body tunnel vxlan(id,vtep_ip,alien_mac_table)
{
tunnel_id => "$(id)";
tunnel_address => "$(vtep_ip)";
tunnel_multicast_group => "239.1.1.1";
tunnel_interface => "eth0";
tunnel_alien_addresses => "$(alien_mac_table)";
}

body link_state up
{
state => "up";
}

##############################################################

body common control
{
bundlesequence => { "main" };
}

```

