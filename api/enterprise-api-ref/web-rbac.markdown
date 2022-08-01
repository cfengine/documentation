---
layout: default
title: Web RBAC API
published: true
tags: [reference, enterprise, API, settings, RBAC]
---
Web RBAC API for managing role based access control settings.

## Get all permissions list

**URI:** https://hub.cfengine.com/api/rbac

**Method:** GET

**Example request (curl):**

```
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/rbac
```

**Example response:**

```
[
    {
        "alias": "Inventory.post",
        "group": "Inventory API",
        "name": "Get inventory report",
        "description": "",
        "application": "API",
        "allowed_by_default": true
    },
    {
        "alias": "VariablesDictionary.get",
        "group": "Inventory API",
        "name": "Get inventory attributes",
        "description": "",
        "application": "API",
        "allowed_by_default": true
    },
    {
        "alias": "variablesDictionaryUpdate.post",
        "group": "Inventory API",
        "name": "Update inventory attributes",
        "description": "",
        "application": "API",
        "allowed_by_default": true
    }
]
```

**Output:**

* **alias** *(string)*
    Alias (ID) of a permission
* **group** *(string)*
    Group of a permission.
* **name** *(string)*
    Name of a permission.
* **description** *(string)*
    Description of a permission.
* **application** *(string)*
    Application of a permission. Allowed values: `API`, `Mission portal`
* **allowed_by_default** *(boolean)*
    Permission allowed by default. New role will be able to perform allowed by default actions.

## Get current user permissions

**URI:** https://hub.cfengine.com/api/rbac/user-permissions

**Method:** GET

**Example request (curl):**

```
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/rbac/user-permissions
```

**Example response:**
```
[
    {
        "alias": "Inventory.post",
        "group": "Inventory API",
        "name": "Get inventory report",
        "description": "",
        "application": "API",
        "allowed_by_default": true
    },
    {
        "alias": "VariablesDictionary.get",
        "group": "Inventory API",
        "name": "Get inventory attributes",
        "description": "",
        "application": "API",
        "allowed_by_default": true
    },
    {
        "alias": "variablesDictionaryUpdate.post",
        "group": "Inventory API",
        "name": "Update inventory attributes",
        "description": "",
        "application": "API",
        "allowed_by_default": true
    }
]
```


## Get role permissions

**URI:** https://hub.cfengine.com/api/role/:role_name/permissions

**Method:** GET

**Parameters:**

* **role_name** *(string)*
    Role name

**Example request (curl):**

```
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/role/admin/permissions
```

**Example response:**

```
[
    {
        "alias": "Inventory.post",
        "group": "Inventory API",
        "name": "Get inventory report",
        "description": "",
        "application": "API",
        "allowed_by_default": true
    },
    {
        "alias": "VariablesDictionary.get",
        "group": "Inventory API",
        "name": "Get inventory attributes",
        "description": "",
        "application": "API",
        "allowed_by_default": true
    },
    {
        "alias": "variablesDictionaryUpdate.post",
        "group": "Inventory API",
        "name": "Update inventory attributes",
        "description": "",
        "application": "API",
        "allowed_by_default": true
    }
]
```

## Add permissions to role 

**URI:** https://hub.cfengine.com/api/role/:role_name/permissions

**Method:** POST

Assign new permission to role. Permissions will be added to existing permission list.

**Parameters:**

* **role_name** *(string)*
    Role name
    
* **alias** *(array)*
    Array of permission aliases `Emp: ["Inventory.post", "VariablesDictionary.get"]`. Required parameter.

**Example request (curl):**
 
```
curl -k --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/role/role_name/permissions \
  -H 'content-type: application/json' \
  -d '["Inventory.post", "VariablesDictionary.get"]'
```

**Example response:**

```
 HTTP 201 Created
```


## Rewrite role's permissions 

**URI:** https://hub.cfengine.com/api/role/:role_name/permissions

**Method:** PUT

Assign permission to role. New permissions replace existing. 

**Parameters:**

* **role_name** *(string)*
    Role name
    
* **alias** *(array)*
    Array of permission aliases `Emp: ["Inventory.post", "VariablesDictionary.get"]`. Required parameter.

**Example request (curl):**
 
```
curl -k --user <username>:<password> \
  -X PUT \
  https://hub.cfengine.com/api/role/role_name/permissions \
  -H 'content-type: application/json' \
  -d '["Inventory.post", "VariablesDictionary.get"]'
```

**Example response:**

```
 HTTP 201 Created
```


## Revoke permissions from role

**URI:** https://hub.cfengine.com/api/role/:role_name/permissions

**Method:** DELETE

**Parameters:**

* **role_name** *(string)*
    Role name

* **alias** *(array)*
    Array of permission aliases `Emp: ["Inventory.post", "VariablesDictionary.get"]`. Required parameter.

**Example request (curl):**
 
```
curl -k --user <username>:<password> \
  -X DELETE \
  https://hub.cfengine.com/api/role/role_name/permissions \
  -H 'content-type: application/json' \
  -d '["Inventory.post", "VariablesDictionary.get"]'
```

**Example response:**

```
 HTTP 204 No Content
```