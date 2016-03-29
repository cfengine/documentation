---
layout: default
title: Reporting Architecture
published: true
sorting: 10
tags: [manuals, enterprise, reporting, architecture, cf-hub]
---

The reporting architecture of CFEngine Enterprise uses two software
components from the CFEngine Enterprise hub package.

## cf-hub ##

Like all CFEngine components, `cf-hub` is
located in `/var/cfengine/bin`. It is a daemon process that runs in the
background, and is started by `cf-agent` and from the init scripts.

`cf-hub` wakes up every 5 minutes and connects to the `cf-serverd` of
each host to download new data.


To collect reports from any host manually, run the following:

    $ /var/cfengine/bin/cf-hub -H <host IP>

* Add `-v` to run in verbose mode to diagnose connectivity issues and trace the data collected.

* Delta (differential) reporting, the default mode, collects data that has changed since the
last collection. Rebase (full) reports collect everything. You can choose the full collection by
adding `-q rebase` (for backwards comapatibility, also available as
`-q full`).

## Apache ##

REST over HTTP is provided by the
[Apache http server](http://httpd.apache.org) which also hosts the
Mission Portal. The `httpd` process is started through CFEngine policy
and the init scripts and listens on ports 80 and 443 (HTTP and HTTP/S).

Apache is part of the CFEngine Enterprise installation in
`/var/cfengine/httpd`. A local `cfapache` user is created with
privileges to run `cf-runagent`.
