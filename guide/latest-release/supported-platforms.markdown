---
layout: default
title: Supported Platforms and Versions
sorting: 20
published: true
tags: [overviews, releases, latest release, 3.6, platforms, versions, support]
---

CFEngine works on a wide range of platforms, and the CFEngine team strives to
provide support for the platforms most frequently used by our users.

## Enterprise Server ##

| Platform     | Versions   | Architecture    |
|:--------------:|:-----------:|:---------------:|
| CentOS 	| 5, 6 	| x86-64   |
| RHEL 	| 5, 6 	| x86-64   |
| SLES 	| 11 	| x86-64   |
| Ubuntu 	| 10.04, 12.04 	| x86-64   |


## Hosts ##

Any host can be a policy server in Community installations of CFEngine.

| OS              | Versions     | Architectures      |
|-----------------|--------------|--------------------|
| AIX 	| 5.3, 6, 7 	| PowerPC   |
| CentOS 	| 5, 6 	| x86-64, i386   |
| Debian 	| 6, 7 	| x86-64, i386   |
| RedHat 	| 4, 5, 6 	| x86-64, i386   |
| SLES 	| 10, 11 	| x86-64, i386   |
| Solaris 	| 9 	| SPARC   |
| Solaris 	| 10, 11* 	| x86-64, UltraSparc   |
| Ubuntu 	| 10.4, 12.4 	| x86-64, i386   |
| Windows 	| 2008 	| x86-64, i386   |
| Windows 	| 2008, 2012 	| x86-64   |

\* Solaris 11 is currently experimental - see [Known Issues][]

CFEngine Enterprise has [Virtual I/O Server (VIOS) Recognized status](http://www.ibm.com/partnerworld/gsd/solutiondetails.do?solution=48493) from IBM.
This means that CFEngine Enterprise has been technically verified by IBM
to be installed in and manage VIOS environments.

## Hub/Host compatibility ##

An upgrade path from previous versions will be made available in 3.6.1.

Some data will not be available from older hosts, and the policy you serve
needs to take into account hosts with different versions.

## Additional platforms ##

CFEngine is known to run on a wide range of other platforms. As long as the
platform is POSIX compliant and has a C compiler toolchain that fully implements
the C99 standard, we are happy to work with you to make CFEngine available.
Please [contact our sales team][contact us] for details.

Note that availability of the current version of CFEngine on these platforms
does not imply availability of future versions of CFEngine.

