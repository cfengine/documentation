---
layout: default
title: Installing CFEngine
sorting: 10
categories: [Getting Started, Installation]
published: true
alias: getting-started-installation.html
tags: [getting started, installation]
---

**IMPORTANT NOTE:** *This is a pre-release of CFEngine, intended for testing
and showcase only. This version is not supported, not covered by service-level
agreements (SLAs), and not intended for production environments. Do not 
upgrade or use in conjunction with other versions at this point.*

<!--- TODO: move up when no longer a pre-release
-->

## General Requirements

CFEngine recommends the following:

**Host(s) Memory** 

256 MB available memory in order to run the CFEngine agent software (cf-agent).

**Disk Storage** 

A full installation of CFEngine requires 25 MB. Additional disk usage
depends on your specific policies, especially those that concern reporting.

**Network** 

* Verify that the machine’s network connection is working and that port 5308
  (used by CFEngine) is open for both incoming and outgoing connections.

* If iptables are active on your operating system, stop this service or adapt
  it to allow for communication on the above ports. If applicable, type the
  following two commands: /`etc/init.d/iptables stop` and `chkconfig iptables
  off`

CFEngine bundles all critical dependencies into the package; therefore,
additional software is not required.

## Specific Requirements

Click here to complete the [Community][Installing Community] installation.

Click here to complete the [Enterprise][Installing Enterprise] installation.
