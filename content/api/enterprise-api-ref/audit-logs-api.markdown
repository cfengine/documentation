---
layout: default
title: Audit log API
---

Audit log API provides access to system audit logs that track user actions across the platform made to critical parts
such as settings, host data, users, roles, Build projects, etc.

## Get audit logs

**URI:** https://hub.cfengine.com/api/audit-log

**Method:** GET

**Parameters:**

* **actor** *(string)*
  Filter by user who performed the action.
* **object_type** *(string)*
  Filter by object type (see [Allowed object types][Audit log API#Allowed object types]).
* **action** *(string)*
  Filter by action type (see [Allowed actions][Audit log API#Allowed actions]).
* **object_name** *(integer)*
  Filter by object name.
* **created_after** *(integer)*
  Unix timestamp to filter logs after this time.
* **created_before** *(integer)*
  Unix timestamp to filter logs before this time.
* **page** *(integer)*
  Page number for pagination (default: 1).
* **offset** *(integer)*
    Number of results to skip for the processed query.
* **sort_column** *(string)*
    Column to sort by. Allowed values:
    * time
    * actor
    * action
    * object_id
    * object_name
    * object_type
* **sort_direction** *(string, default: "DESC")*
  Sort direction. Allowed values:
    * ASC (ascending)
    * DESC (descending)

**Example request (curl):**

```console
curl --user <username>:<password> -X GET https://hub.cfengine.com/api/audit-log
```

**Successful response example:**

```
HTTP 200 OK
{
    "data": [
        {
            "id": 4,
            "time": "2024-10-24 09:47:08.329041",
            "actor": "admin",
            "action": "created",
            "object_type": "user",
            "object_name": "test",
            "object_id": "test",
            "details": [
                "Created user `test`."
            ]
        },
        {
            "id": 3,
            "time": "2024-10-24 09:46:56.204391",
            "actor": "admin",
            "action": "created",
            "object_name": "test",
            "object_type": "role",
            "object_id": "test",
            "details": [
                "Created role `test`.",
                {
                    "description": "test",
                    "excludeContext": "",
                    "includedContext": "test"
                }
            ]
        },
        {
            "id": 2,
            "time": "2024-10-24 09:46:42.595813",
            "actor": "admin",
            "action": "updated",
            "object_type": "settings",
            "object_name": "Preferences",
            "object_id": null,
            "details": [
                "Settings updated.",
                {
                    "changes": [
                        "minPasswordLength"
                    ]
                }
            ]
        }
    ],
    "meta": {
        "count": 4,
        "page": 1,
        "timestamp": 1729763237,
        "total": 4
    }
}
```

**Responses:**

| HTTP response code           | Description                          |
|------------------------------|--------------------------------------|
| 200 OK                       | Audit logs returned                  |
| 422 Unprocessable entity     | Validation error occurred            |
| 401 Unauthorized             | Authorization is missing             |
| 403 Insufficient permissions | Audit logs are not available to user |
| 500 Internal server error    | Internal server error                |


### Allowed actions

| Action               | Description               |
|----------------------|---------------------------|
| Created              | Resource creation         |
| Updated              | Resource update           |
| Deleted              | Resource deletion         |
| Deployed             | Deployment action         |
| Pushed               | Push action               |
| Module added         | Module addition           |
| Module deleted       | Module removal            |
| Module updated       | Module modification       |
| Module input updated | Module input modification |
| CMDB updated         | CMDB update               |
| CMDB deleted         | CMDB deletion             |
| CMDB created         | CMDB creation             |
| RBAC updated         | RBAC modification         |

### Allowed object types

| Object Type         | Description                                  |
|---------------------|----------------------------------------------|
| User                | User account                                 |
| Role                | Role definition                              |
| Settings            | System, Mail, VCS or Authentication settings |
| Federated reporting | Federated reporting configuration            |
| Group               | Host groups                                  |
| Host                | Host configuration                           |
| Build project       | Build project configuration                  |


## Get audit logs actors

Returns list of users who performed actions.

**URI:** https://hub.cfengine.com/api/audit-log/actors

**Method:** GET

**Example request (curl):**

```console
curl --user <username>:<password> -X GET https://hub.cfengine.com/api/audit-log/actors
```

**Successful response example:**

```
HTTP 200 OK
[
    "admin",
    "test"
]
```

## Get audit logs object name by type

Returns list of object names filtered by type.

**URI:** https://hub.cfengine.com/api/audit-log/:type/names

**Method:** GET

**Parameters:**

* **object_type** *(string)*
  Filter by object type (see [Allowed object types][Audit log API#Allowed object types]).

**Example request (curl):**

```console
curl --user <username>:<password> -X GET https://hub.cfengine.com/api/audit-log/Settings/names
```

**Successful response example:**

```
HTTP 200 OK
[
    "Preferences",
    "Mail",
    "VCS",
    "Authentication",
]
```
