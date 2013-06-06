---
layout: default
title: Reporting Architecture
categories: [Manuals, Enterprise Reporting, Architecture]
published: true
alias: manuals-enterprise-reporting-architecture.html
tags: [manuals, enterprise, reporting, architecture, cf-hub]
---

The reporting architecture of CFEngine Enterprise consists of software 
components that are included in the hub-package of the [CFEngine Enterprise 
installation](getting-started-installation.html).

### cf-hub

Like all CFEngine components, [`cf-hub`](reference-components-cfhub.html) is 
located in `/var/cfengine/bin`. It is a daemon process that runs in the 
background, and is started by `cf-agent` through the `failsafe` policy.

Every 5 minutes it wakes up to connect to the `cf-serverd` of each host via 
port 5308, and to download new data (delta report). A download of the complete 
set of data is performed every 6 hours.

In addition, cf-hub runs a maintenance check and database cleanup routine 
every 6 hours, and collects data about its own performance, the status of the 
database and connectivity status for hosts.

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

The [Enterprise API](manuals-enterprise-api.html) implementation connects to 
the database to provide access to the data via SQL queries.

### Apache

REST over HTTP is provided by the [Apache http 
server](http://httpd.apache.org) which also hosts the [Mission 
Portal](**TODO**). The`httpd` process is started through CFEngine policy, and 
listens on port 80.

Apache is part of the CFEngine Enterprise installation in 
`/var/cfengine/httpd`. A user `apache` is created with privileges to run 
`cf-runagent`.

### Troubleshooting of CFEngine Enterprise

If you are experiencing problems with logging into the Mission Portal or don't 
see up-to-date data, check the following points:

* Make sure that the daemon processes are running

`ps -e` should list processes 'cf-hub', 'httpd' and 'mongod'

If that is not the case, run

    /var/cfengine/bin/cf-twin -Kv > cfout.log

* check the CFEngine output

If the processes are still not running after this, check the generated output file for:

    [timestamp] verbose: Comment 'Start CFE httpd process if not exist'

and

    [timestamp] verbose: Comment 'Check for mongod process'

The lines around those comments might give an indication why the respective 
processes failed to start.

* Check apache and mongo logs

If problems remain in spite of running processes, or if the processes 
terminated immediately after a successful start, check the logs in:

    /var/cfengine/httpd/logs/*
    /var/log/mongo.log

These should provide details about why the processes refused to start, shut 
down or continue to deny access.
