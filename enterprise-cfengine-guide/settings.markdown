---
layout: default
title: Settings
sorting: 25
published: true
tags: [cfengine enterprise, user interface, mission portal]
---

A variety of CFEngine and system properties can be changed in the
Settings view.

* [Opening Settings][Settings#Opening Settings]
* [Preferences][Settings#Preferences]
* [User Management][Settings#User Management]
* [Role Management][Settings#Role Management]
* [Manage Apps][Settings#Manage Apps]
* [Version Control Repository][Settings#Version Control Repository]
* [Host Identifier][Settings#Host Identifier]
* [About CFEngine][Settings#About CFEngine]


## Opening Settings ##

![Opening Settings](Settings-1.png)

Settings are accessible from any view of the mission portal, from the
drop down in the top right hand corner.

## Preferences ##

![Preferences](Settings-2.png)

User settings and preferences allows the CFEngine Enterprise
administrator to change various options, including:

* User authentication
* Turn on or off RBAC
* Log level
* Customize the user experience with the organization logo

## User Management ##

![User Management](Settings-3.png)

User management is for adding or adjusting CFEngine Enterprise UI
users, including their name, role, and password.

## Role Management ##

![Role Management](Settings-role.png)

Roles are used to lmit access. Roles can limit access for reporting on
hosts that have or do not have spcecific classes, and they can be used
to limit which sketches from Design Center a user is authorized to
use.

For example if you want to limit a users ability to report only on
hosts in the "North American Data Center" you could setup a role that
includes only the `location_nadc` class.

If you have multiple roles assigned to a user, the user can access
only hosts that match all of their role restrictions. For example, if
you have the admin role and a role that matches zero hosts, the user
will not see any hosts in Mission Portal.

Users without a role will not be able to see any hosts in Mission
Portal.

**Default Roles:**
* admin - The admin role can see everything and do anything.
* cf_remoteagent - This role allows execution of cf-runagent. It can
  be used from within Design Center to troubleshoot hosts that have
  failed sketch activations.

## Manage Apps ##

![Manage Apps](Settings-4.png)

Application settings can help adjust some of CFEngine Enterprise UI
app features, including the order in which the apps appear and their
status (on or off).

## Version Control Repository ##

![Version Control Repository](Settings-5.png)

The repository holding the organization's masterfiles can be adjusted
on the Version Control Repository screen.

## Host Identifier ##

![Host Identifier](Settings-6.png)

Host identity for the server can be set within settings, and can be
adjusted to refer to the FQDN, IP address, or an unqualified domain
name.

## About CFEngine ##

![About CFEngine](Settings-7.png)

The About CFEngine screen contains important information about the
specific version of CFEngine being used, license information, and
more.
