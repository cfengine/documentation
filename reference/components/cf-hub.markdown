---
layout: default
title: cf-hub
categories: [Reference, Components, cf-hub]
published: true
alias: reference-components-cfhub.html
tags: [reference, components, cf-hub, enterprise]
keywords: [hub]
---

`cf-hub` connects to [`cf-serverd`][cf-serverd] instances to collect data 
about a host managed by CFEngine. `cf-agent` and [`cf-monitord`][cf-monitord] 
both store data at host in local databases. `cf-hub` connects to a 
`cf-serverd` instance running at a host and collect the data into its own 
central database. `cf-hub` automatically schedules data collection from hosts 
that have registered a connection with a collocated `cf-serverd`

`cf-hub` keeps the promises made in `common`, and is affected by
`common` and `hub` control bodies.

## Command reference

    --cache, -a
        Rebuild database caches used for efficient query handling (e.g. compliance graphs)

    --continuous, -c
        Continuous update mode of operation

    --debug, -d
        Set debugging level 0,1,2,3.

    --no-fork, -F
        Run as a foreground processes (do not fork)

    --file, -f
        Specify an alternative input file than the default

    --help, -h
        Print the help message

    --index, -i
        Reindex all collections in the CFEngine report database

    --no-lock, -K
        Ignore locking constraints during execution (ifelapsed/expireafter) if "too soon" to run

    --logging, -l
        Enable logging of report collection and maintenance to hub_log in the working directory

    --maintain, -m
        Start database maintenance process. By default, entries older than 7 days (1 year for longterm reports) are purged.

    --dry-run, -n
        All talk and no action mode - make no changes, only inform of promises not kept

    --splay_updates, -s
        Splay/load balance full-updates, overriding bootstrap times, assuming a default 5 minute update schedule.

    --query, -q
        Collect reports from remote host. Value is 'full' or 'delta'. -H option is required.

    --query-host, -H
        Remote hosts to gather reports from (for -q)

    --version, -V
        Output the version of the software

    --verbose, -v
        Output verbose information about the behaviour of the agent

    --color, -C
        Enable colorized output. Possible values: 'always', 'auto', 'never'. Default is 'never'


## Control Promises

```cf3
    body hub control
    {
    export_zenoss => "/var/www/reports/summary.z";
    }
```

### export_zenoss

**Description:** Generate report for Zenoss integration

**Type:** `string`

**Allowed input range:** `.+`

**Example:**

    body hub control
    {
    am_policy_hub::

      export_zenoss => "/var/www/reports/summary.z";
    }

**Notes:**

For integration with the Zenoss monitoring software.

**History:** Was introduced in version 3.1.0b1, Enterprise 2.0.0b1 (2010)

### exclude_hosts

**Description:** A list of IP addresses of hosts to exclude from
report collection

This list of IP addresses will not be queried for reports by `cf-hub`, even
though they are in the last-seen database.

The lists may contain network addresses in CIDR notation or regular
expressions to match the IP address. However, host names are
currently not supported.

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

    body hub control
    {
    exclude_hosts => { "192.168.12.21", "10.10", "10.12.*" };
    }

**Notes:**

**History:** Was introduced in 3.3.0, Enterprise 2.1.1 (2011)

### hub_schedule

**Description:** The class schedule used by cf-hub for report
collation

**Type:** `slist`

**Allowed input range:** (arbitrary string)

**Example:**

    body hub control
    {
    hub_schedule => { "Min00", "Min30", "(Evening|Night).Min45_50" };
    }

**History:** Was introduced in version 3.1.0b1, Enterprise 2.0.0b1 (2010)


### port

**Description:** Default port for contacting hosts

**Type:** `int`

**Allowed input range:** `1024,99999`

**Default value:** 5308

**Examples**:

```cf3
    body hub control
    {
    port => "5308";
    }

    body server control
    {
    specialhost::
     port => "5308";

    !specialhost::
     port => "5308";
    }
```

**Notes:**

The standard or registered port number is tcp/5308. CFEngine does not
presently use its registered udp port with the same number, but this could
change in the future.

Changing the standard port number is not recommended practice. You should not
do it without a good reason.
