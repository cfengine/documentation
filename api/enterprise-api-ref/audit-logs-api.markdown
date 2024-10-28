---
layout: default
title: Audit logs API
published: true
---

Audit logs API provides access to system audit logs that track user actions across the platform made to critical parts
such as settings, host data, users, roles, Build projects, etc.

## Get audit logs

**URI:** https://hub.cfengine.com/api/audit-logs

**Method:** GET

**Parameters:**

* **actor** *(string)*
  Filter by user who performed the action.
* **object_type** *(string)*
  Filter by object type (see [Allowed object types][Audit logs API#Allowed object types]).
* **action** *(string)*
  Filter by action type (see [Allowed actions][Audit logs API#Allowed actions]).
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
    * object_type
* **sort_direction** *(string, default: "DESC")*
  Sort direction. Allowed values:
    * ASC (ascending)
    * DESC (descending)

**Example request (curl):**

```console
curl --user <username>:<password> -X GET https://hub.cfengine.com/api/audit-logs
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
| created              | Resource creation         |
| updated              | Resource update           |
| deleted              | Resource deletion         |
| deployed             | Deployment action         |
| pushed               | Push action               |
| module added         | Module addition           |
| module deleted       | Module removal            |
| module updated       | Module modification       |
| module input updated | Module input modification |
| CMDB updated         | CMDB update               |
| CMDB deleted         | CMDB deletion             |
| CMDB created         | CMDB creation             |
| RBAC updated         | RBAC modification         |

### Allowed object types

| Object Type         | Description                                  |
|---------------------|----------------------------------------------|
| user                | User account                                 |
| role                | Role definition                              |
| settings            | System, Mail, VCS or Authentication settings |
| federated reporting | Federated reporting configuration            |
| group               | Host groups                                  |
| host                | Host configuration                           |
| Build project       | Build project configuration                  |
