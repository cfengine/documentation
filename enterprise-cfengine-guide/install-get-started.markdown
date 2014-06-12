---
layout: default
title: Install and Get Started
published: true
sorting: 10
---

* [Installation][Install and Get Started#Installation]
* [Post-Install Configuration][Install and Get Started#Post-Install Configuration]
	
## Installation ##

## Post-Install Configuration ##

### Change Email Setup After CFEngine Enterprise Installation ###

For Enterprise 3.6.0 local mail relay is used, and it is assumed the server has a proper mail setup.

The default FROM email for all emails sent from the Mission Portal is ```admin@organization.com```. This can be changed on the CFE Server in ```/var/cfengine/httpd/htdocs/application/config/appsettings.php:$config['appemail']```.