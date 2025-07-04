---
layout: default
title: Supported platforms and versions
sorting: 20
---

CFEngine works on a wide range of platforms, and the CFEngine team strives to
provide support for the platforms most frequently used by our users. CFEngine
provides [binary packages of the Enterprise edition][enterprise software download page]
for all supported platforms and [binary packages for popular Linux distributions for the Community edition][community download page].

## Hub

| Platform    | Versions            | Architecture |
|:-----------:|:-------------------:|:------------:|
| CentOS/RHEL | 7, 8.1+, 9          | x86-64       |
| Debian      | 11, 12              | x86-64       |
| Debian      | 11, 12              | arm64        |
| Ubuntu      | 20.04, 22.04, 24.04 | x86-64       |
| Ubuntu      | 22.04, 24.04        | arm64        |

Any supported host can be a policy server in Community installations of CFEngine.

## Clients

| Platform    | Versions            | Architectures |
|:-----------:|:-------------------:|:-------------:|
| AIX         | 7.1, 7.2            | PowerPC       |
| CentOS/RHEL | 7, 8.1+, 9          | x86-64        |
| Debian      | 11, 12              | x86-64        |
| Debian      | 11, 12              | arm64         |
| HP-UX       | 11.31+              | Itanium       |
| SLES        | 12, 15              | x86-64        |
| Solaris     | 11                  | UltraSparc    |
| Ubuntu      | 20.04, 22.04, 24.04 | x86-64        |
| Ubuntu      | 22.04, 24.04        | arm64         |
| Windows     | 2012, 2016, 2019    | x86-64        |


[Known issues][] also includes platform-specific notes.


CFEngine Enterprise has [Virtual I/O Server (VIOS) Recognized status](http://www.ibm.com/partnerworld/gsd/solutiondetails.do?solution=48493) from IBM.
This means that CFEngine Enterprise has been technically verified by IBM
to be installed in and manage VIOS environments.

## Future platform support

The CFEngine team will continue to support future releases of popular Host
platforms, including RHEL, Debian, Ubuntu, as well as maintaining support for
existing platforms important to users.

In general, CFEngine is known to run on a wide range of other platforms. As long
as the platform is POSIX compliant and has a C compiler toolchain that fully
implements the C99 standard, we are happy to work with you to make CFEngine
available. Please [contact our sales team][contact us] for details.
