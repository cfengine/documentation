---
layout: default
title: hub control promises
categories: [Reference, Components, cf-hub, hub control promises]
published: true
alias: reference-components-cfhub-control-promises.html
tags: [Components, cf-hub, control promises]
---

**TODO:overview**

```cf3
    body hub control
    {
    export_zenoss => "/var/www/reports/summary.z";
    }
```

## `export_zenoss`

**Type**: string

**Allowed input range**: `.+`

**Synopsis**: Generate report for Zenoss integration

    body hub control
    {
    am_policy_hub::
    
      export_zenoss => "/var/www/reports/summary.z";
    }

**Notes**:

*History*: Was introduced in version 3.1.0b1, Enterprise 2.0.0b1 (2010)

For integration with the Zenoss monitoring software.


## `exclude_hosts`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: A list of IP addresses of hosts to exclude from
report collection

    body hub control
    {
    exclude_hosts => { "192.168.12.21", "10.10", "10.12.*" };
    }

**Notes**:

*History*: Was introduced in 3.3.0, Enterprise 2.1.1 (2011)

In commercial CFEngine editions, this list of IP addresses will not
be queried for reports by `cf-hub`, even though they are in the
last-seen database.

The lists may contain network addresses in CIDR notation or regular
expressions to match the IP address. However, host names are
currently not supported.


## `hub_schedule`

**Type**: slist

**Allowed input range**: (arbitrary string)

**Synopsis**: The class schedule used by cf-hub for report
collation

    body hub control
    {
    hub_schedule => { "Min00", "Min30", "(Evening|Night).Min45_50" };
    }

**Notes**:

*History*: Was introduced in version 3.1.0b1, Enterprise 2.0.0b1 (2010)


## `port`

**Type**: int

**Allowed input range**: `1024,99999`

**Default value:** 5308

**Synopsis**: Default port for contacting hub nodes

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

