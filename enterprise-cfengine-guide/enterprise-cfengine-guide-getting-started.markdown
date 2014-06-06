---
layout: default
title: Getting Started With CFEngine Enterprise
published: true
sorting: 1
---

* [CFEngine Enterprise Features][Getting Started With CFEngine Enterprise#CFEngine Enterprise Features]
* [Installation][Getting Started With CFEngine Enterprise#Installation]
* [Post-Install Configuration][Getting Started With CFEngine Enterprise#Post-Install Configuration]
	
## CFEngine Enterprise Features ##

### Scalability ###

CFEngine Enterprise can manage 1,000's of hosts from a single Policy Server, and parallel processing of policy requests by the Policy Server multiplies the scalability further. 
	  	
### Configurable Data Feeds ###

The CFEngine Enterprise `Mission Portal` provides System Administrators with detailed information about the actual state of the IT infrastructure and how that compares with the desired state. 

### Federation and SQL Reporting ###

CFEngine Enterprise has the ability to create federated structures, in which parts of organizations can have their own configuration policies, while at the same time the central IT organization may impose some policies that are more global in nature. 

### Monitoring and reporting ###

The CFEngine Enterprise Mission Portal contains continual reporting that details compliance with policies, repairs and any failures of hosts to match their desired state.

## Installation ##

## Post-Install Configuration ##

### Change Email Setup After CFEngine Enterprise Installation ###

For Enterprise 3.6.0 local mail relay is used, and it is assumed the server has a proper mail setup.

The default FROM email for all emails sent from the Mission Portal is ```admin@organization.com```. This can be changed on the CFE Server in ```/var/cfengine/httpd/htdocs/application/config/appsettings.php:$config['appemail']```.