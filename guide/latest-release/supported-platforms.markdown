---
layout: default
title: Supported Platforms and Versions
sorting: 20
published: true
tags: [overviews, releases, latest release, "3.6", platforms, versions, support]
---

CFEngine works on a wide range of platforms, and the CFEngine team strives to
provide support for the platforms most frequently used by our users.


## Enterprise Server ##

| Platform         | Versions      | Architecture      |
| :--------------: | :-----------: | :---------------: |
| CentOS           | 5, 6, 7       | x86-64            |
| Debian           | 6, 7, 8       | x86-64            |
| RHEL             | 5, 6, 7       | x86-64            |
| SLES             | 11            | x86-64            |
| Ubuntu           | 10.04, 12.04  | x86-64            |

Any supported host can be a policy server in Community installations of CFEngine.

## Hosts ##

| Platform| Versions     | Architectures |
| :-----: | :----------: | :-----------: |
| AIX     | 5.3*, 6, 7   | PowerPC       |
| CentOS  | 4, 5, 6, 7   | x86-64, x86   |
| Debian  | 6, 7, 8      | x86-64, x86   |
| HP-UX   | 11.23+       | Itanium       |
| RHEL    | 4, 5, 6, 7   | x86-64, x86   |
| SLES    | 10, 11       | x86-64, x86   |
| Solaris | 9            | SPARC         |
| Solaris | 10, 11       | UltraSparc    |
| Ubuntu  | 10.04, 12.04 | x86-64, x86   |
| Windows | 2008         | x86-64, x86   |
| Windows | 2008, 2012   | x86-64        |

\* AIX 5.3 is required to have "5300-05-CSP" or later

[Known Issues][] also includes platform-specific notes.


CFEngine Enterprise has [Virtual I/O Server (VIOS) Recognized status](http://www.ibm.com/partnerworld/gsd/solutiondetails.do?solution=48493) from IBM.
This means that CFEngine Enterprise has been technically verified by IBM
to be installed in and manage VIOS environments.

## Hub/Host compatibility ##

An upgrade path from previous versions is available.

Some data will not be available from hosts on version 3.5.x or older, and the policy you serve
needs to take into account hosts with different versions.

## Future platform support ##

The CFEngine team will continue to support future releases of popular Host platforms, including RHEL, Debian, Ubuntu, as well as maintaining support for existing platforms important to users.

In general, CFEngine is known to run on a wide range of other platforms. As long as the
platform is POSIX compliant and has a C compiler toolchain that fully implements
the C99 standard, we are happy to work with you to make CFEngine available.
Please [contact our sales team][contact us] for details.

