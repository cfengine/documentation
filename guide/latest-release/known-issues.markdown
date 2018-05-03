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

### Protocol incompatibility (3.5 or earlier)

The CFEngine protocol versions 1 and 2 are incompatible (the latter is based
on TLS). CFEngine 3.6 supports both protocol versions, but earlier versions
only support protocol version 1. Protocol version 2 the default in
3.7. This can be configured with the allowlegacyconnects and protocol_version
attributes.

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

### Enterprise emails sent for alert noticies come from 'admin@organization.com'.
There is currently no setting in Mission Portal to configure the sender email
address. This issue is tracked in [ENT-695](https://tracker.mender.io/browse/ENT-695)
and will be addressed in a future release.

To change the setting you must edit the from email address in
`/var/cfengine/share/GUI/application/config/appsettings.php`. Policy in the
Masterfiles Policy Framework will take care of updating the running config
during the next policy run.
 
```
// Default FROM email address
$config['appemail'] = 'admin@organisation.com';
```

### Enterprise monitoring graphs

Monitoring graphs are disabled by default in CFEngine Enterprise 3.6 and later
versions.  To enable them, change monitoring_include in
masterfiles/controls/VERSION/reports.cf to e.g. ".*".  Note that this has a
significant impact on the resource consumption of your hub.

Monitoring graphs are not supported on all platforms, currently Aix and Windows
do not have this data.

### Enterprise reports not collected from 3.5
CFEngine Enterprise 3.6 has a new diff-based report collection mechanism,
and so a 3.7 hub cannot collect reports from 3.5 or earlier agents.

Currently the 3.5 agents will not show in Mission Portal at all, but
you will see them by running `cf-key -s` on the hub.

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

### Enterprise Hub - PHP warnings after upgrading from `3.6.x`

After upgrading from `3.6.x` PHP warns it is unable to
initialize the apc module.

```
  notice: Q: "...hp/bin/php /var": PHP Warning:  PHP Startup: apc: Unable to initialize module
Q: "...hp/bin/php /var": Module compiled with module API=20100525
Q: "...hp/bin/php /var": PHP    compiled with module API=20131226
Q: "...hp/bin/php /var": These options need to match
Q: "...hp/bin/php /var":  in Unknown on line 0
```

This warning can be resolved by removing
`/var/cfengine/httpd/php/lib/apc.ini` and
`/var/cfengine/httpd/php/lib/php/extensions/no-debug-non-zts-20131226/apc.so`

### Dynamic bundle actuation results in error about `cf_null`

[Jira #CFE-2426](https://tracker.mender.io/browse/CFE-2426)
```
   error: A method attempted to use a bundle 'cf_null' that was apparently not defined
```

This is a benign error. `cf_null` is an internal implementation detail that is
used to handle empty lists.

**Workarounds:**

* Explicitly guard against iterating methods on an empty list.

This snippet shows one way to define a class if a list is **not** empty.

```cf3
  classes:
    "have_some_zero_dynamic_role_bundles"
      expression => some( ".*", "roles_dynamic.bundles" );
```

* Ignore missing bundles in body common control

```cf3
body common control
{
#...

  ignore_missing_bundles => "true";

#...
}
```

* Add an empty `cf_null` bundle

```cf3
bundle common cf_null
{
  reports:
    !any::
      "This works around an issue iterating over an list of bundles.";
}
```
