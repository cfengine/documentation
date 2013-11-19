---
layout: default
title: Installing Community
categories: [Getting Started, Installation, Installing Community]
published: true
sorting: 10
alias: getting-started-installation-installing-community.html
tags: [getting started, installation, community]
---

## Packages

Select a Community package to download:

32bit:
wget  http://cfengine.com/inside/binarydownload/download/items/1180 -O cfengine-community-3.5.2-1.i386.rpm
wget  http://cfengine.com/inside/binarydownload/download/items/1182 -O cfengine-community_3.5.2-1_i386.deb

64bit:
wget  http://cfengine.com/inside/binarydownload/download/items/1181 -O cfengine-community-3.5.2-1.x86_64.rpm
wget  http://cfengine.com/inside/binarydownload/download/items/1183 -O cfengine-community_3.5.2-1_amd64.deb


## Installation 

First, install the package **first** on the Policy Server, and then on each Host:

32bit:
     ```
        [RedHat/CentOS/SUSE] $ rpm -i cfengine-community_3.5.2-1.i386.rpm
        [Debian/Ubuntu]      $ dpkg -i cfengine-community_3.5.2-1_i386.deb
     ```
64bit:
     ```
        [RedHat/CentOS/SUSE] $ rpm -i cfengine-community-3.5.2-1.x86_64.rpm
        [Debian/Ubuntu]      $ dpkg -i cfengine-community_3.5.2-1_amd64.deb
     ```  

Next, run the bootstrap command, **first** on the Policy Server, and then on each Host:

     ```
        /var/cfengine/bin/cf-agent --bootstrap <IP address of policy server>
     ```

## Next Steps

Learn more about CFEngine by using the following resources:

* Tutorial: [Get CFEngine Up and Running Quickly: A Primer for New Community Users][Up and Running]

* Tutorial: [Create a standalone policy (Hello World).][Hello World]

* CFEngine [manuals][CFEngine Manuals].

* View additional [tutorials, examples, and documentation][Learning Tools].

* Get [Support][Support and Community] from the CFEngine community.

## Production Environment

If you plan to use Community in a production environment, complete the following general requirements:

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
