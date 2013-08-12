---
layout: default
title: sys
categories: [Reference, Special Variables, sys]
published: true
alias: reference-special-variables-context-sys.html
tags: [reference, variables, sys, discovery, system, inventory]
---

System variables are derived from CFEngine's automated discovery of system 
values. They are provided as variables in order to make automatically adaptive 
rules for configuration.

```cf3
    files:

      "$(sys.resolv)"

          create        => "true",
          edit_line     => doresolv("@(this.list1)","@(this.list2)"),
          edit_defaults => reconstruct;
```

### sys.arch

The variable gives the kernel's short architecture description.

```cf3
    # arch = x86_64
```

### sys.bindir

The name of the directory where CFEngine looks for its binaries..

```cf3
    # bindir = /var/cfengine/bin
```

**History:** Introduced in CFEngine 3.6

### sys.cdate

The date of the system in canonical form, i.e. in the form of a class.

```cf3
    # cdate = Sun_Dec__7_10_39_53_2008_
```

### sys.cf_promises

A variable containing the path to the CFEngine syntax analyzer
`cf-promises` on the platform you are using.

```cf3
    classes:

      "syntax_ok" expression => returnszero("$(sys.cf_promises)");
```

### sys.cf_version

The variable gives the version of the running CFEngine Core.

```cf3
    # cf_version = 3.0.5
```

### sys.cf_version_major

The variable gives the major version of the running CFEngine Core.

```cf3
    # cf_version = 3.0.5
    # cf_version_major = 3
```

**History:** Was introduced in 3.5.1, Enterprise 3.5.1.

### sys.cf_version_minor

The variable gives the minor version of the running CFEngine Core.

```cf3
    # cf_version = 3.0.5
    # cf_version_minor = 0
```

**History:** Was introduced in 3.5.1, Enterprise 3.5.1.

### sys.cf_version_patch

The variable gives the patch version of the running CFEngine Core.

```cf3
    # cf_version = 3.0.5
    # cf_version_patch = 5
```

**History:** Was introduced in 3.5.1, Enterprise 3.5.1.

### sys.class

This variable contains the name of the hard-class category for this host
(i.e. its top level operating system type classification).

```cf3
    # class = linux
```

**See also:** [`sys.os`][sys#sys.os]

### sys.cpus

A variable containing the number of CPU cores detected. On systems which
provide virtual cores, it is set to the total number of virtual, not
physical, cores. In addition, on a single-core system the class `1_cpu`
is set, and on multi-core systems the class *n*`_cpus` is set, where
*n* is the number of cores identified.

```cf3
    reports:

     "Number of CPUS = $(sys.cpus)";
     8_cpus::
       "This system has 8 processors.";
```

**History:** Was introduced in 3.3.0, Enterprise 2.2.0 (2012)

### sys.crontab

The variable gives the location of the current users's master crontab
directory.

```cf3
    # crontab = /var/spool/crontab/root 
```

### sys.date

The date of the system as a text string.

```cf3
    # date = Sun Dec  7 10:39:53 2008
```

### sys.doc_root

A scalar variable containing the default path for the document root of
the standard web server package.

**History:** Was introduced in 3.1.0, Enterprise 2.0.

### sys.domain

The domain name as discovered by CFEngine. If the DNS is in use, it could
be possible to derive the domain name from its DNS registration, but in
general there is no way to discover this value automatically. The
`common control` body permits the ultimate specification of this value.

```cf3
    # domain = example.org
 
```

### sys.enterprise_version

The variable gives the version of the running CFEngine Enterprise
Edition.

```cf3
    # enterprise_version = 3.0.0
```

**History:** Was introduced in 3.5.0, Enterprise 3.0.0

### sys.expires

```cf3
    reports:

     enterprise::

      "License expires $(sys.expires)";
```

### sys.exports

The location of the system NFS exports file.

```cf3
    # exports = /etc/exports
    # exports = /etc/dfs/dfstab
```

### sys.failsafe

The name of the failsafe policy file.

```cf3
    # failsafe = /var/cfengine/inputs/failsafe.cf
```

**History:** Introduced in CFEngine 3.6

### sys.flavor, sys.flavour

A variable containing an operating system identification string that is
used to determine the current release of the operating system in a form
that can be used as a label in naming. This is used, for instance, to
detect which package name to choose when updating software binaries for
CFEngine.

These two variables are synonyms for each other.

**History:** Was introduced in 3.2.0, Enterprise 2.0

**See also:** [`sys.ostype`][sys#sys.ostype]

### sys.fqhost

The fully qualified name of the host. In order to compute this value
properly, the domain name must be defined.

```cf3
    # fqhost = host.example.org
```

**See also:** [`sys.uqhost`][sys#sys.uqhost]

### sys.fstab

The location of the system filesystem (mount) table.

```cf3
    # fstab = /etc/fstab
```

### sys.hardware_addresses

This is a list variable containing a list of all known MAC addresses for
system interfaces.

**History:** Was introduced in 3.3.0, Enterprise 2.2.0 (2011)

### sys.hardware_mac[interface_name]

This contains the MAC address of the named interface. For example:

```cf3
    reports:
        "Tell me $(harware_mac[eth0])";
```

**History:** Was introduced in 3.3.0, Enterprise 2.2.0 (2011)

### sys.host

The name of the current host, according to the kernel. It is undefined
whether this is qualified or unqualified with a domain name.

```cf3
    # host = myhost
```

### sys.inputdir

The name of the inputs directory where CFEngine looks for its policy files.

```cf3
    # inputdir = /var/cfengine/inputs
```

**History:** Introduced in CFEngine 3.6

### sys.interface

The assumed (default) name of the main system interface on this host.

```cf3
    # interface = eth0
```

### sys.interfaces

Displays a system list of configured interfaces currently active in use
by the system. This list is detected at runtime and it passed in the
variables report to the CFEngine Enterprise Database.

To use this list in a policy, you will need a local copy since only
local variables can be iterated.

```cf3
    bundle agent test
    {
    vars:

     # To iterate, we need a local copy

     "i1" slist => { @(sys.ip_addresses)} ;
     "i2" slist => { @(sys.interfaces)} ;

    reports:

        "Addresses: $(i1)";
        "Interfaces: $(i2)";
        "Addresses of the interfaces: $(sys.ipv4[$(i2)])";
    }
```

**History:** Was introduced in 3.3.0, Enterprise 2.2.0 (2011)

### sys.interface_flags

Contains a space separated list of the flags of the named interface. e.g.

```cf3
    reports:
        "eth0 flags: $(sys.interface_flags[eth0])";
```

Outputs:

    R: eth0 flags: up broadcast running multicast


The following device flags are supported: 

* up
* broadcast
* debug
* loopback
* pointopoint
* notrailers
* running
* noarp
* promisc
* allmulti
* multicast

**History:** Was introduced in 3.5.0 (2013)

### sys.ip_addresses

Displays a system list of IP addresses currently in use by the system.
This list is detected at runtime and passed in the variables report to the 
CFEngine Enterprise Database.

To use this list in a policy, you will need a local copy since only
local variables can be iterated.

```cf3
    bundle agent test
    {
    vars:

     # To iterate, we need a local copy

     "i1" slist => { @(sys.ip_addresses)} ;
     "i2" slist => { @(sys.interfaces)} ;

    reports:

        "Addresses: $(i1)";
        "Interfaces: $(i2)";
        "Addresses of the interfaces: $(sys.ipv4[$(i2)])";
    }
```

**History:** Was introduced in 3.3.0, Enterprise 2.2.0 (2011)

### sys.ipv4

All four octets of the IPv4 address of the first system interface.

**Note**:  

If your system has a single ethernet interface, `$(sys.ipv4)` will contain 
your IPv4 address. However, if your system has multiple interfaces, then 
`$(sys.ipv4)` will simply be the IPv4 address of the first interface in the 
list that has an assigned address, Use `$(sys.ipv4[interface_name])` for 
details on obtaining the IPv4 addresses of all interfaces on a system.

### sys.ipv4[interface_name]

The full IPv4 address of the system interface named as the associative
array index, e.g. `$(ipv4[le0])` or `$(ipv4[xr1])`.

```cf3
    # If the IPv4 address on the interfaces are
    #    le0 = 192.168.1.101
    #    xr1 = 10.12.7.254
    #
    # Then the octets of all interfaces are accessible as an associative array
    # ipv4_1[le0] = 192
    # ipv4_2[le0] = 192.168
    # ipv4_3[le0] = 192.168.1
    #   ipv4[le0] = 192.168.1.101
    # ipv4_1[xr1] = 10
    # ipv4_2[xr1] = 10.12
    # ipv4_3[xr1] = 10.12.7
    #   ipv4[xr1] = 10.12.7.254
```

**Note**:  

The list of interfaces may be acquired with `getindices("sys.ipv4")` (or
from any of the other associative arrays). Only those interfaces which
are marked as "up" and have an IP address will be listed.

### sys.ipv4_1[interface_name]


The first octet of the IPv4 address of the system interface named as the
associative array index, e.g. `$(ipv4_1[le0])` or `$(ipv4_1[xr1])`.

### sys.ipv4_2[interface_name]

The first two octets of the IPv4 address of the system interface named as the associative array index, e.g. `$(ipv4_2[le0])` or `$(ipv4_2[xr1])`.

### sys.ipv4_3[interface_name]

The first three octets of the IPv4 address of the system interface named as the associative array index, e.g. `$(ipv4_3[le0])` or `$(ipv4_3[xr1])`.

### sys.libdir

The name of the directory where CFEngine looks for its libraries.

```cf3
    # libdir = /var/cfengine/inputs/lib/3.6
```

**History:** Introduced in CFEngine 3.6

### sys.local_libdir

The name of the directory where CFEngine looks for its libraries, without any prefixes.

```cf3
    # local_libdir = lib/3.6
```

**History:** Introduced in CFEngine 3.6

### sys.license_owner

```cf3
    reports:

     enterprise::

      "This version of CFEngine is licensed to $(sys.license_owner)";
```

**History:** Was introduced in version 3.1.4,Enterprise 2.0.2 (2011)

### sys.licenses_granted

```cf3
    reports:

     enterprise::

      "There are $(sys.licenses_granted) licenses granted for use";
```

**History:** Was introduced in version 3.1.4,Enterprise 2.0.2 (2011)

### sys.long_arch

The long architecture name for this system kernel. This name is
sometimes quite unwieldy but can be useful for logging purposes.

```cf3
    # long_arch = linux_x86_64_2_6_22_19_0_1_default__1_SMP_2008_10_14_22_17_43__0200
```

**See also:** [`sys.ostype`][sys#sys.ostype]

### sys.maildir

The name of the system email spool directory.

```cf3
    # maildir = /var/spool/mail
```

### sys.masterdir

The name of the directory on the hub where CFEngine looks for inputs to be validated and copied into `sys.inputdir`.

```cf3
    # masterdir = /var/cfengine/masterfiles
```

**History:** Introduced in CFEngine 3.6

<!---
### sys.nova_version

The variable gives the version of the running CFEngine Enterprise Edition.

```cf3
# nova_version = 1.1.3
```
-->

### sys.os

The name of the operating system according to the kernel.

```cf3
    # os = linux
```

**See also:** [`sys.ostype`][sys#sys.ostype]

### sys.ostype

Another name for the operating system.

```cf3
    # ostype = linux_x86_64
```

**See also:** [`sys.class`][sys#sys.class]

### sys.policy_hub

Hostname of the machine acting as the policy server. This value is set
during bootstrap. In case bootstrap was not performed, it is set to
undefined.

```cf3
    reports:

     "Policy hub is $(sys.policy_hub)";
```

**History:** Was introduced in version 3.1.0b1,Enterprise 2.0.0b1 (2010).
Available in Community since 3.2.0

### sys.release

The kernel release of the operating system.

```cf3
    # release = 2.6.22.19-0.1-default
```

### sys.resolv

The location of the system resolver file.

```cf3
    # resolv = /etc/resolv.conf
```

### sys.sysday

A variable containing the time since the UNIX Epoch (00:00:00 UTC, January 1,
1970), measured in days. It is equivalent to `$(sys.systime)` divided by the
number of seconds in a day, expressed as an integer. No time zone conversion
is performed, the direct result of the time() system call is used. This value
is most commonly used in the /etc/shadow file.

```cf3
   # sysday = 15656

   Corresponds to Monday, November 12, 2012.
```

**History:** Introduced in CFEngine 3.6

### sys.systime

A variable containing the result of the time() system call, which is the
time since the UNIX Epoch (00:00:00 UTC, January 1, 1970), measured in
seconds. See also `$(sys.sysday)`.

```cf3
   # systime = 1352754900

   Corresponds to Mon Nov 12 21:15:00 2012 UTC.
```

**History:** Introduced in CFEngine 3.6

### sys.update

The name of the update policy file.

```cf3
    # update = /var/cfengine/inputs/update.cf
```

**History:** Introduced in CFEngine 3.6

### sys.uptime

A variable containing the number of minutes which the system has been
online.  (Not implemented on the Windows platform.)

```cf3
   # uptime = 69735

   Equivalent uptime command output:
    16:24:52 up 48 days, 10:15,  1 user,  load average: 0.00, 0.00, 0.00
```

**History:** Introduced in CFEngine 3.6

### sys.uqhost

The unqualified name of the current host.

```cf3
    # uqhost = myhost
```

**See also:** [`sys.fqhost`][sys#sys.fqhost]

### sys.version

The version of the running kernel. On Linux, this corresponds to the
output of `uname -v`.

```cf3
    # version = #55-Ubuntu SMP Mon Jan 10 23:42:43 UTC 2011
```

**History:** Was introduced in version 3.1.4,Enterprise 2.0.2 (2011)

### sys.windir

On the Windows version of CFEngine Enterprise, this is the path to the Windows
directory of this system.

```cf3
    # windir = C:\WINDOWS
```

### sys.winprogdir

On the Windows version of CFEngine Enterprise, this is the path to the program
files directory of the system.

```cf3
    # winprogdir = C:\Program Files
```

### sys.winprogdir86

On 64 bit Windows versions of CFEngine Enterprise, this is the path to the 32
bit (x86) program files directory of the system.

```cf3
    # winprogdir86 = C:\Program Files (x86)
```

### sys.winsysdir

On the Windows version of CFEngine Enterprise, this is the path to the Windows
system directory.

```cf3
    # winsysdir = C:\WINDOWS\system32
```

### sys.workdir

The location of the CFEngine [work 
directory][The CFEngine Components#The Working Directory] and cache. 
For the system privileged user this is normally:

```cf3
    # workdir = /var/cfengine
```

For non-privileged users it is in the user's home directory:

```cf3
    # workdir = /home/user/.cfagent
```

On the Windows version of CFEngine Enterprise, it is normally under program
files (the directory name may change with the language of Windows):

```cf3
    # workdir = C:\Program Files\CFEngine
```
