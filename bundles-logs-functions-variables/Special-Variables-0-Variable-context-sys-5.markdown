---
layout: default
title: xxxx
categories: [xxx]
published: true
alias: Special-Variables-0-Variable-context-sys-5.markdown.html
tags: [xx]
---

### Variable context `sys`

\

System variables are derived from CFEngine's automated discovery of
system values. They are provided as variables in order to make
automatically adaptive rules for configuration. For example:

    files:

     any::

      "$(sys.resolv)"

          create        => "true",
          edit_line     => doresolv("@(this.list1)","@(this.list2)"),
          edit_defaults => reconstruct;

The above rule requires no class specification because the variable
itself is class-specific.

-   Variable sys.arch
-   Variable sys.cdate
-   Variable sys.cf\_promises
-   Variable sys.cf\_version
-   Variable sys.class
-   Variable sys.cpus
-   Variable sys.crontab
-   Variable sys.date
-   Variable sys.doc\_root
-   Variable sys.domain
-   Variable sys.enterprise\_version
-   Variable sys.expires
-   Variable sys.exports
-   Variable sys.flavor
-   Variable sys.flavour
-   Variable sys.fqhost
-   Variable sys.fstab
-   Variable sys.hardware\_addresses
-   Variable sys.hardware\_mac[interface\_name]
-   Variable sys.host
-   Variable sys.interface
-   Variable sys.interfaces
-   Variable sys.ip\_addresses
-   Variable sys.ipv4
-   Variable sys.ipv4[interface\_name]
-   Variable sys.ipv4\_1[interface\_name]
-   Variable sys.ipv4\_2[interface\_name]
-   Variable sys.ipv4\_3[interface\_name]
-   Variable sys.license\_owner
-   Variable sys.licenses\_granted
-   Variable sys.long\_arch
-   Variable sys.maildir
-   Variable sys.nova\_version
-   Variable sys.os
-   Variable sys.ostype
-   Variable sys.policy\_hub
-   Variable sys.release
-   Variable sys.resolv
-   Variable sys.uqhost
-   Variable sys.version
-   Variable sys.windir
-   Variable sys.winprogdir
-   Variable sys.winprogdir86
-   Variable sys.winsysdir
-   Variable sys.workdir

#### Variable sys.arch

\

The variable gives the kernel's short architecture description.

    # arch = x86_64

#### Variable sys.cdate

\

The date of the system in canonical form, i.e. in the form of a class.

    # cdate = Sun_Dec__7_10_39_53_2008_

#### Variable sys.cf\_promises

\

A variable containing the path to the CFEngine syntax analyxer
`cf-promises` on the platform you are using.

    classes:

      "syntax_ok" expression => returnszero("$(sys.cf_promises)");

#### Variable sys.cf\_version

\

The variable gives the version of the running CFEngine Community
Edition.

    # cf_version = 3.0.5 

#### Variable sys.class

\

This variable contains the name of the hard-class category for this host
(i.e. its top level operating system type classification).

    # class = linux

#### Variable sys.cpus

\

*History*: Was introduced in 3.3.0, Nova 2.2.0 (2012)

A variable containing the number of CPU cores detected. On systems which
provide virtual cores, it is set to the total number of virtual, not
physical, cores. In addition, on a single-core system the class "1\_cpu"
is set, and on multi-core systems the class "*n*\_cpus" is set, where
"*n*" is the number of cores identified.

    reports:

     cfengine_3::

       "Number of CPUS = $(sys.cpus)";

     8_cpus::
       "This system has 8 processors.";

#### Variable sys.crontab

\

The variable gives the location of the current users's master crontab
directory.

    # crontab = /var/spool/crontas/root 

#### Variable sys.date

\

The date of the system as a text string.

    # date = Sun Dec  7 10:39:53 2008

#### Variable sys.doc\_root

\

*History*: Was introduced in 3.1.0, Nova 2.0.

A scalar variable containing the default path for the document root of
the standard web server package.

#### Variable sys.domain

\

The domain name as divined by CFEngine. If the DNS is in use, it could
be possible to derive the domain name from its DNS regisration, but in
general there is no way to discover this value automatically. The
`common control` body permits the ultimate specification of this value.

    # domain = example.org
     

#### Variable sys.enterprise\_version

\

*History*: Was introduced in 3.5.0, Enterprise 3.0.0

The variable gives the version of the running CFEngine Enterprise
Edition.

    # enterprise_version = 3.0.0

#### Variable sys.expires

\

    reports:

     nova::

      "License expires $(sys.expires)";

#### Variable sys.exports

\

The location of the system NFS exports file.

    # exports = /etc/exports
    # exports = /etc/dfs/dfstab

#### Variable sys.flavor

\

*History*: Was introduced in 3.2.0, Nova 2.0

A variable containing an operating system identification string that is
used to determine the current release of the operating system in a form
that can be used as a label in naming. This is used, for instance, to
detect which package name to choose when updating software binaries for
CFEngine.

This is a synonym for `$(sys.flavour)`.

#### Variable sys.flavour

\

*History*: Was introduced in 3.2.0, Nova 2.0

A variable containing an operating system identification string that is
used to determine the current release of the operating system in a form
that can be used as a label in naming. This is used, for instance, to
detect which package name to choose when updating software binaries for
CFEngine.

This is a synonym for `$(sys.flavor)`.

#### Variable sys.fqhost

\

The fully qualified name of the host. In order to compute this value
properly, the domain name must be defined.

    # fqhost = host.example.org

#### Variable sys.fstab

\

The location of the system filesystem (mount) table.

    # fstab = /etc/fstab

#### Variable sys.hardware\_addresses

\

*History*: Was introduced in 3.3.0, Nova 2.2.0 (2011)

This is a list variable containing a list of all known MAC addresses for
system interfaces.

#### Variable sys.hardware\_mac[interface\_name]

\

*History*: Was introduced in 3.3.0, Nova 2.2.0 (2011)

This contains the MAC address of the named interface. For example:

    reports:

      linux::

        "Tell me $(harware_mac[eth0])";

#### Variable sys.host

\

The name of the current host, according to the kernel. It is undefined
whether this is qualified or unqualified with a domain name.

    # host = myhost

#### Variable sys.interface

\

The assumed (default) name of the main system interface on this host.

    # interface = eth0

#### Variable sys.interfaces

\

*History*: Was introduced in 3.3.0, Nova 2.2.0 (2011)

Displays a system list of configured interfaces currently active in use
by the system. This list is detected at runtime and it passed in the
variables report to a Mission Portal in commercial editions of CFEngine.

To use this list in a policy, you will need a local copy since only
local variables can be iterated.

    bundle agent test
    {
    vars:

     # To iterate, we need a local copy

     "i1" slist => { @(sys.ip_addresses)} ;
     "i2" slist => { @(sys.interfaces)} ;

    reports:

      cfengine::

        "Addresses: $(i1)";
        "Interfaces: $(i2)";
        "Addresses of the interfaces: $(sys.ipv4[$(i2)])";

    }

#### Variable sys.ip\_addresses

\

*History*: Was introduced in 3.3.0, Nova 2.2.0 (2011)

Displays a system list of IP addresses currently in use by the system.
This list is detected at runtime and passed in the variables report to a
Mission Portal in commercial editions of CFEngine.

To use this list in a policy, you will need a local copy since only
local variables can be iterated.

    bundle agent test
    {
    vars:

     # To iterate, we need a local copy

     "i1" slist => { @(sys.ip_addresses)} ;
     "i2" slist => { @(sys.interfaces)} ;

    reports:

      cfengine::

        "Addresses: $(i1)";
        "Interfaces: $(i2)";
        "Addresses of the interfaces: $(sys.ipv4[$(i2)])";

    }

#### Variable sys.ipv4

\

All four octets of the IPv4 address of the first system interface.

**Note**:\

If your system has a single ethernet interface, \$(sys.ipv4) will
contain your IPv4 address. However, if your system has multiple
interfaces, then \$(sys.ipv4) will simply be the IPv4 address of the
first interface in the list that has an assigned address, See Variable
sys.ipv4[interface\_name], for details on obtaining the IPv4 addresses
of all interfaces on a system.

#### Variable sys.ipv4[interface\_name]

\

The full IPv4 address of the system interface named as the associative
array index, e.g. \$(ipv4[le0]) or \$(ipv4[xr1]).

    # If the IPv4 address on the interfaces are
    #        le0 = 192.168.1.101
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

**Note**:\

The list of interfaces may be acquired with getindices("sys.ipv4") (or
from any of the other associative arrays). Only those interfaces which
are marked as "up" and have an IP address will be listed.

#### Variable sys.ipv4\_1[interface\_name]

\

The first octet of the IPv4 address of the system interface named as the
associative array index, e.g. \$(ipv4\_1[le0]) or \$(ipv4\_1[xr1]) (See
Variable sys.ipv4[interface\_name]).

#### Variable sys.ipv4\_2[interface\_name]

\

The first two octets of the IPv4 address of the system interface named
as the associative array index, e.g. \$(ipv4\_2[le0]) or
\$(ipv4\_2[xr1]) (See Variable sys.ipv4[interface\_name]).

#### Variable sys.ipv4\_3[interface\_name]

\

The first three octets of the IPv4 address of the system interface named
as the associative array index, e.g. \$(ipv4\_3[le0]) or
\$(ipv4\_3[xr1]) (See Variable sys.ipv4[interface\_name]).

#### Variable sys.license\_owner

\

*History*: Was introduced in version 3.1.4,Nova 2.0.2 (2011)

    reports:

     nova::

      "This version of CFEngine is licensed to $(sys.license_owner)";

#### Variable sys.licenses\_granted

\

*History*: Was introduced in version 3.1.4,Nova 2.0.2 (2011)

    reports:

     nova::

      "There are $(sys.licenses_granted) licenses granted for use";

#### Variable sys.long\_arch

\

The long architecture name for this system kernel. This name is
sometimes quite unwieldy but can be useful for logging purposes.

    # long_arch = linux_x86_64_2_6_22_19_0_1_default__1_SMP_2008_10_14_22_17_43__0200

#### Variable sys.maildir

\

The name of the system email spool directory.

    # maildir = /var/spool/mail

#### Variable sys.nova\_version

\

The variable gives the version of the running CFEngine Nova Edition.

    # nova_version = 1.1.3

#### Variable sys.os

\

The name of the operating system according to the kernel.

    # os = linux

#### Variable sys.ostype

\

Another name for the operating system.

    # ostype = linux_x86_64

#### Variable sys.policy\_hub

\
 Hostname of the machine acting as a policy hub. This value is set
during bootstrap. In case bootstrap was not performed, it is set to
undefined.

**History**: Was introduced in version 3.1.0b1,Nova 2.0.0b1 (2010).
Available in Community since 3.2.0

    reports:

     "Policy hub is $(sys.policy_hub)";

#### Variable sys.release

\

The kernel release of the operating system.

    # release = 2.6.22.19-0.1-default

#### Variable sys.resolv

\

The location of the system resolver file.

    # resolv = /etc/resolv.conf

#### Variable sys.uqhost

\

The unqualified name of the current host. See also `sys.fqhost`.

    # uqhost = myhost

#### Variable sys.version

\

The version of the running kernel. On Linux, this corresponds to the
ouput of `uname -v`.

    # version = #55-Ubuntu SMP Mon Jan 10 23:42:43 UTC 2011

*History*: Was introduced in version 3.1.4,Nova 2.0.2 (2011)

#### Variable sys.windir

\

On the Windows version of CFEngine Nova, this is the path to the Windows
directory of this system.

    # windir = C:\WINDOWS

#### Variable sys.winprogdir

\

On the Windows version of CFEngine Nova, this is the path to the program
files directory of the system.

    # winprogdir = C:\Program Files

#### Variable sys.winprogdir86

\

On 64 bit Windows versions of CFEngine Nova, this is the path to the 32
bit (x86) program files directory of the system.

    # winprogdir86 = C:\Program Files (x86)

#### Variable sys.winsysdir

\

On the Windows version of CFEngine Nova, this is the path to the Windows
system directory.

    # winsysdir = C:\WINDOWS\system32

#### Variable sys.workdir

\

The location of the CFEngine work directory and cache. For the system
privileged user this is normally:

    # workdir = /var/cfengine

For non-privileged users it is in the user's home directory:

    # workdir = /home/user/.cfagent

On the Windows version of CFEngine Nova, it is normally under program
files (the directory name may change with the language of Windows):

    # workdir = C:\Program Files\CFEngine
