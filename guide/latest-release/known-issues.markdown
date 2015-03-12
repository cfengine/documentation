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
on TLS). CFEngine 3.6 supports both protocol versions, but earlier versions
only support protocol version 1. Protocol version 1 is still the default in
3.6 but the default will change to 2 in future versions.


### RHEL 7 / CentOS 7 ###

* The CFEngine Enterprise hub does not yet support RHEL 7 / CentOS 7
* The community package repositories hosted by CFEngine does not have the RHEL 7 /CentOS 7 package. Please download and install the package separately.
* If you use the community edition as a Policy Server on RHEL 7 / CentOS 7 you will see "Failed to start the server" when you bootstrap it to itself. This message is harmless and will be removed in future releases.


### HP-UX specific ###

* [Package promises][packages] do not have out-of-the-box support for the HP-UX specific package manager. The workaround is to call the package manager directly using [commands promises][commands].
* Some important system information is missing from the HP-UX inventory report, as well as from CFEngine hard classes and system variables. The workaround is to use system tools to obtain the required information and set classes based on this.
        * Disk free
        * Memory size
        * Several OS and architecture specific attributes
                * System version
                * System serial number
                * System manufacturer
                * CPU model
                * BIOS version
                * BIOS vendor
* [User promises][users] do not work reliably on HP-UX. It is recommended not to use them at this time. The workaround is to call the useradd/usermod/userdel tools directly.  (fixed in CFEngine 3.6.4)
* [Process promises][processes] depend on the `ps` native tool, which by default truncates lines at 128 columns on HP-UX. It is recommended to edit the file `/etc/default/ps` and increase the `DEFAULT_CMD_LINE_WIDTH` setting to 1024 to guarantee that process promises will work smoothly on the platform.
* [`edit_xml` bundles][bundle edit_xml] do not work on HP-UX. (fixed in CFEngine 3.6.4)

### Enterprise emails sent for alert noticies come from 'admin@orginization.com'.
There is currently no setting in Mission Portal to configure the sender email
address. This issue is on the [backlog](https://dev.cfengine.com/issues/6726)
and will be addressed in a future release.

To change the setting you must edit the from email address in
`/var/cfengine/httpd/htdocs/application/config/appsettings.php`

```
// Default FROM email address
$config['appemail'] = 'admin@organisation.com';
```

### Enterprise reports not collected from 3.5
CFEngine Enterprise 3.6 has a new diff-based report collection mechanism,
and so a 3.6 hub cannot collect reports from 3.5 or earlier agents.

Currently the 3.5 agents will not show in Mission Portal at all, but
you will see them by running `cf-key -s` on the hub.
