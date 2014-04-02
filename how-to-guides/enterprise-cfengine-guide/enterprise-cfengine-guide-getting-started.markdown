---
layout: default
title: Getting Started With CFEngine Enterprise
categories: [How to Guides,CFEngine Enterprise Guide, Getting Started]
published: true
sorting: 10
alias: how-to-guides-cfengine-enterprise-getting-started.html
---

* [Installation](#installation)
* [Post-Install Configuration](#post-install-configuration)
	* [Change Email Setup After CFEngine Enterprise Installation](#change-email-setup-after-cfengine-enterprise-installation)

## Installation ##

## Post-Install Configuration ##

### Change Email Setup After CFEngine Enterprise Installation ###

For Enterprise 3.6.0 local mail relay is used, and it is assumed the server has a proper mail setup.

The default FROM email for all emails sent from the Mission Portal is ```admin@organization.com```. This can be changed on the CFE Server in ```/var/cfengine/httpd/htdocs/application/config/appsettings.php:$config['appemail']```.