---
layout: default
title: cfsettings
---

Settings used by Mission Portal APIs, no reported data.

## Table: audit_logs

Stores system logs about actions performed by users.

**Columns:**

- **id** _(bigint)_
  The unique identifier of audit log event, generated from a sequence.
- **time** _(timestamp without a time zone)_
  Time when an event happened.
- **action** _(text)_
  What was done (e.g., updated, created, deleted, deployed).
- **object_type** _(text)_
  Type of affected object (e.g., user, role, build project).
- **object_id** _(text)_
  Identifier of an affected object (e.g. user, role id, build project id), if applicable.
- **details** _(json)_
  More details in the free-json format.
- **ip_address** _(boolean)_
  IP address of the user who performed the action.

## Table: build_modules

Information about build modules available from the index (build.cfengine.com).

**Columns:**

- **name** _(text)_
  The name of the build module.
- **readme** _(text)_
  The readme file content of the build module in HTML.
- **description** _(text)_
  The description of the build module.
- **version** _(text)_
  The version of the build module.
- **author** _(jsonb)_
  The author information of the build module as a JSON object with keys such as url, name, image.
- **updated** _(timestamp with time zone)_
  The last updated time of the build module.
- **downloads** _(integer)_
  The number of downloads of the build module.
- **repo** _(text)_
  The repository URL of the build module.
- **documentation** _(text)_
  The documentation URL of the build module.
- **website** _(text)_
  The website URL of the build module.
- **subdirectory** _(text)_
  The subdirectory of the build module in the repository.
- **commit** _(text)_
  The commit hash of the build module.
- **dependencies** _(jsonb)_
  The dependencies of the build module as a JSON object.
- **tags** _(jsonb)_
  The tags of the build module as a JSON object.
- **versions** _(jsonb)_
  The available versions of the build module as a JSON object.
- **latest** _(boolean)_
  A flag indicating whether the build module is the latest version.
- **ts_vector** \*(tsvector)\*\*
  Generated ts_vector column based on id and description.

## Table: build_projects

Build application projects.

**Columns:**

- **id** _(bigint)_
  The unique identifier of the build project, generated from a sequence.
- **repository_url** _(text)_
  The URL of the git repository that contains the build project.
- **branch** _(text)_
  The branch of the git repository that the build project uses.
- **name** _(text)_
  The name of the build project, derived from the repository URL and branch.
- **authentication_type** _(authentication_types)_
  The type of authentication that the build project uses to access the git repository. Must match authentication_types such as password or private_key.
- **username** _(text)_
  The username that the build project uses to access the git repository, if applicable.
- **password** _(text)_
  The password that the build project uses to access the git repository, if applicable.
- **ssh_private_key** _(text)_
  This field is not used. Ref ENT-11330.
- **ssh_key_id** _(integer)_
  The foreign key that references the ssh_keys table, if applicable.
- **created_at** _(timestamp with time zone)_
  The timestamp of when the build project was created.
- **pushed_at** _(timestamp with time zone)_
  The timestamp of when the build project was last pushed to the git repository.
- **is_local** _(boolean)_
  The flag that indicates whether the build project is local or remote.
- **is_deployed_locally** _(boolean)_
  The flag that indicates whether the build project is deployed locally or not.
- **action** _(text)_
  The action that the build project performs, such as push, pushAndDeploy, localDeploy.

## Table: cfbs_requests

cfbs requests and responses handled by cf-reactor.

**Columns:**

- **id** _(bigint)_
  The unique identifier of the cfbs request, generated from a sequence.
- **request_name** _(text)_
  The name of the cfbs request, such as init_project, local_deploy, etc.
- **arguments** _(jsonb)_
  The JSONB object that stores the arguments of the cfbs request, such as git, project_id, etc.
- **created_at** _(timestamp with time zone)_
  The timestamp of when the cfbs request was created.
- **finished_at** _(timestamp with time zone)_
  The timestamp of when the cfbs request was finished, may be null if the request is still in progress.
- **response** _(jsonb)_
  The JSONB object that stores the response of the cfbs request, such as status, details, etc.

## Table: external_roles_map

Map of external directory group to Mission Portal RBAC role for automatic association of directory users to Mission Portal roles.

**Columns:**

- **external_role** _(text)_
  The name of the external directory (LDAP/Active Directory) group.
- **internal_role** _(text)_
  The name of the internal Mission Portal role, such as admin, auditor, or guest.
- **changetimestamp** _(timestamp with time zone)_
  The timestamp of when the mapping was last changed.

## Table: federated_reporting_settings

Federated reporting settings when enabled.

**Columns:**

- **key** _(character varying)_
  The name of the federated reporting setting, such as enable_as, enable_request_sent, or target_state.
- **value** _(text)_
  The value of the federated reporting setting, such as superhub, 1, or on.

## Table: inventory_aliases

Inventory attributes aliases.

**Columns:**

- **inventory_attribute** _(text)_
  The name of the inventory attribute, such as Kernel, Kernel Release, etc.
- **alias** _(text)_
  The alias of the inventory attribute, such as os type, os kernel, etc.

## Table: keyspendingfordeletion

Keys of deleted hosts yet to be deleted.

**Columns:**

- **hostkey** _(text)_
  The key of the host that was deleted from the database but not yet from the ppkeys directory.

## Table: licenseinfo

Information about the currently installed license.

**Columns:**

- **expiretimestamp** _(timestamp with time zone)_
  The timestamp of when the license expires.
- **installtimestamp** _(timestamp with time zone)_
  The timestamp of when the license was installed.
- **organization** _(text)_
  The name of the organization that owns the license.
- **licensetype** _(text)_
  The type of the license such as Enterprise.
- **licensecount** _(integer)_
  The number of hosts that the license covers.

## Table: oauth_access_tokens

OAuth access tokens and expiration.

**Columns:**

- **access_token** _(character varying(40))_
  The access token that grants access to the OAuth client.
- **client_id** _(character varying(80))_
  The client identifier of the OAuth client that obtained the access token.
- **user_id** _(character varying(255))_
  The user identifier of the user that authorized the access token.
- **expires** _(timestamp without time zone)_
  The timestamp of when the access token expires.
- **scope** _(character varying(2000))_
  The scope of access that the access token grants.

## Table: oauth_authorization_codes

OAuth authorizations.

**Columns:**

- **authorization_code** _(character varying(40))_
  The authorization code that grants access to the OAuth client.
- **client_id** _(character varying(80))_
  The client identifier of the OAuth client that requested the authorization code.
- **user_id** _(character varying(255))_
  The user identifier of the user that authorized the OAuth client.
- **redirect_uri** _(character varying(2000))_
  The URI that the OAuth client will redirect to after obtaining the authorization code.
- **expires** _(timestamp without time zone)_
  The timestamp of when the authorization code expires.
- **scope** _(character varying(2000))_
  The scope of access that the authorization code grants.

## Table: oauth_clients

OAuth clients.

**Columns:**

- **client_id** _(character varying(80))_
  The unique identifier of the OAuth client.
- **client_secret** _(character varying(80))_
  The secret key of the OAuth client.
- **redirect_uri** _(character varying(2000))_
  The URI that the OAuth client will redirect to after authorization.
- **grant_types** _(character varying(80))_
  The grant types that the OAuth client supports, such as authorization_code, password, etc.
- **scope** _(character varying(100))_
  The scope of access that the OAuth client requests, such as read, write, etc.
- **user_id** _(character varying(80))_
  The user identifier that the OAuth client is associated with.

## Table: oauth_jwt

OAuth JSON Web Tokens.

**Columns:**

- **client_id** _(character varying(80))_
  The client identifier of the OAuth client that uses JSON Web Tokens.
- **subject** _(character varying(80))_
  The subject of the JSON Web Token, usually the user identifier.
- **public_key** _(character varying(2000))_
  The public key of the OAuth client that verifies the JSON Web Token signature.

## Table: oauth_refresh_tokens

OAuth token expiration.

**Columns:**

- **refresh_token** _(character varying(40))_
  The refresh token that can be used to obtain a new access token.
- **client_id** _(character varying(80))_
  The client identifier of the OAuth client that obtained the refresh token.
- **user_id** _(character varying(255))_
  The user identifier of the user that authorized the OAuth client.
- **expires** _(timestamp without time zone)_
  The timestamp of when the refresh token expires.
- **scope** _(character varying(2000))_
  The scope of access that the refresh token grants.

## Table: oauth_scopes

OAuth scopes.

**Columns:**

- **scope** _(text)_
  The name of the OAuth scope, such as read, write, etc.
- **is_default** _(boolean)_
  The flag that indicates whether the OAuth scope is the default scope for new clients.

## Table: rbac_permissions

RBAC permissions.

**Columns:**

- **alias** _(character varying(100))_
  The unique alias of the RBAC permission, used as the primary key.
- **group** _(character varying(50))_
  The group that the RBAC permission belongs to, such as Inventory API, Changes API, Events API, Hosts, etc.
- **name** _(character varying(100))_
  The name of the RBAC permission, such as Get inventory report, Get event list, etc.
- **description** _(character varying(200))_
  The description of the RBAC permission, explaining what it does and why it is needed.
- **application** _(character varying(50))_
  The application that the RBAC permission applies to, such as API, Mission Portal, etc.
- **allowed_by_default** _(boolean)_
  The flag that indicates whether the RBAC permission is allowed by default for new roles, defaults to false.

## Table: rbac_role_permission

This table associates roles to permissions in a 1-to-many relationship.

**Columns:**

- **role_id** _(character varying)_
  The name of the role that has the permission.
- **permission_alias** _(character varying)_
  The alias of the permission that the role has.

## Table: remote_hubs

Information about federated reporting feeder hubs when federated reporting has been enabled.

**Columns:**

- **id** _(bigint)_
  The unique identifier of the remote hub, generated from a sequence.
- **hostkey** _(text)_
  The host key of the remote hub.
- **ui_name** _(character varying(70))_
  The user-friendly name of the remote hub, must be unique among all remote hubs.
- **api_url** _(text)_
  The URL of the remote hub API, used for communication and data transfer.
- **target_state** _(character varying(20))_
  The desired state of the remote hub such as on, paused.
- **transport** _(json)_
  The JSON object that stores the transport settings of the remote hub with keys such as mode, ssh_user, ssh_host, ssh_pubkey.
- **role** _(character varying(50))_
  The role of the remote hub, such as feeder or superhub.

## Table: roles

Role definitions that manage host visibility.

**Columns:**

- **name** _(text)_
  The name of the role, must be unique and not null.
- **description** _(text)_
  The description of the role.
- **include_rx** _(text)_
  The regular expression that matches classes reported by the host governing what the role can see.
- **exclude_rx** _(text)_
  The regular expression that matches classes reported by the host governing what the role cannot see.
- **changetimestamp** _(timestamp with time zone)_
  The timestamp of when the role was last change.
- **is_default** _(boolean)_
  The boolean flag that indicates whether the role is the default role for new users, defaults to false.

## Table: scheduledreports

Users scheduled reports.

**Columns:**

- **username** _(text)_
  The username of the user who scheduled the report.
- **query** _(text)_
  The SQL query that defines the report.
- **query_id** _(text)_
  The unique identifier of the query.
- **run_classes** _(text)_
  A CFEngine class expression (without ::) such as (January|February|March|April|May|June|July|August|September|October|November|December).GMT_Hr22.Min50_55 describing when the report should be run.
- **last_executed** _(text)_
  The timestamp of when the report was last executed.
- **email** _(text)_
  The email address of the user who scheduled the report.
- **email_title** _(text)_
  The title of the email that contains the report.
- **email_description** _(text)_
  The description which is present in the email providing the report.
- **host_include** _(text[])_
  The array of hosts that the report should include.
- **host_exclude** _(text[])_
  The array of hosts that the report should exclude (overriding inclusions).
- **already_run** _(boolean)_
  The boolean flag that indicates whether the report has already run or not.
- **enabled** _(boolean)_
  The boolean flag that indicates whether the report is enabled or not.
- **output** _(text[])_
  The array of output formats (csv, pdf) that the report should generate.
- **excludedhosts** _(json)_
  The JSON object that stores the hosts that are excluded from the report.

## Table: settings

User settings and preferences for RBAC, host not reporting threshold, collision threshold (duplicate host indicator), and Enterprise API log level. Populated when non-default settings are saved.

**Columns:**

- **key** _(text)_
  The Key of the setting.
- **value** _(json)_
  The value of the setting.

## Table: ssh_keys

Generated ssh keys.

**Columns:**

- **id** _(bigint)_
  The unique identifier of the ssh key, generated from a sequence.
- **public_key** _(text)_
  The public key of the ssh key, used for authentication and encryption.
- **private_key** _(text)_
  The private key of the ssh key, used for decryption and signing.
- **generated_at** _(timestamp with time zone)_
  The timestamp of when the ssh key was generated, defaults to the current time.
- **generated_by** _(text)_
  The username of the user who generated the ssh key.

## Table: users

User settings (name, email, password, timezone, provenance) and roles associated with the user.

**Columns:**

- **username** _(text)_
  The username of the user.
- **password** _(text)_
  The hashed password of the user.
- **salt** _(text)_
  The salt used to hash the password of the user.
- **name** _(text)_
  The name of the user.
- **email** _(text)_
  The email address of the user.
- **external** _(boolean)_
  The boolean flag that indicates whether the user is an external user or not, defaults to false.
- **active** _(boolean)_
  The boolean flag that indicates whether the user is active or not, defaults to false.
- **roles** _(text[])_
  The array of roles that the user has, defaults to an empty array.
- **time_zone** _(text)_
  The timestamp of when the user settings were last changed.
- **changetimestamp** _(timestamp with time zone)_
  The time zone of the user, defaults to Etc/GMT+0.

## Table: setup_codes

Stores setup codes used to complete hub setup.

**Columns:**

- **id** _(serial)_
  Unique auto-incrementing identifier.
- **code** _(char(6))_
  Six-character code.
- **created_at** _(timestamp with time zone)_
  Timestamp indicating when the setup code was created, defaults to NOW().
- **expires_at** _(timestamp with time zone)_
  Timestamp indicating when the setup code will expire.
- **attempts** _(integer)_
  Number of attempts made to use the setup code, defaults to 0.
- **is_revoked** _(boolean)_
  Indicates whether the setup code has been revoked before expiration, defaults to false.
- **is_used** _(boolean)_
  Indicates whether the setup code has been successfully used, defaults to false.
- **session_id** _(varchar(64))_
  Session identifier linking the setup code to a session, can be null.
