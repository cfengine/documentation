---
layout: default
title: cfsettings
published: true
---

Settings used by Mission Portal APIs, no reported data.

## Table: audit_logs

Stores system logs about actions performed by users.

**Columns:**

* **id** *(bigint)*
  The unique identifier of audit log event, generated from a sequence.
* **time** *(timestamp without a time zone)*
  Time when an event happened.
* **action** *(text)*
   What was done (e.g., updated, created, deleted, deployed).
* **object_type** *(text)*
  Type of affected object (e.g., user, role, build project).
* **object_id** *(text)*
  Identifier of an affected object (e.g. user, role id, build project id), if applicable.
* **details** *(json)*
  More details in the free-json format.
* **ip_address** *(boolean)*
  IP address of the user who performed the action.


## Table: build_modules

Information about build modules available from the index (build.cfengine.com).

**Columns:**

* **name**          *(text)*
  The name of the build module.
* **readme**        *(text)*
  The readme file content of the build module in HTML.
* **description**   *(text)*
  The description of the build module.
* **version**       *(text)*
  The version of the build module.
* **author**        *(jsonb)*
  The author information of the build module as a JSON object with keys such as url, name, image.
* **updated**       *(timestamp with time zone)*
  The last updated time of the build module.
* **downloads**     *(integer)*
  The number of downloads of the build module.
* **repo**          *(text)*
  The repository URL of the build module.
* **documentation** *(text)*
  The documentation URL of the build module.
* **website**       *(text)*
  The website URL of the build module.
* **subdirectory**  *(text)*
  The subdirectory of the build module in the repository.
* **commit**        *(text)*
  The commit hash of the build module.
* **dependencies**  *(jsonb)*
  The dependencies of the build module as a JSON object.
* **tags**          *(jsonb)*
  The tags of the build module as a JSON object.
* **versions**      *(jsonb)*
  The available versions of the build module as a JSON object.
* **latest**        *(boolean)*
  A flag indicating whether the build module is the latest version.
* **ts_vector**     *(tsvector)**
  Generated ts_vector column based on id and description.

## Table: build_projects

Build application projects.

**Columns:**

* **id**                  *(bigint)*
  The unique identifier of the build project, generated from a sequence.
* **repository_url**      *(text)*
  The URL of the git repository that contains the build project.
* **branch**              *(text)*
  The branch of the git repository that the build project uses.
* **name**                *(text)*
  The name of the build project, derived from the repository URL and branch.
* **authentication_type** *(authentication_types)*
  The type of authentication that the build project uses to access the git repository. Must match authentication_types such as password or private_key.
* **username**            *(text)*
  The username that the build project uses to access the git repository, if applicable.
* **password**            *(text)*
  The password that the build project uses to access the git repository, if applicable.
* **ssh_private_key**     *(text)*
  This field is not used. Ref ENT-11330.
* **ssh_key_id**          *(integer)*
  The foreign key that references the ssh_keys table, if applicable.
* **created_at**          *(timestamp with time zone)*
  The timestamp of when the build project was created.
* **pushed_at**           *(timestamp with time zone)*
  The timestamp of when the build project was last pushed to the git repository.
* **is_local**            *(boolean)*
  The flag that indicates whether the build project is local or remote.
* **is_deployed_locally** *(boolean)*
  The flag that indicates whether the build project is deployed locally or not.
* **action**              *(text)*
  The action that the build project performs, such as push, pushAndDeploy, localDeploy.

## Table: cfbs_requests

cfbs requests and responses handled by cf-reactor.

**Columns:**

* **id**           *(bigint)*
  The unique identifier of the cfbs request, generated from a sequence.
* **request_name** *(text)*
  The name of the cfbs request, such as init_project, local_deploy, etc.
* **arguments**    *(jsonb)*
  The JSONB object that stores the arguments of the cfbs request, such as git, project_id, etc.
* **created_at**   *(timestamp with time zone)*
  The timestamp of when the cfbs request was created.
* **finished_at**  *(timestamp with time zone)*
  The timestamp of when the cfbs request was finished, may be null if the request is still in progress.
* **response**     *(jsonb)*
  The JSONB object that stores the response of the cfbs request, such as status, details, etc.

## Table: external_roles_map

Map of external directory group to Mission Portal RBAC role for automatic association of directory users to Mission Portal roles.

**Columns:**

* **external_role**   *(text)*
  The name of the external directory (LDAP/Active Directory) group.
* **internal_role**   *(text)*
  The name of the internal Mission Portal role, such as admin, auditor, or guest.
* **changetimestamp** *(timestamp with time zone)*
  The timestamp of when the mapping was last changed.

## Table: federated_reporting_settings

Federated reporting settings when enabled.

**Columns:**

* **key**    *(character varying)*
  The name of the federated reporting setting, such as enable_as, enable_request_sent, or target_state.
* **value**  *(text)*
  The value of the federated reporting setting, such as superhub, 1, or on.

## Table: inventory_aliases

Inventory attributes aliases.

**Columns:**

* **inventory_attribute** *(text)*
  The name of the inventory attribute, such as Kernel, Kernel Release, etc.
* **alias**               *(text)*
  The alias of the inventory attribute, such as os type, os kernel, etc.

## Table: keyspendingfordeletion

Keys of deleted hosts yet to be deleted.

**Columns:**

* **hostkey** *(text)*
  The key of the host that was deleted from the database but not yet from the ppkeys directory.

## Table: licenseinfo

Information about the currently installed license.

**Columns:**

* **expiretimestamp**  *(timestamp with time zone)*
  The timestamp of when the license expires.
* **installtimestamp** *(timestamp with time zone)*
  The timestamp of when the license was installed.
* **organization**     *(text)*
  The name of the organization that owns the license.
* **licensetype**      *(text)*
  The type of the license such as Enterprise.
* **licensecount**     *(integer)*
  The number of hosts that the license covers.

## Table: oauth_access_tokens

OAuth access tokens and expiration.

**Columns:**

* **access_token** *(character varying(40))*
  The access token that grants access to the OAuth client.
* **client_id**    *(character varying(80))*
  The client identifier of the OAuth client that obtained the access token.
* **user_id**      *(character varying(255))*
  The user identifier of the user that authorized the access token.
* **expires**      *(timestamp without time zone)*
  The timestamp of when the access token expires.
* **scope**        *(character varying(2000))*
  The scope of access that the access token grants.

## Table: oauth_authorization_codes

OAuth authorizations.

**Columns:**

* **authorization_code** *(character varying(40))*
  The authorization code that grants access to the OAuth client.
* **client_id**          *(character varying(80))*
  The client identifier of the OAuth client that requested the authorization code.
* **user_id**            *(character varying(255))*
  The user identifier of the user that authorized the OAuth client.
* **redirect_uri**       *(character varying(2000))*
  The URI that the OAuth client will redirect to after obtaining the authorization code.
* **expires**            *(timestamp without time zone)*
  The timestamp of when the authorization code expires.
* **scope**              *(character varying(2000))*
  The scope of access that the authorization code grants.

## Table: oauth_clients

OAuth clients.

**Columns:**

* **client_id**     *(character varying(80))*
  The unique identifier of the OAuth client.
* **client_secret** *(character varying(80))*
  The secret key of the OAuth client.
* **redirect_uri**  *(character varying(2000))*
  The URI that the OAuth client will redirect to after authorization.
* **grant_types**   *(character varying(80))*
  The grant types that the OAuth client supports, such as authorization_code, password, etc.
* **scope**         *(character varying(100))*
  The scope of access that the OAuth client requests, such as read, write, etc.
* **user_id**       *(character varying(80))*
  The user identifier that the OAuth client is associated with.

## Table: oauth_jwt

OAuth JSON Web Tokens.

**Columns:**

*  **client_id**  *(character varying(80))*
  The client identifier of the OAuth client that uses JSON Web Tokens.
*  **subject**    *(character varying(80))*
  The subject of the JSON Web Token, usually the user identifier.
*  **public_key** *(character varying(2000))*
  The public key of the OAuth client that verifies the JSON Web Token signature.

## Table: oauth_refresh_tokens

OAuth token expiration.

**Columns:**

*  **refresh_token** *(character varying(40))*
  The refresh token that can be used to obtain a new access token.
*  **client_id**     *(character varying(80))*
  The client identifier of the OAuth client that obtained the refresh token.
*  **user_id**       *(character varying(255))*
  The user identifier of the user that authorized the OAuth client.
*  **expires**       *(timestamp without time zone)*
  The timestamp of when the refresh token expires.
*  **scope**         *(character varying(2000))*
  The scope of access that the refresh token grants.

## Table: oauth_scopes

OAuth scopes.

**Columns:**

* **scope**      *(text)*
  The name of the OAuth scope, such as read, write, etc.
* **is_default** *(boolean)*
  The flag that indicates whether the OAuth scope is the default scope for new clients.

## Table: rbac_permissions

RBAC permissions.

**Columns:**

* **alias**              *(character varying(100))*
  The unique alias of the RBAC permission, used as the primary key.
* **group**              *(character varying(50))*
  The group that the RBAC permission belongs to, such as Inventory API, Changes API, Events API, Hosts, etc.
* **name**               *(character varying(100))*
  The name of the RBAC permission, such as Get inventory report, Get event list, etc.
* **description**        *(character varying(200))*
  The description of the RBAC permission, explaining what it does and why it is needed.
* **application**        *(character varying(50))*
  The application that the RBAC permission applies to, such as API, Mission Portal, etc.
* **allowed_by_default** *(boolean)*
  The flag that indicates whether the RBAC permission is allowed by default for new roles, defaults to false.

## Table: rbac_role_permission

This table associates roles to permissions in a 1-to-many relationship.

**Columns:**

* **role_id**          *(character varying)*
  The name of the role that has the permission.
* **permission_alias** *(character varying)*
  The alias of the permission that the role has.

## Table: remote_hubs

Information about federated reporting feeder hubs when federated reporting has been enabled.

**Columns:**

* **id**           *(bigint)*
  The unique identifier of the remote hub, generated from a sequence.
* **hostkey**      *(text)*
  The host key of the remote hub.
* **ui_name**      *(character varying(70))*
  The user-friendly name of the remote hub, must be unique among all remote hubs.
* **api_url**      *(text)*
  The URL of the remote hub API, used for communication and data transfer.
* **target_state** *(character varying(20))*
  The desired state of the remote hub such as on, paused.
* **transport**    *(json)*
  The JSON object that stores the transport settings of the remote hub with keys such as mode, ssh_user, ssh_host, ssh_pubkey.
* **role**         *(character varying(50))*
  The role of the remote hub, such as feeder or superhub.

## Table: roles

Role definitions that manage host visibility.

**Columns:**

* **name**            *(text)*
  The name of the role, must be unique and not null.
* **description**     *(text)*
  The description of the role.
* **include_rx**      *(text)*
  The regular expression that matches classes reported by the host governing what the role can see.
* **exclude_rx**      *(text)*
  The regular expression that matches classes reported by the host governing what the role cannot see.
* **changetimestamp** *(timestamp with time zone)*
  The timestamp of when the role was last change.
* **is_default**      *(boolean)*
  The boolean flag that indicates whether the role is the default role for new users, defaults to false.

## Table: scheduledreports

Users scheduled reports.

**Columns:**

* **username**          *(text)*
  The username of the user who scheduled the report.
* **query**             *(text)*
  The SQL query that defines the report.
* **query_id**          *(text)*
  The unique identifier of the query.
* **run_classes**       *(text)*
  A CFEngine class expression (without ::) such as (January|February|March|April|May|June|July|August|September|October|November|December).GMT_Hr22.Min50_55 describing when the report should be run.
* **last_executed**     *(text)*
  The timestamp of when the report was last executed.
* **email**             *(text)*
  The email address of the user who scheduled the report.
* **email_title**       *(text)*
  The title of the email that contains the report.
* **email_description** *(text)*
  The description which is present in the email providing the report.
* **host_include**      *(text[])*
  The array of hosts that the report should include.
* **host_exclude**      *(text[])*
  The array of hosts that the report should exclude (overriding inclusions).
* **already_run**       *(boolean)*
  The boolean flag that indicates whether the report has already run or not.
* **enabled**           *(boolean)*
  The boolean flag that indicates whether the report is enabled or not.
* **output**            *(text[])*
  The array of output formats (csv, pdf) that the report should generate.
* **excludedhosts**     *(json)*
  The JSON object that stores the hosts that are excluded from the report.

## Table: settings

User settings and preferences for RBAC, host not reporting threshold, collision threshold (duplicate host indicator), and Enterprise API log level. Populated when non-default settings are saved.

**Columns:**

* **key**    *(text)*
  The Key of the setting.
* **value**  *(json)*
  The value of the setting.

## Table: ssh_keys

Generated ssh keys.

**Columns:**

* **id**           *(bigint)*
  The unique identifier of the ssh key, generated from a sequence.
* **public_key**   *(text)*
  The public key of the ssh key, used for authentication and encryption.
* **private_key**  *(text)*
  The private key of the ssh key, used for decryption and signing.
* **generated_at** *(timestamp with time zone)*
  The timestamp of when the ssh key was generated, defaults to the current time.
* **generated_by** *(text)*
  The username of the user who generated the ssh key.

## Table: users

User settings (name, email, password, timezone, provenance) and roles associated with the user.

**Columns:**

* **username**        *(text)*
  The username of the user.
* **password**        *(text)*
  The hashed password of the user.
* **salt**            *(text)*
  The salt used to hash the password of the user.
* **name**            *(text)*
  The name of the user.
* **email**           *(text)*
  The email address of the user.
* **external**        *(boolean)*
  The boolean flag that indicates whether the user is an external user or not, defaults to false.
* **active**          *(boolean)*
  The boolean flag that indicates whether the user is active or not, defaults to false.
* **roles**           *(text[])*
  The array of roles that the user has, defaults to an empty array.
* **time_zone**       *(text)*
  The timestamp of when the user settings were last changed.
* **changetimestamp** *(timestamp with time zone)*
  The time zone of the user, defaults to Etc/GMT+0.
