---
layout: default
title: Supported Platforms and Versions
sortkey: 3
categories: [Getting Started, Supported Platforms]
published: true
alias: getting-started-supported-platforms.html
tags: [getting started, platforms, versions, support]
---

<!--- TODO: switch for release
CFEngine Enterprise 3.5 has been tested and is generally available on the 
following platforms:
-->
This pre-release of CFEngine Enterprise 3.5 has been rudimentarily tested and 
released on the following platforms:

## Hub

| Platform     | Versions | Architecture    | Notes                          |
|--------------|---------:|:---------------:|--------------------------------|
|CentOS        | 5, 6     | x86-64          | Use RHEL packages              |
|RHEL          | 5, 6     | x86-64          |                                |
|Ubuntu        | 10.4     | x86-64          |                                |

## Hosts

| Platform     | Versions | Architecture    | Notes                          |
|--------------|---------:|:---------------:|--------------------------------|
|CentOS        | 5, 6     | x86-64, i386    | Use RHEL packages              |
|RHEL          | 5, 6     | x86-64, i386    |                                |
|Ubuntu        | 10.4     | x86-64, i386    |                                |
|Solaris       | 10       | x86-64, sparc   |                                |


## Hub/Host compatibility

We strongly recommend to install identical versions on all hosts and servers 
in your system.

A server running CFEngine Enterprise 3.5 can serve policy and collect data 
from hosts running the following versions of CFEngine:

* 3.5.x
* 3.0.x
* 2.2.x


Some data will not be available from older hosts, and the policy you serve 
needs to take into account hosts with different versions.
