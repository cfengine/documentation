---
layout: default
title: Supported Platforms and Versions
sorting: 1
published: true
tags: [overviews, releases, latest release, 3.6.0, platforms, versions, support]
---

* [Supported Platforms][Supported Platforms and Versions#Supported Platforms]
* [Platform Notes][Supported Platforms and Versions#Platform Notes]
	* [Microsoft Windows][Supported Platforms and Versions#Microsoft Windows]

## Supported Platforms ##

This pre-release of CFEngine has been rudimentarily tested on the
following platforms:

| Platform     | Versions   | Architecture    |
|--------------|-----------:|:---------------:|
|CentOS        | 5, 6       | x86-64, i386    |
|RHEL          | 5, 6       | x86-64, i386    |
|Ubuntu        | 10.4, 12.4 | x86-64, i386    |

<!--- TODO: switch for release, remove above from stable branches

CFEngine works on a wide range of platforms, and the CFEngine team strives to 
provide support for the platforms most frequently used by our users.

### CFEngine Enterprise Server

| OS              | Versions     | Architectures      |
|-----------------|--------------|--------------------|
| RedHat          | 5, 6         | x86-64             |
| Debian          | 6, 7         | x86-64             |
| SLES            | 11           | x86-64             |
| Ubuntu          | 10.4, 12.4   | x86-64             |

### Hosts

Any host can be a policy server in Community installations of CFEngine.

| OS              | Versions     | Architectures      |
|-----------------|--------------|--------------------|
| AIX             | 5.3, 6, 7    | PowerPC            |
| CentOS          | 5, 6         | x86-64, x386       |
| Debian          | 6, 7         | x86-64, x386       |
| RedHat          | 4, 5, 6      | x86-64, x386       |
| SLES            | 10, 11       | x86-64, x386       |
| Solaris         | 9            | SPARC              |
| Solaris         | 10, 11       | x86-64, UltraSparc |
| Ubuntu          | 10.4, 12.4   | x86-64, x386       |
| Windows         | 2008         | x386               |
| Windows         | 2008, 2012   | x86-64             |

CFEngine Enterprise has [Virtual I/O Server (VIOS) Recognized status](http://www.ibm.com/partnerworld/gsd/solutiondetails.do?solution=48493) from IBM.
This means that CFEngine Enterprise has been technically verified by IBM
to be installed in and manage VIOS environments.

## Hub/Host compatibility

We strongly recommend to install identical versions on all hosts and servers 
in your system.

A server running CFEngine Enterprise 3.6 can serve policy to and collect data 
from hosts running the following versions of CFEngine:

* 3.5.x
* 3.0.x
* 2.2.x

Some data will not be available from older hosts, and the policy you serve 
needs to take into account hosts with different versions.

## Additional platforms

CFEngine is known to run on a wide range of other platforms. As long as the 
platform is POSIX compliant and has a C compiler toolchain that fully implements 
the C99 standard, we are happy to work with you to make CFEngine available.
Please [contact our sales team][contact us] for details.

Note that availability of the current version of CFEngine on these platforms 
does not imply availability of future versions of CFEngine.

-->

## Platform Notes ##

CFEngine supports several platforms, including POSIX operating systems such as Unix and Linux, as well as Microsoft Windows.

While the latest versions of several popular operating systems are generally tested and supported, it is important to check the information specific to your platform to ensure a good understanding of specific approaches to take when deploying CFEngine.

### Microsoft Windows ###

CFEngine supports Microsoft Windows machines as client hosts, but with some functional differences compared with POSIX platforms, such as Unix and Linux. At the same time, CFEngine also does not currently support Windows policy servers. 

This however does not need to become a limitation to those who wish to deploy CFEngine in a Windows only IT environment. It is quite easy to setup a virtual machine running a popular flavor of Linux with minimal effort and under certain conditions no or low cost. See the instructions for deploying [CFEngine from Windows to an Amazon Web Services virtual machine running Red Hat Enterprise Linux][Installing CFEngine on RHEL Using AWS] for an example.
