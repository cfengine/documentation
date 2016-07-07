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

### Enterprise Hub - Mission Portal database not properly preserved

When upgrading from earlier versions, the Mission Portal database may not be preserved, resulting
in Mission Portal to appear as a fresh installation.

### Incompatible Apache config during upgrade

Mis-spellings in the `3.9.0` release of the MPF when run on a hub with `3.6.x`
binaries results in Apache getting an incompatible configuration.

Fixed in `3.9.1` with [this change](https://github.com/cfengine/masterfiles/pull/740/files).

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

* Add an empty =cf_null= bundle

```cf3
bundle common cf_null
{
  reports:
    !any::
      "This works around an issue iterating over an list of bundles.";
}
```
