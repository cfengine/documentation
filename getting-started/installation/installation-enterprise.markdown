---
layout: default
title: Installing Enterprise
categories: [Getting Started, Installation, Installing Enterprise]
published: true
alias: getting-started-installation-installing-enterprise.html
tags: [getting started, installation, enterprise]
---

Please complete the [General Requirements][Installing CFEngine] if you have not already done so.

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

## Packages

CFEngine Enterprise is provided in two packages; one is for the Policy
Server and the other is for each Host (Client). These packages contain the
following naming convention:

**Policy Server**: Only 64bit packages

* RPM Package: `cfengine-nova-hub-3.6.0-1.x86_64.rpm`

* Debian Package: `cfengine-nova-hub_3.6.0-1_amd64.deb`

**Hosts**: Both 64bit and 32bit

* RPM Package: `cfengine-nova-3.6.0-1.i386.rpm` or
  `cfengine-nova-3.6.0-1.x86_64.rpm`

* Debian Package: `cfengine-nova_3.6.0-1_i386.deb` or
  `cfengine-nova_3.6.0-1_amd64.deb`

## Installation

Follow these steps to install CFEngine:

1. Install packages

    On the designated Policy Server, install the `cfengine-nova-hub` package:

    ```
        [RedHat/CentOS/SUSE] $ rpm -i <hub package>.rpm
        [Debian/Ubuntu]      $ dpkg -i <hub package>.deb
    ```

    On each Host, install the `cfengine-nova` package:

    ```
        [RedHat/CentOS/SUSE] $ rpm -i <agent package>.rpm
        [Debian/Ubuntu]      $ dpkg -i <agent package>.deb
    ```

2. Run the bootstrap command, **first** on the policy server and then on each
host:

    ```
        $ /var/cfengine/bin/cf-agent --bootstrap <IP address of the Policy Server>
    ```

## Licensed installations

Send the Policy Server's public key (`/var/cfengine/ppkeys/localhost.pub`) to
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

* Read CFEngine [manuals][CFEngine Manuals].

* Get [Support][Support and Community] from the CFEngine community.

* View additional [tutorials, examples, and documentation][Learning Tools].
