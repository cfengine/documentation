---
layout: default
title: Troubleshooting
categories: [Manuals, Enterprise Reporting, Troubleshooting]
published: true
sorting: 90
alias: manuals-enterprise-reporting-troubleshooting.html
tags: [manuals, enterprise, reporting, troubleshooting, cf-hub, mongo, apache]
---

If you are experiencing problems with logging into the Mission Portal or don't 
see up-to-date data, check the following points:

* Make sure that the daemon processes are running

`ps -e` should list processes 'cf-hub', 'httpd' and 'mongod'

If that is not the case, run:

    $ rm -f /var/cfengine/state/mongod.lock
    $ /var/cfengine/bin/cf-execd -Ov > cfout.log

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

* Changing PHP settings

For CFEngine Enterprise <= v3.5.2, the default location for `php.ini` is incorrect. To confirm:

		$/var/cfengine/httpd/php/bin/php -i | grep php.ini
		cfengine-enterprise-api: Initialized log-level: debug
		cfengine-enterprise-api: Initialized crypto
		cfengine-enterprise-api: Initialized file cache for queries
		cfengine-enterprise-api: CFEngine Enterprise API module initialized
		*Configuration File (php.ini) Path => /var/cfengine/httpd/php/lib*

As a workaround, please create a symlink to the `php.ini` shipped with the package:

		ln -s /var/cfengine/httpd/php/php.ini /var/cfengine/httpd/php/lib/php.ini
