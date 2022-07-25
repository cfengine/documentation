---
layout: default
title: Installing Enterprise for Production
published: true
sorting: 40
tags: [getting started, installation, enterprise production]
---

These instructions describe how to install the latest version of
CFEngine Enterprise in a production environment using pre-compiled rpm
and deb packages for Ubuntu, Debian, Redhat, CentOS, and SUSE.

## General Requirements

CFEngine recommends the following:

**Host Memory**

During normal operation the CFEngine processes consume about 30 MB of
resident memory (RSS) on hosts with the agent only (not acting as
Policy Server).

However there might be spikes due to e.g. commands executed from the
CFEngine policy so it is generally recommended to have at least 256 MB
available memory in order to run the CFEngine agent software.

**Host disk**

So that the agent is not affected by full disks it is recommended that
`/var/cfengine` be on its own partition.

On Unix-like systems, a 500 MB partition for `/var/cfengine` should give you
some breathing room, typical user reported sizes are in the 100-250 MB range. On
Windows systems, CFEngine consumes more space because Windows lacks support for
sparse files (which are used opportunistically by lmdb). 5 G of space should
provide some breathing room, typical user reported sizes for `C:\Program
Files\Cfengine` are around 1 GB. As always things vary in different environments
it's a good idea to measure consumption in your infrastructure and customize
accordingly.

The agent builds local differential reports for promise outcomes. The
longer the period between collections from the enterprise hub the more
resources are required to calculate these differentials. You can
control the maximum disk space used by diff reports (contexts,
variables, software installed, software patches, lastseen hosts and
promise executions) by adjusting `def.max_client_history_size`.

**Network**

* Verify that the machine’s network connection is working and that
  port 5308 (used by CFEngine) is open for both incoming and outgoing
  connections.

* If a firewall is active on your operating system, adapt it to it to
  allow for communication on port 5308 or disable it.

CFEngine bundles all critical dependencies into the package; therefore,
additional software is not required.

**Requirements for VIOS**

CFEngine Enterprise has
[Virtual I/O Server (VIOS) Recognized status](http://www.ibm.com/partnerworld/gsd/solutiondetails.do?solution=48493)
from IBM.  This means that CFEngine Enterprise has been technically
verified by IBM to be installed in and manage VIOS environments.

During testing, CFEngine Enterprise was seen to use up to 2% of the
VIOS CPU during `cf-agent` runs with the default CFEngine policy. The
resource utilization may vary depending on the policy CFEngine is
running.  The VIOS should be configured with Shared Processors in
Uncapped mode.

## Policy Server Requirements

Please note that the resource requirements below are meant as minimum
guidelines and have been obtained with synthetic testing, and it is
always better to leave some headroom if intermittent bottlenecks
should occur.  The key drivers for the vertical scalability of the
Policy Servers are 1) the number of agents bootstrapped and 2) the
size and complexity of the CFEngine policy.

### cfapache and cfpostgres users

The CFEngine Server requires two users: **cfapache** and
**cfpostgres**.  If these users do not exist during installation of
the server package, they will be created, so if there are constraints
on user creation, please ensure that these users exists prior to
installation.

These users are not required nor created by the agent package.

### Dedicated OS

The CFEngine Server is only supported when installed on a **dedicated,
vanilla OS** (i.e. it only has repositories and packages officially
supported by the OS vendor). This is because the CFEngine Server uses
services, e.g. apache, that are configured for CFEngine and may
conflict with other custom application configurations.

One option, especially for smaller installations, is to run the
CFEngine Server in a VM. But please consider the performance
requirements when doing this.

### CPU

A modern 64-bit processor with 12 or more cores for handling up to
5000 bootstrapped agents.  This number is also linear with respect to
the number of bootstrapped agents (so 6 cores would suffice for 2500
agents).

### Memory

Minimum 3GB memory (can run with less for small testing/lab environments), but
not lower than **8MB per bootstrapped agent**. This means that, for a server
with 5000 hosts, you should have at least 40GB of memory.

### Disk sizing and partitioning

So that the agent is not affected by full disks it is recommended that
`/var/cfengine` be on it's own partition.

It is recommended that `$(sys.workdir)/state/pg` is mounted on a
**separate disk**. This will give PostgreSQL, which can be very disk I/O
intensive, dedicated resources.

Plan for approximately **100MB of disk space per bootstrapped agent**.
This means that, for a server with 5000 hosts, you should have at
least 500 GB available on the database partition.

xfs is strongly recommended as the file system type for the file
system mounted on `$(sys.workdir)/state/pg`. ext4 can be used as an
alternative, but ext3 should be avoided.

### Disk speed

For 5000 bootstrapped agents, the disk that serves PostgreSQL
(`$(sys.workdir)/state/pg`) should be able to perform at least **1000
IOPS** (in 16KiB block size) and 10 MB/s. The disk mounted on
`$(sys.workdir)` should be able to perform at least 500 IOPS and 0.5
MB/s. **SSD is recommended** for the disk that serves PostgreSQL
(`$(sys.workdir)/state/pg`).

If you do not have separate partitions for `$(sys.workdir)` and
`$(sys.workdir)/state/pg`, the speed required by the disk serving
`$(sys.workdir)` adds up (for 5000 bootstrapped agents it would be
1500 IOPS and 10.5 MB/s).

**Note** Your storage IOPS specification may be given in 4KiB block
  size, in which case you would need to divide it by 4 to get the
  corresponding 16KiB *theoretical maximum*.

### Network

For serving policy and collecting reports for up to 5000 bootstrapped
agents, plan for at least 30 MB/s (240 MBit) speed on the interface
that connects the Policy Server with the agents.

### cf-serverd maxconnections

The maximum number of connections is the maximum number of sessions that
`cf-serverd` will support. The general rule of thumb is that it should be set to
**two times the number of clients** bootstrapped to the hub. So if you have 100
remote agents bootstrapped to your policy server, 200 would be a good value body
server control maxconnections.


### Open file descriptors

Open file descriptors should be set at least **two times body server control
maxconnections**. Adjust `soft` and `hard` `nofile` in `/etc/limits.conf` or
appropriate file in `/etc/limits.d/` accordingly for your platform.

For example, if you have 1000 remote agents, body server control maxconnections
should be set to 2000, and open file descriptors should be set to at least 4000.

`/etc/limits.d/90-nproc.conf`

```
soft nofile 4000
hard nofile 4000
```

Not sure what your open file limits for `cf-serverd` are? Inspect the current
limits with this command:

```
cat /proc/$(pgrep cf-serverd)/limits
```

## Download Packages

[Download CFEngine](http://cfengine.com/product/free-download)

## Install Packages

CFEngine Enterprise is provided in two packages; one is for the Policy
Server (hub) and the other is for each Host (client).

**Log in as root** and then follow these steps to install CFEngine
  Enterprise:


1. On the designated Policy Server, install the `cfengine-nova-hub` package:

    ```console
    [RedHat/CentOS/SUSE] # rpm -i <hub package>.rpm
    [Debian/Ubuntu]      # dpkg -i <hub package>.deb
    ```

2. On each Host, install the `cfengine-nova` package:

    ```console
    [RedHat/CentOS/SUSE] # rpm -i <agent package>.rpm
    [Debian/Ubuntu]      # dpkg -i <agent package>.deb
    [Solaris]            # pkgadd -d <agent package>.pkg all
    [AIX]                # installp -a -d <agent package>.bff cfengine.cfengine-nova
    [HP-UX]              # swinstall -s <full path to agent package>.depot cfengine-nova
    ```

Note: Install actions logged to `/var/logs/cfengine-install.log`.

## Bootstrap

Run the bootstrap command, **first** on the policy server and then on each
host:

```console
# /var/cfengine/bin/cf-agent --bootstrap <IP address of the Policy Server>
```

After bootstrapping the hub run the policy to complete the hub configuration.

```console
# /var/cfengine/bin/cf-agent -Kf update.cf; /var/cfengine/bin/cf-agent -K
```

## Licensed installations

If you are evaluating CFEngine Enterprise or otherwise using it in an
environment with less than 25 agents connecting to a Policy Server,
you do not need a license and there is no expiry.

If you are a customer, please send the Policy Server's public key
to CFEngine support to obtain a license.

It's best to pack the public key into an archive so that it does not
get corrupt in transit.

```console
# tar --create --gzip --directory /var/cfengine --file $(hostname)-ppkeys.tar.gz ppkeys/localhost.pub
```

CFEngine will send you a `license.dat` file. Install the obtained
license with `cf-key`.

```console
# cf-key --install-license ./license.dat
```

## Next Steps

When bootstrapping is complete, CFEngine is up and running on your system.

The Mission Portal is immediately accessible. Connect to the Policy Server
through your web browser at http://`<IP address of your Policy Server>`.

Learn more about CFEngine by using the following resources:

* Tutorial: [Tutorial for Running Examples][Examples and Tutorials#Tutorial for Running Examples]

* [CFEngine Guide][Guide]

* [Tutorials and Examples][Examples and Tutorials]
