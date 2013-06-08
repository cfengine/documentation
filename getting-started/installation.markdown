---
layout: default
title: Installing CFEngine
sortkey: 1
categories: [Getting Started, Installation]
published: true
alias: getting-started-installation.html
tags: [getting started, installation]
---

**IMPORTANT NOTE:** *This is a pre-release of 3.5, intended for testing and 
showcase only. This version is not supported, not covered by service level 
agreements (SLAs) and not intended for production environments. Do not upgrade 
or use in conjunction with other versions at this point. We are planning 
monthly snapshot (alpha) releases going forward, but official release date for 
3.5 has not been set.*

<!--- TODO: move up when no longer a pre-release
-->


## Requirements

CFEngine recommends to have 256 MB available memory on the clients. For 
machines under CFEngine’s management (clients), a full installation of 
CFEngine 3.5 requires about 25 MB of disk storage. Otherwise disk usage 
depends on your specific policies, especially those that concern reporting.

Verify that the machine’s network connection is working and that port 5308 
(used by CFEngine) is open for both incoming and outgoing connections. A 
common problem is that iptables are active by default on some operating 
systems. Remember to stop this service or adapt it to allow for communication 
on the above ports. If applicable, typing the following two commands: 
"/etc/init.d/iptables stop" and "chkconfig iptables off".

No special software is otherwise required on machines in your network, 
CFEngine bundles all critical dependencies in the package (see also SOFTWARE 
DEPENDENCIES below).

### Requirements specific to CFEngine Enterprise Server

CFEngine recommends that the machine for the CFEngine Server should have at 
least 2 GB of memory and a modern 64 bit processor. For a large number of 
clients we recommend, as a rule of thumb, to have 8 GB of memory available per 
500 hosts bootstrapped to the server. Please contact your sales representative 
if you have any questions regarding these numbers. 

The CFEngine Enterprise server hosts the Mission Portal through Apache, so make sure that port 80 is open.

To avoid potential interference with the installation process, start from a blank system (i.e. no Apache Web
Server, no MongoDB, etc).

Requirements specific to MongoDB:

1. Filesystem type:
   - ext4 ( kernel version >= 2.6.23 )
   - xfs ( kernel version >= 2.6.25 )
2. Memory: Approximately 8 GB per 500 hosts
3. Turn off NUMA if running on numa hardware. 
   http://www.mongodb.org/display/DOCS/NUMA
4. Do not use large VM pages with Linux (info about large pages: 
   http://linuxgazette.net/155/krishnakumar.html)
5. Set file descriptor limit and user process limit to 4k+ (see etc/limits and 
   ulimit)

For those running databases on ext4 filesystems, a 2.6.23 kernel is required 
for efficient filesystem preallocation, 2.6.25 is required for XFS support of 
the same feature. High filesystem I/O following the allocation of new database 
files is one symptom of this problem.

****

## Installation Instructions

### Community Edition

If you are using CFEngine Enterprise, go straight to the respective 
instructions further down.

The Community Edition is in packages with these naming patterns:

* RPM Package: `cfengine-community-3.5.0XXXX.x86_64.rpm`

* Debian Package: `cfengine-community_3.5.0XXX_amd64.deb`

Install the package first on the policy server, then on the clients. Upon 
installation on two or more hosts, the role of policy server is adopted by the 
first host that is bootstrapped to by another host. After bootstrapping, 
running the following command on a host will show whether or not it is the hub 
(policy server):

    $ /var/cfengine/bin/cf-promises -v

If the host is currently a hub, the am_policy_hub class should
be set.


### Enterprise Edition

CFEngine 3.5 Enterprise is provided in two packages (one hub and one client 
package) with the following names:

**Hub**: Only 64bit packages

* RPM Package: `cfengine-nova-hub-3.5.0XXXX.x86_64.rpm`

* Debian Package: `cfengine-nova-hub_3.5.0XXXX_amd64.deb`

**Client**: Both 64bit and 32bit

* RPM Package: `cfengine-nova-3.5.0-XXXX.i386.rpm` or 
`cfengine-nova-3.5.0-XXXX.x86_64.rpm`

* Debian Package: `cfengine-nova_3.5.0XXXX_i386.deb` or 
`cfengine-nova_3.5.0XXXX_amd64.deb`


Follow these steps to install CFEngine:

1. Copy the CFEngine 3.5 Enterprise packages to their respective systems

I.e hub package to the host that will be the CFEngine policy server, and 
the client packages to each of the other hosts.

2. On the hub/policy server, unpack the `cfengine-nova-hub` package:

```
    [RedHat/CentOS/SUSE] $ rpm -i <hub package>.rpm
    [Debian/Ubuntu]      $ dpkg -i <hub package>.deb
```

   - (Skip for CFEngine 3.5 Free Enterprise): Send the hub's public key (`/var/cfengine/ppkeys/localhost.pub`) to CFEngine support to obtain a license
   - (Skip for CFEngine 3.5 Free Enterprise): Copy the obtained license file to `/var/cfengine/masterfiles/license.dat`

3. On the hosts: Unpack the `cfengine-nova` package:

```
    [RedHat/CentOS/SUSE] $ rpm -i <agent package>.rpm
    [Debian/Ubuntu]      $ dpkg -i <agent package>.deb
```

4. Bootstrap the machines to the hub, starting with the hub itself.

```
     $ /var/cfengine/bin/cf-agent --bootstrap <IP ADDRESS OF HUB>
```

**Note**: For host machines, see below for an automatic alternative to this 
step.

6. CFEngine should now be up and running on your system.

The Mission Portal should be immediately accessible, and you should be able to 
connect to the hub IP-address through your web browser (http and port 80).

## Automatic Bootstrapping

Automatic bootstrap allows the user to connect a CFEngine client to a 
hub/policy server without specifying the IP address manually. 
It uses the *Avahi* service discovery implementation of `zeroconf` to locate 
the hub, obtain its IP address and connect to it. To use automatic bootstrap 
installation of Avahi libraries is required.

* libavahi-client
* libavahi-common

To make the CFEngine Server discoverable, it needs to register itself as an 
Avahi service. Run the following command:

    $ /var/cfengine/bin/cf-serverd -A

This generates the configuration file for Avahi in `/etc/avahi/services` and 
restarts the Avahi daemon in order to register the new service.

From now on the hub will be discovered as an Avahi service. To verify that the 
server is visible run the following command (requires `avahi-utils`):

    $ avahi-browse -atr | grep cfenginehub

The sample output should look like this:

    eth0 IPv4 CFEngine Community 3.5.0 Policy Server on policy_hub_debian7  _cfenginehub._tcp    local

Once the hub is configured as an Avahi service, you can auto-bootstrap clients 
to it.

    $ /var/cfengine/bin/cf-agent -B :avahi

The clients require Avahi libraries to be installed in order to use this 
functionality. By default `cf-agent` looks for libraries in standard install 
locations. Install location may vary from system to system. If Avahi is 
installed in non-standard location (i.e. compiled from source) set the 
`AVAHI_PATH` environmental variable to specify path.

   $ AVAHI_PATH=/lib/libavahi-client.so.3 /var/cfengine/bin/cf-agent -B

If more than one server was found, or the server had more than one IP address, 
the list of all available servers will be printed and user will be asked to 
manually specify the IP address of the correct server by running standard 
bootstrap command of cf-agent:

   $ /var/cfengine/bin/cf-agent --bootstrap <IP address>

If only one Policy Server is found in the network cf-agent will perform the bootstrap without any further manual intervention of the user.

### Limitations:

Support ONLY for Linux, and automatic bootstrap is limited only to one subnet.
