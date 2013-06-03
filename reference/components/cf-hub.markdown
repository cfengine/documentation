---
layout: default
title: cf-hub
categories: [Reference, Components, cf-hub]
published: true
alias: reference-components-cfhub.html
tags: [reference, components, cf-hub, enterprise]
---

The data aggregator of CFEngine Enterprise. **TODO: more!**

`cf-hub` keeps the promises made in `common`, and is affected by
`common` and `hub` control bodies.

## Command reference

    '--cache'
       (-a) - Rebuild database caches used for efficient query handling (e.g. 
       compliance graphs)
    '--continuous'
       (-c) - Continuous update mode of operation
    '--debug'
       (-d value) - Set debugging level 0,1,2,3
    '--no-fork'
       (-F) - Run as a foreground processes (do not fork)
    '--file'
       (-f value) - Specify an alternative input file than the default
    '--help'
       (-h) - Print the help message
    '--index'
       (-i) - Reindex all collections in the CFEngine report database
    '--no-lock'
       (-K) - Ignore locking constraints during execution 
       (ifelapsed/expireafter) if "too soon" to run
    '--logging'
       (-l) - Enable logging of report collection and maintenance to hub_log 
       in the working directory
    '--maintain'
       (-m) - Start database maintenance process. By default, entries older 
       than 7 days (1 year for longterm reports) are purged.
    '--dry-run'
       (-n) - All talk and no action mode - make no changes, only inform of 
       promises not kept
    '--splay_updates'
       (-s) - Splay/load balance full-updates, overriding bootstrap times, 
       assuming a default 5 minute update schedule.
    '--version'
       (-V) - Output the version of the software
    '--verbose'
       (-v) - Output verbose information about the behaviour of the agent

## Control Promises


```cf3
    body hub control
    {
    export_zenoss => "/var/www/reports/summary.z";
    }
```

### export_zenoss

**Type**: `string`

**Allowed input range**: `.+`

**Description**: Generate report for Zenoss integration

    body hub control
    {
    am_policy_hub::
    
      export_zenoss => "/var/www/reports/summary.z";
    }

**Notes**:

**History**: Was introduced in version 3.1.0b1, Enterprise 2.0.0b1 (2010)

For integration with the Zenoss monitoring software.


### exclude_hosts

**Type**: `slist`

**Allowed input range**: (arbitrary string)

**Description**: A list of IP addresses of hosts to exclude from
report collection

    body hub control
    {
    exclude_hosts => { "192.168.12.21", "10.10", "10.12.*" };
    }

**Notes**:

**History**: Was introduced in 3.3.0, Enterprise 2.1.1 (2011)

In CFEngine Enterprise, this list of IP addresses will not
be queried for reports by `cf-hub`, even though they are in the
last-seen database.

The lists may contain network addresses in CIDR notation or regular
expressions to match the IP address. However, host names are
currently not supported.


### hub_schedule

**Type**: `slist`

**Allowed input range**: (arbitrary string)

**Description**: The class schedule used by cf-hub for report
collation

    body hub control
    {
    hub_schedule => { "Min00", "Min30", "(Evening|Night).Min45_50" };
    }

**Notes**:

**History**: Was introduced in version 3.1.0b1, Enterprise 2.0.0b1 (2010)


### port

**Type**: `int`

**Allowed input range**: `1024,99999`

**Default value:** 5308

**Description**: Default port for contacting hub nodes

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

**Notes**:

The standard or registered port number is tcp/5308. CFEngine does not 
presently use its registered udp port with the same number, but this could 
change in the future.

Changing the standard port number is not recommended practice. You should not 
do it without a good reason.

