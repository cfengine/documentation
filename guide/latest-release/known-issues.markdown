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

### Windows agents are unable to use the shortcut feature

Windows agents are unable to use the shortcut feature in access type promises.
This is resolved in 3.7.x and will not be backported to 3.6.x.

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
* Upgrading CFEngine on HP-UX is not supported by the out-of-the-box policy.
  There is a [support article](https://cfengine.zendesk.com/hc/en-us/articles/205454908)
  with a workaround.


### Enterprise Mission Portal is slow and/or /var/cfengine/state/pg consumes a lot of space/iops or CPU utilization is high ###

With ceratin policies, the BenchmarksLog table in the PostgreSQL database is known to grow large with CFEngine versions from 3.6.0 to and including 3.6.5. This issue is resolved in CFEngine 3.6.6 and later versions.
To test for the problem, run the following commands on the hub:

```console
# /var/cfengine/bin/psql cfdb
SELECT nspname || '.' || relname AS "relation", pg_size_pretty(pg_total_relation_size(C.oid)) AS "total_size" FROM pg_class C LEFT JOIN pg_namespace N ON (N.oid = C.relnamespace) WHERE nspname NOT IN ('pg_catalog', 'information_schema') AND C.relkind <> 'i' ORDER BY pg_total_relation_size(C.oid) DESC LIMIT 20;
```

If the table public.__benchmarkslog is larger than 2-3 GB, you are likely affected by this isse. The table is not used unless you have created custom queries against it yourself. To resolve the issue, please run these commands after a fresh install of any hub prior to version 3.6.6:

```console
# /var/cfengine/bin/psql cfdb
cfdb=# truncate table __benchmarkslog;
cfdb=# create index benchmarks_subselect ON __benchmarkslog (hostkey, eventname, checktimestamp) WITH (FILLFACTOR = 70);
```

If your hub is still slow or BenchmarksLog was not the problem, please contact support.


### Unsupported direct upgrade from CFEngine Enterprise 3.6.0 / 3.6.1 to 3.6.5 ###
Due to an issue in Enterprise 3.6.5 direct upgrade from 3.6.0 and 3.6.1 may resolve with database schema curruption.
Upgrade from 3.6.0 / 3.6.1 to 3.6.5 can be done by upgrading first to 3.6.2 / 3.6.3 / 3.6.4 and then to 3.6.5.


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

### Enterprise monitoring graphs ###

Monitoring graphs are disabled by default in CFEngine Enterprise 3.6 and later versions.
To enable them, change monitoring_include in masterfiles/lib/VERSION/reports.cf to e.g. ".*".
Note that this has a significant impact on the resource consumption of your hub.

Monitoring graphs are not supported on all platforms, currently Aix and Windows do not have this data.


### Scheduled reports not written to expected location

There is a known issue when generating scheduled reports for ONLY CSVs. The
report gets written to `/var/cfengine/reports` instead of
`/var/cfengine/httpd/htdocs/tmp` and it is **NOT** named for the report title,
but
instead named by internal identifiers (like
admin-17_admin_1440692523-1441038374.csv).

The workaround is to schedule BOTH CSV and PDF reports. When both CSV and PDF
reports are scheduled the CSV report will be written to
`/var/cfengine/httpd/htdocs/tmp` and named for the report title as expected.

### Enterprise reports not collected from 3.5
CFEngine Enterprise 3.6 has a new diff-based report collection mechanism,
and so a 3.6 hub cannot collect reports from 3.5 or earlier agents.

Currently the 3.5 agents will not show in Mission Portal at all, but
you will see them by running `cf-key -s` on the hub.


### Enterprise software inventory is not out-of-the-box ###

Software inventory is not out-of-the-box for reporing from the hub on Windows platforms.
In order to add it, please contact support for a custom policy.
