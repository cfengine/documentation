---
layout: default
title: Installing CFEngine
sortkey: 1
categories: [Getting Started, Installation]
published: true
alias: getting-started-installation.html
tags: [getting started, installation]
---

-IMPORTANT NOTE: This is an early alpha release of 3.5, intended for testing 
-and showcase only. This version is not supported, not covered by service level 
-agreements (SLAs) and not intended for production environments. Do not upgrade 
-or use in conjuction with other versions at this point. We are planning 
-monthly snapshot (alpha) releases going forward, but official release date for 
-3.5 has not been set (expect it soon). See also 
-http://cfengine.com/blog/?page=4 for more information.
-<!--- TODO: move up when no longer a pre-release
--->
-

## Requirements

CFEngine recommends that your hub machine should have at least 2 GB of memory 
and a modern 64 bit processor. For a large number of clients we recommend, as 
a rule of thumb, to have 8 GB of memory available per 500 hosts bootstrapped 
to the hub (not applicable to CFEngine 3.5 Free Enterprise). Please contact your 
sales representative if you have any questions regarding these numbers. 

CFEngine recommends to have 256 MB available memory on the clients. For 
machines under CFEngine’s management (clients), a full installation of 
CFEngine 3.5 Enterprise requires about 25 MB of disk storage. Otherwise disk 
usage depends on your specific policies, especially those that concern 
reporting.

Verify that the machine’s network connection is working and that port 5308 
(used by CFEngine) and port 80 (used for the Mission Portal) are both open 
for both incoming and outgoing connections. A common problem is that iptables are 
active by default on some operating systems. Remember to stop this service or 
adapt it to allow for communication on the above ports. If applicable, typing 
the following two commands: "/etc/init.d/iptables stop" and "chkconfig 
iptables off".

A working package manager is required on the hub/policy server to install an 
Apache Web Server, php module, etc. You should start from a blank system (i.e. 
with none of these components installed) to avoid potential interference with 
the installation process. No special software is otherwise required on 
machines in your network, CFEngine bundles all critical dependencies in the 
CFEngine 3.5 Enterprise package (see also SOFTWARE DEPENDENCIES below).

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

----------------------------------------------------------------------------


INSTALLATION INSTRUCTIONS (CLEAN INSTALL)
-----------------------------------------
* Clean install is tested
* Do not upgrade from previous versions of CFEngine 3 Enterprise/Nova.
MC
* As always, install HUB first, then client(s).

 

Enterprise Package
------------------
CFEngine 3.5 Enterprise is provided in two packages (one hub and one client 
package). These are the two packages (inside the respective hub and client 
sections found under each platform in the software listing, example for 64 bit 
rpm packages).

The general form for the enterprise package names are given below.

Hub:

Debian Package:
cfengine-nova-hub_3.5.0XXXX_amd64.deb

RPM Package:
cfengine-nova-hub-3.5.0XXXX.x86_64.rpm


Client:

Debian Package:
cfengine-nova_3.5.0XXXX_amd64.deb or cfengine-nova_3.5.0XXXX_i386.deb

RPM Package:
cfengine-nova-3.5.0-XXXX.i386.rpm or cfengine-nova-3.5.0-XXXX.x86_64.rpm


Community Package
-----------------
The community edition is supplied in a single archive. Upon 
installation on two or more hosts, the role of policy server is adopted by
the first host that is bootstrapped to by another host. After boostrapping,
running the following command on a host will show whether or not it is the 
hub (policy server):
 
	/var/cfengine/bin/cf-promises -v

If the host is currently a hub, the am_policy_hub class should
be set.

The general form for the community package names are given below.

RPM Package:
cfengine-community-3.5.0XXXX.x86_64.rpm

Debian Package:
cfengine-community_3.5.0XXX_amd64.deb

Note
----
RedHat 6 Users: RedHat have split their main repository into several repositories. Some of our dependencies used to be in the main repository but have been moved to the Server Optional repository. Please make sure you have that repository configured before installing CFEngine Enterprise 3.5

Installing the Enterprise RPM Package
-------------------------------------
1. Copy the CFEngine 3.5 Enterprise packages to their respective systems - i.e hub package copied to policy server host and other package to each of the agents.
2. On the hub/policy server:
   a) Unpack the cfengine-nova-hub package:
      [RedHat/CentOS/SUSE]
        $ rpm -i <hub package>.rpm 
   b)(Skip for CFEngine 3.5 Free Enterprise): Send the hub's public key (/var/cfengine/ppkeys/localhost.pub) to CFEngine support to obtain a license 
   c)(Skip for CFEngine 3.5 Free Enterprise): Copy the obtained license file to /var/cfengine/masterfiles/license.dat
3. On the clients: Unpack the cfengine-nova package:
   [RedHat/CentOS/SUSE]
     $ rpm -i <agent package>.rpm (NOTE: use client package)
4. Bootstrap the machines to the hub (starting with bootstrapping the hub to itself. NOTE: please see AUTO-BOOTSTRAP INSTRUCTIONS for an alternative to this step): 
     $ /var/cfengine/bin/cf-agent --bootstrap <IP ADDRESS OF HUB>
6. CFEngine should now be up and running on your system. The Mission Portal will not be immediately accessible, you should wait approximately 10-15 minutes for the system to converge before attempting to connect to the hub IP-address through your web browser. 

Installing the Enterprise Debian Package
----------------------------------------
The same as for RPM except you should use the following command to do the install for each package:
	 [Ubuntu/Debian]
	 Hub:
           $ dpkg -i <hub package>.deb 
	 Agent:
           $ dpkg -i <agent package>.deb
           
See Enterprise 3.5 Owner's Manual for more detailed installation instructions and troubleshooting tips.

If you wish to manually install cfmod to the machine, you'll need to do the following:
1. Make a symlink from php library directory (typically something like
     /usr/lib/php5/20100525) to $installdir/lib/php/cfmod.so
2. Put a configuration file (with .ini extension) to php configuration directory (typically something like /etc/php5/conf.d):
     extension=cfmod.so



----------------------------------------------------------------------------
AUTO-BOOTSTRAP INSTRUCTIONS

Automatic bootstrap using Avahi implementation of zeroconf (a set of protocols and techniques user to create an IP network without special configuration servers or manual intervention of operator).

Requirements:
 - libavahi-client
 - libavahi-common

What is automatic bootstrap?
Automatic bootstrap allows the user to connect a CFEngine client to a hub/policy server without specifing the IP address manually. 
It uses the Avahi service discovery to locate the hub, obtain its IP address and connect to it. To use automatic bootstrap
installation of Avahi libraries is required.

How does it work?

1. Preparing the hub/policy server:
After setting up the hub it is required to register it as an Avahi service. To do this run the following command:
   $> /var/cfengine/bin/cf-serverd -A
This will generate the configuration file for Avahi in /etc/avahi/services and restarts Avahi daemon in order to register the new service.
From now on the hub will be discovered as an Avahi service. To verify that server is visible run the following command(requires avahi-utils):
   $> avahi-browse -atr | grep cfenginehub
The sample output should look like this:
   eth0 IPv4 CFEngine Community 3.5.0a1.fdf65b3 Policy Server on policy_hub_debian7  _cfenginehub._tcp    local
Once the hub is configured as Avahi service users can auto-bootstrap clients to it.

2. Bootstraping clients:
The clients require Avahi libraries to be installed in order to use this functionality. By default cf-agent looks for libraries in standard install locations. Install location may vary from system to system. If Avahi is installed in non-standard location (i.e. compiled from source) please use AVAHI_PATH environmental variable to specify path.
Sample command:
   $> AVAHI_PATH=/lib/libavahi-client.so.3 /var/cfengine/bin/cf-agent -B
If Avahi is installed in standard location specifing AVAHI_PATH variable is not required. Sample command to run automatic bootstrap:
   $> /var/cfengine/bin/cf-agent -B
cf-agent will not bootstrap if no hub/policy server was found in the network. If more than one server was found, or the server had more than one IP address, the list of all available servers will be printed and user will be asked to manually specify the IP address of the correct server by running starndard bootstrap command of cf-agent:
   $> /var/cfengine/bin/cf-agent --bootstrap <IP address>
If only one Policy Server is found in the network cf-agent will perform the bootstrap without any further manual intervention of the user.

Limitations:
Support ONLY for Linux.
Automatic bootstrap is limited only to one subnet.
This feature requires Policy Server machine to have only one IP address. With more IP adrresses i.e IPv4 and IPv6 at the same time server will be discovered as two different machines and user will be asked to specify IP address manually while bootstrap. Similar situation will occure when machine have more than one network interface installed.

----------------------------------------------------------------------------


CFEngine is currently tested on the following OS platforms:

Debian 6
RHEL 5
RHEL 6
Suse Linux Enterprise (SLES) 11
Ubuntu 10 and Ubuntu 12
Solaris 10 (Intel and Sparc)







