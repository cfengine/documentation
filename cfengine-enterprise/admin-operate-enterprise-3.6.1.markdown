---
layout: default
title: Operation of CFEngine
sorting: 30
published: false
tags: [cfengine enterprise]
---

<!--
Operation and Administration of CFEngine

Note: Assumption for this section is that it contains topics that are key to setup, admin and operation of CFEngine itself, rather than delving too much into using CFEngine to administer the systems under its control

Based in part on rough summary of real world SOW

Summary Topics (some new, some old)
	Post-install configuration (CFEngine specific)
	Mission Portal
	VCS setup
	Groups and users
	RBAC and Mission Portal
	Setting up reports 
	(something about support for reports rather than running reports?)
	E-mail (setup)
	Best Practices
	Scalability
	Regular maintenance of CFEngine(?)
	What ongoing maintenance of CFEngine needs to be considered?
-->

* [Troubleshooting][#Troubleshooting]

## Troubleshooting ##

### There is no OOTB reports/alerts right after install ###

Check the CFEngineHub-Install.log (inside /var/log) for lines which contain ootb_import.sql

if nothing found, or there are some errors right after that line you must run the import again
as root:
```console
/var/cfengine/bin/psql cfmp -f /var/cfengine/httpd/htdocs/phpcfenginenova/ootb_import.sql
```
Be careful, because this will remove everything you created in reports/alerts.



### There are no events in events log, but at least one of the alerts is failing ###

Make sure that user CFE_ROBOT is created.

Check CFEngineHub-Install.log (inside /var/log) for the strings like:

```
 CFE_ROBOT_PWD= ...
+ /var/cfengine/httpd/php/bin/php /var/cfengine/httpd/htdocs/index.php cli_tasks create_cfe_robot_user MFjglG7mdEzIKEYtvwBuZQtLNzGjkl9F
cfengine-enterprise-api: Initialized log-level: debug
cfengine-enterprise-api: Initialized crypto
cfengine-enterprise-api: CFEngine Enterprise API module initialized

 Config file created
```

and make sure that there is a cf_robot.php file in /var/cfengine/httpd/htdocs/application/config with lines:

```php
$config['CFE_ROBOT_PASSWORD'] = "<something here>";
```

if file is not created please run:

```console
/var/cfengine/httpd/php/bin/php /var/cfengine/httpd/htdocs/index.php cli_tasks create_cfe_robot_user <new passwordhere>
```

and check that file with the password you specified was created.

Note: You must have a sucessfull connection to cfengine-enterprise-api

