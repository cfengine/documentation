---
layout: default
title: Users and access-control REST API
---

This REST API allows to manage users allowed to use Mission Portal as also Role Based Access Control settings.

## List users

**URI:** https://hub.cfengine.com/api/user

**Method:** GET

List all users.
API call allowed only for administrator.

**Parameters:**

* **id** *(regex string)*
    Regular expression for filtering usernames.
* **external** *('true', 'false')*
    Returns only internal users (false) or only external (true), or all if not specified.

**Example response:**

```
{
  "meta": {
    "page": 1,
    "count": 3,
    "total": 3,
    "timestamp": 1437383957
  },
  "data": [
    {
      "id": "CFE_ROBOT",
      "email": "admin@organisation.com",
      "roles": [
        "admin",
        "cf_remoteagent"
      ],
      "external": false,
      "two_factor_enabled": true
    },
    {
      "id": "admin",
      "name": "admin",
      "email": "admin@organisation.com",
      "roles": [
        "admin",
        "cf_remoteagent"
      ],
      "external": false,
      "two_factor_enabled": false
    },
    {
      "id": "user_1",
      "email": "user_1@example.com",
      "roles": [
        "linux_team"
      ],
      "external": false
    }
  ]
}
```

**Output:**

* **id**
    User name.
* **email**
    Email address.
* **roles**
    List of assigned RBAC roles.
* **external**
    Is user from external source (LDAP/AD).
* **two_factor_enabled**
    If a user has enabled two-factor authentication

**Example usage:** `Example: Listing users`

## Get user data

**URI:** https://hub.cfengine.com/api/user/:username

**Method:** GET

Get info for a specified user.
API call allowed only for administrator.

**Example response:**

```
{
  "meta": {
    "page": 1,
    "count": 1,
    "total": 1,
    "timestamp": 1437385581
  },
  "data": [
    {
      "id": "user_1",
      "name": "",
      "email": "user_1@example.com",
      "roles": [
        "linux_team"
      ],
      "external": false,
      "time_zone": "Europe/Oslo",
      "two_factor_enabled": false
    }
  ]
}
```

**Output:**

* **id**
    User name.
* **email**
    Email address.
* **roles**
    List of assigned RBAC roles.
* **external**
    Is user from external source (LDAP/AD).
* **time_zone**
    Time zone
* **two_factor_enabled**
    If a user has enabled two-factor authentication

**Example usage:** `Example: Retrieving a user`

## Create new user

**URI:** https://hub.cfengine.com/api/user/:username

**Method:** PUT

**Parameters:**

* **username** *(string)*
    User name
* **password** *(string)*
    User password
* **email** *(string)*
    User email
* **roles** *(array)*
    User roles, emp: `["admin", "test"]`
* **time_zone** *(string)*
    Time zone

Create a new user.
API call allowed only for administrator.

**Example Request Body:**

```
{
  "email": "user_1@example.com",
  "roles": [
    "linux_team"
  ]
}
```

**Example usage:** `Example: Creating a new user`

## Update user

**URI:** https://hub.cfengine.com/api/user/:username

**Method:** POST

Update user information.
API call allowed only for administrator.

**Parameters:**

* **username** *(string)*
    User name
* **password** *(string)*
    User password
* **email** *(string)*
    User email
* **roles** *(array)*
    User roles, emp: `["admin", "test"]`
* **time_zone** *(string)*
    Time zone

**Example Request Body:**

```
{
  "email": "user_1@example.com",
  "roles": [
    "linux_team"
  ]
}
```

**Example usage:** `Example: Updating an existing user`, `Example: Adding a user to a role`

## Delete user

**URI:** https://hub.cfengine.com/api/user/:username

**Method:** DELETE

Remove internal user.
API call allowed only for administrator.

**Example usage:** `Example: Deleting a user`

## List RBAC roles

**URI:** https://hub.cfengine.com/api/role

**Method:** GET

List defined roles for Role Based Access Control.
API call allowed only for administrator.

**Example response:**

```
{
  "meta": {
    "page": 1,
    "count": 3,
    "total": 3,
    "timestamp": 1437391879
  },
  "data": [
    {
      "id": "admin",
      "description": "Admin role"
    },
    {
      "id": "cf_remoteagent",
      "description": "Allow execution of cf-runagent"
    },
    {
      "id": "linux_team",
      "description": "Linux team is responsible for all linux test servers.",
      "includeContext": "linux,test_env",
      "excludeContext": "dev_env|production_env"
    }
  ]
}
```

**Output:**

* **id**
    Unique role name.
* **description**
    Role description.
* **includeContext**
    Permit access to hosts that have **class set**.
* **excludeContext**
    Permit access to hosts that have **class not set**.

## Get RBAC role

**URI:** https://hub.cfengine.com/api/role/:role_id

**Method:** GET

Get role definition.
API call allowed only for administrator.

**Example response:**

```
{
  "meta": {
    "page": 1,
    "count": 1,
    "total": 1,
    "timestamp": 1437392992
  },
  "data": [
    {
      "id": "linux_team",
      "description": "Linux team is responsible for all linux servers.",
      "includeContext": "linux"
    }
  ]
}
```

**Output:**

* **id**
    Unique role name.
* **description**
    Role description.
* **includeContext**
    Permit access to hosts that have **class set**.
* **excludeContext**
    Permit access to hosts that have **class not set**.

## Create RBAC role

**URI:** https://hub.cfengine.com/api/role/:role_id

**Method:** PUT

Create a new role definition.
API call allowed only for administrator.

**Fields:**

* **description**
    Role description.
* **includeContext**
    Permit access to hosts that have **class set**.
* **excludeContext**
    Permit access to hosts that have **class not set**.

**Example Request Body:**

```
{
  "description": "Linux team is responsible for all linux servers.",
  "includeContext": "linux",
  "excludeContext": "product_a"
}
```

## Update RBAC role

**URI:** https://hub.cfengine.com/api/role/:role_id

**Method:** POST

Update role definition.
API call allowed only for administrator.

**Fields:**

* **description**
    Role description.
* **includeContext**
    Permit access to hosts that have **class set**.
* **excludeContext**
    Permit access to hosts that have **class not set**

**Example Request Body:**

```
{
  "description": "Linux team is responsible for all linux servers.",
  "includeContext": "linux",
  "excludeContext": "product_a"
}
```

## Delete RBAC role

**URI:** https://hub.cfengine.com/api/role/:role_id

**Method:** DELETE

Remove role definition.
API call allowed only for administrator.

## Unlock user

If a system enforces using two-factor authentication (2FA),
users must configure it after their first login within 48 hours.
This endpoint unlocks users who have been locked out due to this reason
and grants an additional 48 hours to complete the 2FA setup.

Note: to be able to perform this action related RBAC rule (alias `user.unlock`) should be enabled.

**URI:** https://hub.cfengine.com/api/user/:username/unlock

**Method:** POST

**Example request (curl):**

```console
curl --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/user/tom/unlock
```

**Example response:**

```
HTTP 202 ACCEPTED
```
