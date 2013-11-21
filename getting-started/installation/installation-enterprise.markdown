---
layout: default
title: Installing Enterprise for Production
categories: [Getting Started, Installation, Installing Enterprise]
published: 
sorting: 40
alias: getting-started-installation-installing-enterprise.html
tags: [getting started, installation, enterprise]
---

These instructions describe how to install the latest version of CFEngine Enterprise in a production environment 
using pre-compiled rpm and deb packages for Ubuntu, Debian, Redhat, CentOS, and SUSE.

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

## Policy Server Requirements

CFEngine recommends the following:

### Memory

A minimum of 2 GB of available memory and a modern 64 bit processor. For a
large number of Hosts (Clients), we recommend 8 GB of available memory per 500
hosts that are bootstrapped to your Policy Server. Contact your sales
representative if you have any questions regarding these numbers.

### Port 80

The Policy Server hosts the Mission Portal through Apache, so ensure that port
80 is open.

**Note:** To avoid potential interference with the installation process, start
from a blank system (i.e. no Apache Web Server, no MongoDB, etc).

### MongoDB Requirements

CFEngine uses MongoDB, an open-source, NoSQL database. It stores data that
is collected from the Hosts.

CFEngine recommends the following configurations:

1. Filesystem type:
   - ext4 (a 2.6.23 kernel is required for efficient filesystem preallocation)
   - xfs (a 2.6.25 kernel is required for efficient filesystem preallocation)
2. Memory: Approximately 8 GB per 500 hosts
3. Turn off NUMA if you are running MongoDB on NUMA. Refer to
http://www.mongodb.org/display/DOCS/NUMA for more information.
4. Do not use large VM pages with Linux. Refer to
http://linuxgazette.net/155/krishnakumar.html for more information on large
pages.
5. Set the file descriptor limit and user process limit to 4k+ (see etc/limits
and ulimit)

## Download Packages

CFEngine Enterprise is provided in two packages; one is for the Policy
Server (hub) and the other is for each Host (client). 

**Select a Policy Server (hub) package to download:**

Ubuntu 10.04

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/hub/ubuntu-10.04-x86_64/cfengine-nova-hub_3.5.2-1_amd64.deb
```

Ubuntu 12.04

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/hub/ubuntu-12.04-x86_64/cfengine-nova-hub_3.5.2-1_amd64.deb
```

RHEL 5.4

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/hub/rhel-5.4-x86_64/cfengine-nova-hub-3.5.2-1.x86_64.rpm
```

SUSE 11.1

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/hub/sles-11.1-x86_64/cfengine-nova-hub-3.5.2-1.x86_64.rpm
```

Debian 6.0

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/hub/debian-6.0-x86_64/cfengine-nova-hub_3.5.2-1_amd64.deb
```

RHEL 6.0 

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/hub/rhel-6.0-x86_64/cfengine-nova-hub-3.5.2-1.x86_64.rpm
```

**Select a Host (client) package to download:**

Ubuntu/Debian 32-bit:

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/client/agent_deb_i386/cfengine-nova_3.5.2-1_i386.deb
```

Ubuntu/Debian 64-bit:

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/client/agent_deb_x86_64/cfengine-nova_3.5.2-1_x86_64.deb
```

Redhat/CentOS/SUSE 32-bit:

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/client/agent_rpm_i386/cfengine-nova-3.5.2-1.i386.rpm
```

Redhat/CentOS/SUSE 64-bit:

```
wget http://s3.amazonaws.com/cfengine.packages/Enterprise-3.5.2/client/agent_rpm_x86_64/cfengine-nova-3.5.2-1.x86_64.rpm
```

## Install Packages

**Log in as root** and then follow these steps to install CFEngine Enterprise:

1. On the designated Policy Server, install the `cfengine-nova-hub` package:

    ```
        [RedHat/CentOS/SUSE] $ rpm -i <hub package>.rpm
        [Debian/Ubuntu]      $ dpkg -i <hub package>.deb
    ```

2. On each Host, install the `cfengine-nova` package:

    ```
        [RedHat/CentOS/SUSE] $ rpm -i <agent package>.rpm
        [Debian/Ubuntu]      $ dpkg -i <agent package>.deb
    ```

## Bootstrap

Run the bootstrap command, **first** on the policy server and then on each
host:

```
$ /var/cfengine/bin/cf-agent --bootstrap <IP address of the Policy Server>
```

## Licensed installations

If you are evaluating CFEngine Enterprise or otherwise using it in an environment with 
less than 25 agents connecting to a Policy Server, 
you do not need a license and there is no expiry.

If you are a customer, please send the Policy Server's public key (`/var/cfengine/ppkeys/localhost.pub`) to
CFEngine support to obtain a license. CFEngine will send you a `license.dat`
file. Copy the obtained license file to
`/var/cfengine/masterfiles/license.dat`

## Next Steps

When bootstrapping is complete, CFEngine is up and running on your system.

The Mission Portal is immediately accessible. Connect to the Policy Server
through your web browser at http://`<IP address of your Policy Server>`.

To be able to use the [Mission Portal's][Mission Portal] Design Center
front-end, continue with [integrating Mission Portal with git] [Integrating Mission Portal with git]. 

Learn more about CFEngine by using the following resources:

* Tutorial: [Create a standalone policy (Hello World).][Hello World]

* Tutorial: [Configure and deploy a policy using sketches in the Design Center.][Configure and Deploy a Policy Using Sketches (Enterprise Only)]

* CFEngine [manuals][CFEngine Manuals].

* Additional [tutorials, examples, and documentation][Learning Tools].

* Get [Support][Support and Community] from the CFEngine community.
