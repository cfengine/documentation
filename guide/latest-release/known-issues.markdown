---
layout: default
title: Known Issues
sorting: 50
published: true
tags: [overviews, releases, latest release, "3.8", platforms, versions, known issues]
---

CFEngine defects are managed in our [bug tracker][bug tracker]. Please report
bugs or unexpected behavior there, following the documented guideline for new
bug reports.

The items below highlight issues that require additional awareness when starting
with CFEngine or when upgrading from a previous version.

### HP-UX specific

* [Package promises][packages] do not have out-of-the-box support for the HP-UX
  specific package manager. The workaround is to call the package manager
  directly using [commands promises][commands].
* Some important system information is missing from the HP-UX inventory report,
  as well as from CFEngine hard classes and system variables. The workaround is
  to use system tools to obtain the required information and set classes based
  on this.
        * Disk free
        * Memory size
        * Several OS and architecture specific attributes
                * System version
                * System serial number
                * System manufacturer
                * CPU model
                * BIOS version
                * BIOS vendor
* [Process promises][processes] depend on the `ps` native tool, which by
  default truncates lines at 128 columns on HP-UX. It is recommended to edit
  the file `/etc/default/ps` and increase the `DEFAULT_CMD_LINE_WIDTH` setting
  to 1024 to guarantee that process promises will work smoothly on the
  platform.
* Upgrading CFEngine on HP-UX is not supported by the out-of-the-box policy.
  There is a [support article](https://cfengine.zendesk.com/hc/en-us/articles/205454908)
  with a workaround.

### Enterprise emails sent for alert noticies come from 'admin@organization.com'.
There is currently no setting in Mission Portal to configure the sender email
address. This issue is on the [backlog](https://dev.cfengine.com/issues/6726)
and will be addressed in a future release.

To change the setting you must edit the from email address in
`/var/cfengine/httpd/htdocs/application/config/appsettings.php`

```
// Default FROM email address
$config['appemail'] = 'admin@organisation.com';
```

### Enterprise monitoring graphs

Monitoring graphs are disabled by default in CFEngine Enterprise 3.6 and later
versions.  To enable them, change monitoring_include in
masterfiles/controls/VERSION/reports.cf to e.g. ".*".  Note that this has a
significant impact on the resource consumption of your hub.

Monitoring graphs are not supported on all platforms, currently AIX, HP-UX and
Windows do not have this data.

### Enterprise software inventory is not out-of-the-box

Software inventory is not out-of-the-box for reporting from the hub on other
platforms than Debian, Ubuntu and Red Hat/CentOS.

In order to add software inventory for other platforms,
please contact support for a custom policy.

### Enterprise - Unable to edit directory based users with dots in username

Mission Portal does not allow users from a directory to be edited if they have
dots in their username.
