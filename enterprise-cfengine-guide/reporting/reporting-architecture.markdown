---
layout: default
title: Reporting Architecture
published: true
sorting: 10
tags: [manuals, enterprise, reporting, architecture, cf-hub]
---

The reporting architecture of CFEngine Enterprise consists of software 
components that are included in the hub-package of the CFEngine Enterprise 
installation.

## cf-hub ##

Like all CFEngine components, [`cf-hub`][cf-hub] is 
located in `/var/cfengine/bin`. It is a daemon process that runs in the 
background, and is started by `cf-agent` through the `failsafe` policy.

`cf-hub` wakes up every 5 minutes and connects to the `cf-serverd` of each 
host to download new data. Delta reports include new data in the last interval and a 
subset of variable information. 

Report collection from any host can be triggered manually by running the following:

    $ /var/cfengine/bin/cf-hub -q full -H <host IP>

Run in verbose mode (-v) to diagnose connectivity issues and trace the data 
collected.

## Apache ##

REST over HTTP is provided by the
[Apache http server](http://httpd.apache.org) which also hosts the Mission Portal. 
The `httpd` process is started through CFEngine policy and listens on port 80.

Apache is part of the CFEngine Enterprise installation in 
`/var/cfengine/httpd`. An `apache` user is created with privileges to run 
`cf-runagent`.
