---
layout: default
title: Settings
sorting: 10
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
* [Export/Import][Settings#Export/Import]
* [Role based access control][Settings#Role based access control]
* [About CFEngine][Settings#About CFEngine]


## Opening Settings ##

<img src="Settings-1.png" alt="Opening Settings" width="424px">

Settings are accessible from any view of the mission portal, from the
drop down in the top right hand corner.

## Preferences ##

<img src="Settings-2.png" alt="Preferences" width="700px">

User settings and preferences allows the CFEngine Enterprise
administrator to change various options, including:

* Turn on or off RBAC
  * When RBAC is disabled any user can see a host that has reported classes
  * Note, administrative functions like the ability to delete hosts are not
    affected by this setting and hosts that have no reported classes are never
    shown.
* Unreachable host threshold
* Number of samples used to identify a duplicate identity
* Log level
* Customize the user experience with the organization logo

## User Management ##

<img src="Settings-3.png" alt="User Management" width="700px">

User management is for adding or adjusting CFEngine Enterprise UI
users, including their name, role, and password.

## Role Management ##

<img src="Settings-role.png" alt="Role Management" width="430px">

Roles limit access to host data and access to shared assets like saved reports
and dashboards.

Roles limit access to which hosts can be seen based on the classes reported by
the host. For example if you want to limit a users ability to report only on
hosts in the "North American Data Center" you could setup a role that includes
only the `location_nadc` class.

When multiple roles are assigned to a user, the user can access only resources
that match the most restrictive role across all of their roles. For example,
if you have the admin role and a role that matches zero hosts, the user will
not see any hosts in Mission Portal. A shared report will only be accessible
to a user if the user has all roles that the report was restricted to.

In order to access a shared reports or dashboard the use must have all roles
that the report or dashboard was shared with.

In order to see a host, none of the classes reported by the host can match the
class exclusions from any role the user has.

Users without a role will not be able to see any hosts in Mission
Portal.

Role **suse**:
- Class include: `SUSE`
- Class exclude: empty

Role **cfengine_3**:
- Class include: `cfengine_3`
- Class exclude: empty

Role **no_windows**
- Class include: `cfengine_3`
- Class exclude: `windows`

Role **windows_ubuntu**
- Class include: `windows`
- Class include: `ubuntu`
- Class exclude: empty

User one has role `SUSE`.

User two has roles `no_windows` and `cfengine_3`.

User three has roles `windows_ubuntu` and `no_windows`.

A report shared with `SUSE` and `no_windows` will not be seen by any of the
listed users.

A report shared with `no_windows` and `cfengine_3` will only be seen by user
two.

A report shared with `SUSE` will be seen by user one.

User one will only be able to see hosts that report the `SUSE` class.

User two will be able to see all hosts that have **not** reported the `windows`
class.

User three will only be able to see hosts that have reported the `ubuntu` class.

### Predefined Roles

* ```admin``` - The admin role can see everything and do anything.
* ```cf_remoteagent``` - This role allows execution of `cf-runagent`.
  
### Default Role

To set the default role, click Settings -> User management -> Roles. You can then select which role will be the default role for new users.

<img src="roles-list.png" alt="DefaultRoleSelecting" width="700px">

**Behaviour of Default Role:**

Any new users created in Mission Portal's local user database will have this new role assigned.

Users authenticating through LDAP (if you have LDAP configured in Mission Portal) will get this new role applied the first time they log in.

Note that the default role will not have any effect on users that already exist (in Mission Portal's local database) or have already logged in (when using LDAP).

In effect this allows you to set the default permissions for new users (e.g. which hosts a user is allowed to see) by configuring the access for the default role.

<img src="add-new-user.png" alt="AddNewUser" width="430px">

## Manage Apps ##

<img src="Settings-4.png" alt="Manage Apps" width="700px">

Application settings can help adjust some of CFEngine Enterprise UI
app features, including the order in which the apps appear and their
status (on or off).

## Version Control Repository ##

<img src="settings-vcs.png" alt="Version Control Repository" width="700px">

The repository holding the organization's masterfiles can be adjusted
on the Version Control Repository screen.

## Host Identifier ##

<img src="Settings-6.png" alt="Host Identifier" width="700px">

Host identity for the server can be set within settings, and can be
adjusted to refer to the FQDN, IP address, or an unqualified domain
name.

## Mail settings ##

<img src="mail-settings.png" alt="Mail settings" width="700px">

Configure outbound mail settings:

- Default from email : Email address that Mission Portal will use by default
  when sending emails.

- Mail protocol : Use the system mailer (Sendmail) or use an SMTP server.

- Max email attachment size (MB) : mails sent by Mission Portal with attachments
  exceeding this will have the attachment replaced with links to download the
  large files.

## Authentication settings ##

<img src="Authentication-settings.png" alt="Authentication settings" width="700px">

Mission portal can authenticate against an external directory.

**Special Notes:** 

- LDAP API Url refers to the API cfengine uses internally for authentication.
  Most likely you will not alter the default value.

- LDAP filter must be supplied.

- LDAP Host refers is the IP or Hostname of your LDAP server.

- LDAP bind username should be the username used to bind and search the LDAP
  directory. It must be provided in distinguished name format.

- Default roles for users is configured under [Role Management][Settings#Role Management].

### LDAP groups syncing ###

- Ldap group syncing can be turned on by clicking the corresponding checkbox
    
    - User group attribute must be provided to obtain groups from an LDAP user entity. 
    The default value for Active Directory is `memberOf`. 
    The group name will be taken from `cn` attribute
    - List of groups to sync, names must match in LDAP/MP. Each role should be added on a new line.
    - Click `Perform sync on every login` checkbox to synchronize user roles on every login, otherwise
    roles will be assigned to a user only on sign-up (first login).
    

**See also:** [LDAP authentication REST API][LDAP authentication API]


## Export/Import ##

Mission Portal's configuration can be exported and imported.

<img src="settings-export-import-3.18.0.png" alt="Export/Import" width="590px">

**See also:** [Export/Import API][Import & Export API]

## Role based access control ##

<img src="role_based_access_control_settings.png" alt="Role based access control" width="590px">

Roles in Mission portal can be restricted to perform only configured actions. 
Configure role-based access controls from settings.

**Special Notes:** 

- Admin role has all permissions by default.

- Cf_remoteagent role has all permissions related to API by default.

- Permissions granted by roles are additive, users with multiple roles are permitted to perform actions granted by each role.

**Restore admin role permissions:** 

To restore the CFEngine admin role permissions run the following sql as root on your hub

```console
root@hub:~# /var/cfengine/bin/psql cfsettings -c "INSERT INTO rbac_role_permission (role_id, permission_alias) (SELECT 'admin'::text as role_id, alias as permission_alias FROM rbac_permissions) ON CONFLICT (role_id, permission_alias)  DO NOTHING;"
```

**See also:** [Web RBAC API][Web RBAC API]


## About CFEngine ##

<img src="Settings-7.png" alt="About CFEngine" width="700px">

The About CFEngine screen contains important information about the
specific version of CFEngine being used, license information, and
more.
