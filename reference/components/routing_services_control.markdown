---
layout: default
title: routing_services control
published: true
sorting: 90
tags: [body, bodies, components, agent, networking, promises]
---


**History:** Was introduced in 3.6.2, (2014)

In networking devices that act as layer 3 routers, common services for
route propagation may be controlled by CFEngine. Those promises that
are internal to CFEngine with only minimal configuration are
configured through stanzas of the form:

```cf3
body routing_services control
{

}
```
### Attributes ###

### routing_service_log_file
**Allowed input range:**
**Description:**  Set log file for route service messages, if supported on platform
**Type:** `file path`

### routing_service_password

**Allowed input range:**
**Description:**  Set password for service, if supported on platform (e.g. quagga)
**Type:** `string`


### ospf_log_adjacency_changes
**Allowed input range:** normal,detail,none
**Description:**  OSPF logging of neighbour changes
**Type:** `menu string`

### ospf_log_timestamp_precision
**Allowed input range:** 0,6
**Description:**  Maximum precision in microseconds
**Type:** `int`

### ospf_router_id
**Allowed input range:** aaa.bbb.ccc.ddd
**Description:**  The router's identity address aka loopback address used by ospf
**Type:** `quasi IPv4 address`

### ospf_redistribute
**Allowed input range:** kernel,connected,static,bgp
**Description:**  List of sources of routing information considered authoritative
**Type:** `menu string`

### ospf_redistribute_metric_type
**Allowed input range:** 1,2
**Description:**  How to calculate metrics for external routes
**Type:** `int`

### ospf_redistribute_kernel_metric
**Allowed input range:** 1,9999
**Description:**  Metric for redistributed kernel route
**Type:** `int`

### ospf_redistribute_connected_metric
**Allowed input range:** 1,9999
**Description:**  Metric for redistributed direct connetions
**Type:** `int`

### ospf_redistribute_static_metric

**Allowed input range:** 1,9999
**Description:**  Metric for redistributed static route
**Type:** `int`

### ospf_redistribute_bgp_metric
**Allowed input range:** 1,9999
**Description:**  Metric for redistributed BGP route
**Type:** `int`

### bgp_local_as
**Allowed input range:** 0,99999
**Description:** This router's BGP autonomous system number
**Type:** `int`

### bgp_router_id
**Allowed input range:** aaa.bbb.ccc.ddd
**Description:**  The router's identity address aka loopback address for bgp
**Type:** `quasi IPv4 address`

### bgp_log_neighbor_changes
**Allowed input range:** true/false
**Description:**  Activate logging for bgp neighbour changes
**Type:** `boolean`

### bgp_redistribute
**Allowed input range:** kernel,connected,static,ospf
**Description:**  Which source of configuration is considered authoritative?
**Type:** `menu string`

### bgp_ipv4_networks
**Allowed input range:** IPv4 CIDR
**Description:**  List of local ipv4 networks to advertise for this router
**Type:** `IPv4 address` in CIDR format

### bgp_ipv6_networks
**Allowed input range:** IPv6 CIDR
**Description:**  List of local ipv6 networks to advertise for this router
**Type:** `IPv6 address` in CIDR format

### bgp_graceful_restart

**Allowed input range:** true/false
**Description:**  BGP session restart RFC, default is false
**Type:** `boolean`


**Example:**

```cf3

body routing_services control
{
any::
 routing_service_log_file => "/var/log/quagga";
 routing_service_password => "x1234";

router1::
 ospf_log_adjacency_changes => "detail";
 ospf_router_id => "$(sys.ipv4[lo])";
 ospf_log_timestamp_precision => "4";
 ospf_redistribute => { "kernel", "static", "bgp" };
 ospf_redistribute_metric_type => "2";
 ospf_redistribute_kernel_metric => "1";
 ospf_redistribute_connected_metric => "0";
 ospf_redistribute_static_metric => "1";
 ospf_redistribute_bgp_metric => "2";

router2::

 bgp_graceful_restart => "true";
 bgp_local_as => "65001";
 bgp_ipv4_networks => { "192.168.1.0/24", "192.168.2.0/24" };
 bgp_log_neighbor_changes => "true";
 bgp_redistribute => { "kernel", "static", "connected", "ospf" };

}

```
