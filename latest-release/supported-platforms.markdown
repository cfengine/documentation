---
layout: default
title: Supported Platforms and Versions
sorting: 40
categories: [Latest Release, Supported Platforms]
published: true
alias: getting-started-supported-platforms.html
tags: [getting started, platforms, versions, support]
---

This pre-release of CFEngine has been rudimentarily tested on the
following platforms:

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

<!--- TODO: switch for release, remove above from stable branches



CFEngine works on a wide range of platforms, and the CFEngine team strives to 
provide support for the platforms most frequently used by our users. We have 
designed our internal testing procedures to divide platforms into three 
categories in order to prioritize internal testing and resources, so that the 
most frequently used platforms are subjected to our most rigorous testing 
processes.

### Tier 1 Platforms

Tier 1 platforms are fully integrated into our continuous delivery process, 
which runs our full automated test suite, from compilation to full system 
deployment into a test environment. We provide throughly tested packages that 
integrate with the platforms respective package management system, and our 
technical staff is working on these platforms on a daily basis.

You should expect the [CFEngine source code][github core] to compile and work 
on these platforms at all times.

#### CFEngine Enterprise Server

| OS              | Versions     | Architectures      |
|-----------------|--------------|--------------------|
| RedHat          | 5, 6         | x86-64             |

#### Host

| OS              | Versions     | Architectures      |
|-----------------|--------------|--------------------|
| RedHat          | 5, 6         | x86-64, x386       |
| Solaris         | 10           | x86-64, UltraSparc |

### Tier 2 Platforms

Platforms in this category are incorporated in some of our continuous 
integration systems and are tested on a regular basis, although not 
continuously.

We provide packages that are subject to basic testing for all releases.
Some of our technical staff has hands-on experience on these platforms.

#### CFEngine Enterprise Server

| OS              | Versions      | Architectures      |
|-----------------|---------------|--------------------|
| SLES            | 11            | x86-64             |
| Debian          | 6             | x86-64             |
| Ubuntu          | 10.04, 12.04  | x86-64             |

#### Host

| OS              | Versions      | Architectures      |
|-----------------|---------------|--------------------|
| SLES            | 11            | x86-64, i386       |
| Debian          | 6             | x86-64, i386       |
| Ubuntu          | 10.04, 12.04  | x86-64, i386       |
| Windows         | 2008 Standard | i386/x86-64

### Tier 3 Platforms

CFEngine is known to run on a wide range of other platforms. As long as the 
platform is POSIX compliant, has a C compiler toolchain that fully implements 
the C99 standard, and is in general supported by the vendor, we are happy to 
work with you to make CFEngine available. Please [contact our sales
team][contact us] for details.

We know that the current version of CFEngine can be made to work on the 
following platforms. However, note that certain CFEngine functionality might 
not be available, and that our capacity to provide technical support on these 
platforms is likely to be limited.

In general, platforms in this category can only be supported as hosts.

* Solaris 9 UltraSparc
* AIX 5.3, 6.1 and 7.1
* HP-UX 11.23 and 11.31
* RHEL 4
* Debian 4
* Open Indiana
* SmartOS
* SLES on Mainframe 390

Note that availability of the current version of CFEngine on these platforms 
does not imply availability of future versions of CFEngine.

Community users might be able to build the host binaries directly from 
sources on additional platforms.


## Hub/Host compatibility

We strongly recommend to install identical versions on all hosts and servers 
in your system.

A server running CFEngine Enterprise 3.5 can serve policy to and collect data 
from hosts running the following versions of CFEngine:

* 3.5.x
* 3.0.x
* 2.2.x


Some data will not be available from older hosts, and the policy you serve 
needs to take into account hosts with different versions.

-->

## General Legal Disclaimer

Please note that CFEngine is offered on an "as is" basis without warranty of 
any kind, and that our products are not error or bug free. To the maximum 
extent permitted by applicable law, CFEngine on behalf of itself and its 
suppliers, disclaims all warranties and conditions, either express or implied, 
including, but not limited to, implied warranties of merchantability, fitness 
for a particular purpose, title and non-infringement with regard to the 
Licensed Software.
