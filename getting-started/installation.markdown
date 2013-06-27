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
and showcase only. This version is not supported, not covered by service level
agreements (SLAs) and not intended for production environments. Do not upgrade
or use in conjunction with other versions at this point.

<!--- TODO: move up when no longer a pre-release
-->

## General Requirements

CFEngine recommends the following:

**Host(s) Memory** 

256 MB available memory in order to run the CFEngine agent software (cf_agent)

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

****

## Community Edition

The Community Edition is packaged using the following naming convention:

* RPM Package: `cfengine-community-3.6.0XXXX.x86_64.rpm`

* Debian Package: `cfengine-community_3.6.0XXX_amd64.deb`

### Installation 

1. Install the package **first** on the Policy Server, and then on each Host:

```
    [RedHat/CentOS/SUSE] $ rpm -i <package>.rpm
    [Debian/Ubuntu]      $ dpkg -i <package>.deb
```

2. Run the bootstrap command, **first** on the Policy Server, and then on each
Host:

````
/var/cfengine/bin/cf-agent --bootstrap <ip address of policy server>
````

****

## Enterprise Edition

### Requirements

#### Policy Server Requirements

CFEngine recommends the following:

**Memory** 

A minimum of 2 GB of available memory and a modern 64 bit processor. For a
large number of Hosts (Clients), we recommend 8 GB of available memory per 500
hosts that are bootstrapped to your Policy Server. Contact your sales
representative if you have any questions regarding these numbers.

**Port 80**

The Policy Server hosts the Mission Portal through Apache, so ensure that port
80 is open.

**Note:** To avoid potential interference with the installation process, start
from a blank system (i.e. no Apache Web Server, no MongoDB, etc).

#### MongoDB Requirements

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

### Packages

CFEngine Enterprise is provided in two packages; one is for the Policy
Server and the other is for each Host (Client). These packages contain the
following naming convention:

**Policy Server**: Only 64bit packages

* RPM Package: `cfengine-nova-hub-3.6.0XXXX.x86_64.rpm`

* Debian Package: `cfengine-nova-hub_3.6.0XXXX_amd64.deb`

**Hosts**: Both 64bit and 32bit

* RPM Package: `cfengine-nova-3.6.0-XXXX.i386.rpm` or
  `cfengine-nova-3.6.0-XXXX.x86_64.rpm`

* Debian Package: `cfengine-nova_3.6.0XXXX_i386.deb` or
  `cfengine-nova_3.6.0XXXX_amd64.deb`

### Installation

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

``` $ /var/cfengine/bin/cf-agent --bootstrap <IP address of the Policy Server>
```

#### Automatic bootstrapping

Automatic bootstrapping allows the user to connect a CFEngine Host to a Policy
Server without specifying the IP address manually. It uses the *Avahi* service
discovery implementation of `zeroconf` to locate the hub, obtain its IP
address, and then connect to it. To use automatic bootstrap, install the
following Avahi libraries:

* libavahi-client
* libavahi-common

To make the CFEngine Server discoverable, it needs to register itself as an 
Avahi service. Run the following command:

```    
$ /var/cfengine/bin/cf-serverd -A
``` 

This generates the configuration file for Avahi in `/etc/avahi/services` and 
restarts the Avahi daemon in order to register the new service.

From this point on, the Policy Server will be discovered with the Avahi service.
To verify that the server is visible, run the following command (requires
`avahi-utils`):

``` 
    $ avahi-browse -atr | grep cfenginehub
``` 

The sample output looks like this:

``` 
    eth0 IPv4 CFEngine Community 3.6.0 Policy Server on policy_hub_debian7
    _cfenginehub._tcp local
``` 

Once the Policy Server is configured with the Avahi service, you can
auto-bootstrap Hosts to it.

``` 
    $ /var/cfengine/bin/cf-agent -B :avahi
``` 

The Hosts require Avahi libraries to be installed in order to use this 
functionality. By default `cf-agent` looks for libraries in standard install 
locations. Install locations vary from system to system. If Avahi is 
installed in a non-standard location (i.e. compiled from source), set the 
`AVAHI_PATH` environmental variable to specify the path.

``` 
   $ AVAHI_PATH=/lib/libavahi-client.so.3 /var/cfengine/bin/cf-agent -B
``` 

If more than one server is found, or if the server has more than one IP
address, the list of all available servers is printed and the user is asked to
manually specify the IP address of the correct server by running the standard
bootstrap command of cf-agent:

``` 
   $ /var/cfengine/bin/cf-agent --bootstrap <IP address>
``` 

If only one Policy Server is found in the network, `cf-agent` performs the
bootstrap without further manual user intervention.

**Note:** Automatic bootstrapping support is ONLY for Linux, and it is limited
only to one subnet.

#### Licensed installations

Send the Policy Server's public key (`/var/cfengine/ppkeys/localhost.pub`) to
CFEngine support to obtain a license. CFEngine will send you a `license.dat`
file. Copy the obtained license file to
`/var/cfengine/masterfiles/license.dat`

### Next Steps

When bootstrapping is complete, CFEngine is up and running on your system.

The Mission Portal is immediately accessible. Connect to the Policy Server
through your web browser at http://<IP address of your Policy Server>.

To be able to use the [Mission Portals'][Mission Portal] Design Center
front-end, continue with [integrating Mission Portal with git][Integrating
Mission Portal with git].

