---
layout: default
title: Users and Access-Control REST API
published: true
tags: [reference, enterprise, REST, API, reporting, URI, users, rbac]
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
      "external": false
    },
    {
      "id": "admin",
      "name": "admin",
      "email": "admin@organisation.com",
      "roles": [
        "admin",
        "cf_remoteagent"
      ],
      "external": false
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

**Example usage:** `Example: Listing Users`

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
      "time_zone": "Europe/Oslo"
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

**Example usage:** `Example: Retrieving a User`

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

**Example usage:** `Example: Creating a New User`

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

**Example usage:** `Example: Updating an Existing User`, `Example: Adding a User to a Role`

## Delete user

**URI:** https://hub.cfengine.com/api/user/:username

**Method:** DELETE

Remove internal user.
API call allowed only for administrator.

**Example usage:** `Example: Deleting a User`

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
