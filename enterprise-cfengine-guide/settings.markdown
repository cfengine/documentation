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
* [Mail Settings][Settings#Mail settings]
* [Authentication settings][Settings#Authentication settings]
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

Roles are used to limit access. Roles can limit access for reporting on
hosts that have or do not have specific classes.

For example if you want to limit a users ability to report only on
hosts in the "North American Data Center" you could setup a role that
includes only the `location_nadc` class.

If you have multiple roles assigned to a user, the user can access
only hosts that match all of their role restrictions. For example, if
you have the admin role and a role that matches zero hosts, the user
will not see any hosts in Mission Portal.

Users without a role will not be able to see any hosts in Mission
Portal.

**Predefined Roles:**

* ```admin``` - The admin role can see everything and do anything.
* ```cf_remoteagent``` - This role allows execution of `cf-runagent`.
  
**Default Role:**

To set the default role, click Settings -> User management -> Roles. You can then select which role will be the default role for new users.

![DefaultRoleSelecting](roles-list.png)

**Behaviour of Default Role:**

Any new users created in Mission Portal's local user database will have this new role assigned.

Users authenticating through LDAP (if you have LDAP configured in Mission Portal) will get this new role applied the first time they log in.

Note that the default role will not have any effect on users that already exist (in Mission Portal's local database) or have already logged in (when using LDAP).

In effect this allows you to set the default permissions for new users (e.g. which hosts a user is allowed to see) by configuring the access for the default role.

![AddNewUser](add-new-user.png)

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

## Mail settings ##

![Mail settings](mail-settings.png)

Configure outbound mail settings:

- Default from email : Email address that Mission Portal will use by default
  when sending emails.

- Mail protocol : Use the system mailer (Sendmail) or use an SMTP server.

- Max email attachment size (MB) : mails sent by Mission Portal with attachments
  exceeding this will have the attachment replaced with links to download the
  large files.

## Authentication settings ##

![Authentication settings](Authentication-settings.png)

Mission portal can authenticate against an external directory.

**Special Notes:** 

- LDAP API Url refers to the API cfengine uses internally for authentication.
  Most likely you will not alter the default value.

- LDAP filter must be supplied.

- LDAP Host refers is the IP or Hostname of your LDAP server.

- LDAP bind username should be the username used to bind and search the LDAP
  directory. It must be provided in distinguished name format.

- Default roles for users is configured under [Role Management][Settings#Role Management].

**See Also:** [LDAP authentication REST API][LDAP authentication API]

## About CFEngine ##

![About CFEngine](Settings-7.png)

The About CFEngine screen contains important information about the
specific version of CFEngine being used, license information, and
more.
