---
layout: default
title: Known Issues
sorting: 50
published: true
tags: [overviews, releases, latest release, platforms, versions, known issues]
---

CFEngine defects are managed in our [bug tracker][bug tracker]. Please report
bugs or unexpected behavior there, following the documented guideline for new
bug reports.

* Core Issues affecting [{{site.cfengine.branch}}](https://tracker.mender.io/secure/QuickSearch.jspa?searchString=v:{{site.cfengine.branch}}*)

The items below highlight issues that require additional awareness when starting
with CFEngine or when upgrading from a previous version.

### `cf-agent -N` or `cf-agent --negate` is not working

As reported in [CFE-1589](https://tracker.mender.io/browse/CFE-1589) the
functionality of negating persistent classes on the command line, was
removed sometime before 3.5, commit
cf63db27945f0628caa5bf45338f7709d5d12b21. The ticket is open until the
functionality is reinstated.

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

### Enterprise monitoring graphs

Monitoring graphs are disabled by default in CFEngine Enterprise 3.6 and later
versions. To enable them, change monitoring_include in
```masterfiles/controls/reports.cf``` to e.g. ".*". Note that this can have
significant impact on the resource consumption of your hub.

Monitoring graphs are not supported on all platforms, currently AIX, HP-UX and
Windows do not have this data.

### Enterprise inventory CSV report is empty (0 bytes)

Exporting a CSV-based inventory report can result in a 0-byte length file
if the CFEngine Server is accessed over https and the certificate's CN
mismatches with the URL you use to export the report. To verify this is the
problem, check the Mission Portal application logs (currently at
/var/cfengine/httpd/htdocs/application/logs) on the CFEngine Server. If you
see lines like the following you affected by this issue.

```
ERROR - 2016-06-15 07:24:15 --> Severity: Warning --> readfile(): Peer certificate CN=`myhostname.example.com' did not match expected CN=`myhostname' /var/cfengine/httpd/htdocs/application/helpers/cf_util_helper.php 612
ERROR - 2016-06-15 07:24:15 --> Severity: Warning --> readfile(): Failed to enable crypto /var/cfengine/httpd/htdocs/application/helpers/cf_util_helper.php 612
ERROR - 2016-06-15 07:24:15 --> Severity: Warning --> readfile(https://myhostname/api/static/e39cfd50f95a853fb103a89477b46eb8.csv): failed to open stream: operation failed /var/cfengine/httpd/htdocs/application/helpers/cf_util_helper.php 612
```

The solution is to generate a new certificate with the correct CN,
i.e. the one you use to access the CFEngine Server. To see how to do
this, look at the documentation for using a [Custom SSL certificate][Custom SSL Certificate].

### Enterprise software inventory is not out-of-the-box

Software inventory is not out-of-the-box for reporting from the hub on other
platforms than Debian, Ubuntu and Red Hat/CentOS.

In order to add software inventory for other platforms,
please contact support for a custom policy.

