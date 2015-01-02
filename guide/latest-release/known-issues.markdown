---
layout: default
title: Known Issues
sorting: 50
published: true
tags: [overviews, releases, latest release, "3.6", platforms, versions, known issues]
---

CFEngine defects are managed in our [bug tracker][bug tracker]. Please report
bugs or unexpected behavior there, following the documented guideline for new
bug reports.

The items below highlight issues that require additional awareness when starting
with CFEngine or when upgrading from a previous version.


### Constant variables do not work, variables are always overrideable

https://dev.cfengine.com/issues/1492

### Showing Classes and variables with cf-promsies

`cf-promises --show-classes` and `cf-promises --show-vars` will only show
classes and variables found on a first pass through the policy, since
`cf-promises` does not evaluate agent promises.

### Protocol incompatibility between

The CFEngine protocol versions 1 and 2 are incompatible (the latter is based
on TLS).  You must migrate your entire site to 3.6 **or** run a second policy
server **or** arrange for an alternate policy distribution method when the
policy server is not available.


### RHEL / CentOS 7 and systemd ###

* Installing the Community Edition gives the following message, but it should be silent:

    Starting cfengine3 (via systemctl):                        [  OK  ]

* Starting the CFEngine daemons from policy, e.g. bootstrapping, does not make systemd aware that CFEngine is running. Thus, using systemd while removing the rpm, starting, stopping CFEngine is not handled correctly.


### Solaris 11 specific ###

*  Some important system information is missing from the Solaris 11 inventory report, as well as from CFEngine hard classes and system variables. The workaround is to use system tools to obtain the required information and set classes based on this.
        * MAC address
        * Network interfaces


### HP-UX specific ###

* [Package promises][packages] do not have out-of-the-box support for the HP-UX specific package manager. The workaround is to call the package manager directly using [commands promises][commands].
* Some important system information is missing from the HP-UX inventory report, as well as from CFEngine hard classes and system variables. The workaround is to use system tools to obtain the required information and set classes based on this.
        * MAC address
        * Network interfaces
        * Disk free
        * Memory size
        * Several OS and architecture specific attributes
                * System version
                * System serial number
                * System manufacturer
                * CPU model
                * BIOS version
                * BIOS vendor
* [User promises][users] do not work reliably on HP-UX. It is recommended not to use them at this time. The workaround is to call the useradd/usermod/userdel tools directly.
* [Process promises][processes] promises do not work reliably on HP-UX. The recommended workaround is to use the `ps` and `kill` tools directly using [commands promises][commands].
* [`edit_xml` bundles][bundle edit_xml] do not work on HP-UX.
