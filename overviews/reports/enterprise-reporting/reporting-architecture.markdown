---
layout: default
title: Reporting Architecture
published: true
sorting: 10
tags: [manuals, enterprise, reporting, architecture, cf-hub]
---

The reporting architecture of CFEngine Enterprise consists of software 
components that are included in the hub-package of the [CFEngine Enterprise 
installation][Installing CFEngine].

### cf-hub

Like all CFEngine components, [`cf-hub`][cf-hub] is 
located in `/var/cfengine/bin`. It is a daemon process that runs in the 
background, and is started by `cf-agent` through the `failsafe` policy.

`cf-hub` wakes up every 5 minutes and connects to the `cf-serverd` of each 
host to download new data. Delta reports include new data in the last interval and a 
subset of variable information. A download of the complete set of data is performed every 6 hours.

Report collection from any host can be triggered manually by running the following:

    $ /var/cfengine/bin/cf-hub -q full -H <host IP>

Run in verbose mode (-v) to diagnose connectivity issues and trace the data 
collected.

In addition, `cf-hub` runs a maintenance check and database cleanup routine 
every 6 hours and collects data about its own performance, the status of the 
database, and connectivity status for hosts.

All data is then stored in a NoSQL MongoDB database.

### mongodb

[MongoDB](http://www.mongodb.org) (from hu**mongo**ous) is an Open Source 
document database. The `mongod` daemon process is started through CFEngine 
policy. The daemon as well as the command line interface program `mongo` are 
included in the CFEngine Enterprise installation in `/var/cfengine/bin`.

`cf-hub` stores collected data in MongoDB. The majority of data is stored for 
a week. Oldest data is continuously purged by the `cf-hub` maintenance 
process, and replaced by new incoming data. An exception is data about file 
changes, which is stored for up to one year.

The Enterprise API implementation connects to 
the database to provide access to the data via [SQL queries][SQL Queries].

### Apache

REST over HTTP is provided by the
[Apache http server](http://httpd.apache.org) which also hosts the Mission Portal. 
The `httpd` process is started through CFEngine policy and listens on port 80.

Apache is part of the CFEngine Enterprise installation in 
`/var/cfengine/httpd`. An `apache` user is created with privileges to run 
`cf-runagent`.
