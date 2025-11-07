---
layout: default
title: Shared groups API
aliases:
  - "/api-enterprise-api-ref-shared-groups.html"
---

The shared groups API enables creating host groups based on host filters (the same ones used in inventory) and assigning CMDB data to them.

## Create group

**URI:** https://hub.cfengine.com/api/host-groups/shared/

**Method:** POST

**Parameters:**

- **name** _(string)_
  Group name.

- **description** _(string)_
  Group description.

- **priority** _(number)_
  Group priority. Groups with a higher priority will take precedence in case of conflicts when merging CMDB data. (A lower number indicates higher priority, so 1 means 1st priority, 2 means 2nd most important, and so on).

- **filter** _(json object)_ Group filter object. Includes inventory filter and classes filters
  - **filter** _(json object)_ Optional parameter.
    Inventory filter data. You can use array values for multiple filter, the logic will be AND. Format is
  - **hostContextInclude** _(array)_ Optional parameter.
    Includes only results that concern hosts which have all specified CFEngine contexts (class) set.
  - **hostContextExclude** _(array)_ Optional parameter.
    Excludes results that concern hosts which have specified CFEngine context (class) set. Hosts that have at least one
    of the specified contexts set will be excluded from the results.
  - **hostFilter** _(json object)_ Optional parameter.
    - **includes** _(json object)_ Optional parameter.
      Object that specifies hosts to be included.
      - **includeAdditionally** _(boolean)_ Default: `false`
        Defines if hosts will be added to the results returned by inventory filters or class filters.
      - **entries** _(json object)_ Filter entries object. Where the key is an entry type and the value is an array of strings
        Allowed entry types: `hostkey`, `hostname`, `ip`, `mac`, `ip_mask`
    - **excludes** _(json object)_ Optional parameter.
      Object that specifies hosts to be excluded.
      - **entries** _(json object)_ Filter entries object. Where the key is an entry type and the value is an array of strings
        Allowed entry types: `hostkey`, `hostname`, `ip`, `mac`, `ip_mask`

  ```json
  {
    "filter": {
      "filter": { "Attribute name": { "operator": "value2" } },
      "hostFilter": {
        "includes": {
          "includeAdditionally": false,
          "entries": {
            "ip": ["192.168.56.5"],
            "hostkey": [],
            "hostname": ["ubuntu-bionic"],
            "mac": [
              "08:00:27:0b:a4:99",
              "08:00:27:dd:e1:59",
              "02:9f:d3:59:7e:90"
            ],
            "ip_mask": ["10.0.2.16/16"]
          }
        },
        "excludes": {
          "entries": {
            "ip": [],
            "hostkey": [],
            "hostname": [],
            "mac": [],
            "ip_mask": []
          }
        }
      },
      "hostContextExclude": ["class_value"],
      "hostContextInclude": ["class_value"]
    }
  }
  ```

**Operators:**

For filtering you can use the operators below:

| Operator        |
| --------------- |
| <               |
| >               |
| =               |
| !=              |
| <=              |
| >=              |
| matches         |
| not_match       |
| contains        |
| not_contain     |
| regex_matches   |
| regex_not_match |
| is_reported     |
| is_not_reported |

```
curl -k --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/host-groups/shared/ \
  -H 'content-type: application/json' \
  -d '{
        "name":"AIX hosts",
        "description":"Host name",
        "filter":{
            "filter": {
                "Architecture": {
                    "matches": "86"
                }
            },
            "hostContextInclude": [
                "aix"
            ]
        }
  }'
```

**Example response:**

```json
{
  "id": "4"
}
```

## Update group

**URI:** https://hub.cfengine.com/api/host-groups/shared/:id

**Method:** PATCH

**Parameters:**

- **id** _(integer)_
  Unique group identifier.

- **name** _(string)_
  Group name.

- **priority** _(number)_
  Group priority. Groups with a higher priority will take precedence in case of conflicts when merging CMDB data. (A lower number indicates higher priority, so 1 means 1st priority, 2 means 2nd most important, and so on).

- **description** _(string)_
  Group description.

- **filter** _(json object)_ Group filter object. Includes inventory filter and classes filters
  - **filter** _(json object)_ Optional parameter.
    Inventory filter data. You can use array values for multiple filter, the logic will be AND. Format is
  - **hostContextInclude** _(array)_ Optional parameter.
    Includes only results that concern hosts which have all specified CFEngine contexts (class) set.
  - **hostContextExclude** _(array)_ Optional parameter.
    Excludes results that concern hosts which have specified CFEngine context (class) set. Hosts that have at least one
    of the specified contexts set will be excluded from the results.
  - **hostFilter** _(json object)_ Optional parameter.
    - **includes** _(json object)_ Optional parameter.
      Object that specifies hosts to be included.
      - **includeAdditionally** _(boolean)_ Default: `false`
        Defines if hosts will be added to the results returned by inventory filters or class filters.
      - **entries** _(json object)_ Filter entries object. Where the key is an entry type and the value is an array of strings
        Allowed entry types: `hostkey`, `hostname`, `ip`, `mac`, `ip_mask`
    - **excludes** _(json object)_ Optional parameter.
      Object that specifies hosts to be excluded.
      - **entries** _(json object)_ Filter entries object. Where the key is an entry type and the value is an array of strings
        Allowed entry types: `hostkey`, `hostname`, `ip`, `mac`, `ip_mask`

```json
{
  "filter": {
    "filter": { "Attribute name": { "operator": "value2" } },
    "hostFilter": {
      "includes": {
        "includeAdditionally": false,
        "entries": {
          "ip": ["192.168.56.5"],
          "hostkey": [],
          "hostname": ["ubuntu-bionic"],
          "mac": [
            "08:00:27:0b:a4:99",
            "08:00:27:dd:e1:59",
            "02:9f:d3:59:7e:90"
          ],
          "ip_mask": ["10.0.2.16/16"]
        }
      },
      "excludes": {
        "entries": {
          "ip": [],
          "hostkey": [],
          "hostname": [],
          "mac": [],
          "ip_mask": []
        }
      }
    },
    "hostContextExclude": ["class_value"],
    "hostContextInclude": ["class_value"]
  }
}
```

**Operators:**

For filtering you can use the operators below:

| Operator        |
| --------------- |
| <               |
| >               |
| =               |
| !=              |
| <=              |
| >=              |
| matches         |
| not_match       |
| contains        |
| not_contain     |
| regex_matches   |
| regex_not_match |
| is_reported     |
| is_not_reported |

**Example request:**

```
curl -k --user <username>:<password> \
  -X PATCH \
  https://hub.cfengine.com/api/host-groups/shared/5 \
  -H 'content-type: application/json' \
  -d '{
        "name":"AIX hosts",
        "description":"Host name",
        "filter":{
            "filter": {
                "Architecture": {
                    "matches": "86"
                }
            },
            "hostContextInclude": [
                "aix"
            ]
        }
  }'
```

**Example response:**

```json
{
  "id": "4"
}
```

## Get group

**URI:** https://hub.cfengine.com/api/host-groups/shared/:id

**Method:** GET

**Parameters:**

- **id** _(integer)_
  Unique group identifier.

**Example request:**

```
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/host-groups/shared/4 \
  -H 'content-type: application/json'
```

**Example response:**

```json
{
  "id": 4,
  "name": "AIX hosts",
  "priority": 3,
  "description": "Host name",
  "creator": "admin",
  "creation_time": "2023-06-14 10:41:25.601112+00",
  "filter": {
    "filter": { "Architecture": { "matches": "86" } },
    "hostContextExclude": "",
    "hostContextInclude": ["aix"]
  },
  "type": "shared"
}
```

## Remove group

**URI:** https://hub.cfengine.com/api/host-groups/shared/:id

**Method:** DELETE

**Parameters:**

- **id** _(integer)_
  Unique group identifier.

**Example request:**

```
curl -k --user <username>:<password> \
  -X DELETE \
  https://hub.cfengine.com/api/host-groups/shared/4 \
  -H 'content-type: application/json'
```

## Groups list

**URI:** https://hub.cfengine.com/api/host-groups/shared

**Method:** GET

**Example request:**

```
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/host-groups/shared\
  -H 'content-type: application/json'
```

**Example response:**

```json
{
  "data": [
    {
      "id": 1,
      "name": "All hosts",
      "priority": 1,
      "description": "",
      "creator": "admin",
      "creation_time": "2023-05-29 09:55:36.878271+00",
      "filter": []
    },
    {
      "id": 4,
      "name": "AIX hosts",
      "priority": 2,
      "description": "Host name",
      "creator": "admin",
      "creation_time": "2023-06-14 10:41:25.601112+00",
      "filter": {
        "filter": { "Architecture": { "matches": "86" } },
        "hostContextExclude": "",
        "hostContextInclude": ["aix"]
      }
    }
  ],
  "meta": {
    "count": 2,
    "page": 1,
    "timestamp": 1686739758,
    "total": 2,
    "hostsCountCacheTime": null
  }
}
```

## Make shared group personal

**URI:** https://hub.cfengine.com/api/host-groups/shared/:id/makePersonal

**Method:** POST

**Parameters:**

- **id** _(integer)_
  Unique group identifier.

**Example request:**

```
curl -k --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/host-groups/shared/5/makePersonal
```

**Example response:**

API returns new ID of the personal group.

```json
{
  "id": "6"
}
```

# Shared Groups CMDB

The configuration management database (CMDB) API enables you to manage classes and variables for specific host groups.

## Get CMDB for specific shared group

You can see a list of stored group-specific configurations

**URI:** https://hub.cfengine.com/api/host-groups/v2/shared/:id/cmdb

**Method:** GET

**Parameters:**

- **id** _(integer)_
  Unique group identifier.
- **sortColumn** _(string)_
  Column to sort by. Default: `created_at`. Optional parameter.
- **sortDescending** _(boolean)_
  Sort in descending order. Default: `true`. Optional parameter.
- **limit** _(integer)_
  Limit the number of results. Default: `10`. Optional parameter.
- **skip** _(integer)_
  Number of results to skip for pagination. Default: `0`. Optional parameter.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/host-groups/v2/shared/4/cmdb?limit=20&skip=0
```

**Example response:**

```json
{
  "data": [
    {
      "id": 1,
      "group_id": 4,
      "type": "class",
      "name": "My_class",
      "description": "CMDB class example",
      "tags": ["production", "webserver"],
      "meta": {},
      "created_at": "2023-06-14 10:41:25.601112+00",
      "entries": [
        {
          "id": 1,
          "group_id": 4,
          "entry_id": 1,
          "item_name": "My_class",
          "item_type": "class",
          "item_value": null
        }
      ]
    }
  ],
  "meta": { "total": 1, "page": 1, "count": 1 }
}
```

## Get group's specific configuration

**URI:** https://hub.cfengine.com/api/host-groups/v2/shared/cmdb/:entry_id

**Method:** GET

**Parameters:**

- **entry_id** _(integer)_
  Unique entry identifier.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/host-groups/v2/shared/cmdb/5
```

**Example response:**

```json
{
  "id": 6,
  "group_id": 5,
  "type": "variable",
  "name": "server_ports",
  "description": "Server port configuration",
  "tags": ["network", "config"],
  "meta": {},
  "created_at": "2023-06-14 11:15:30.123456+00"
}
```

## Get group's CMDB sub-entry

**URI:** https://hub.cfengine.com/api/host-groups/v2/shared/:id/cmdb/subentry/:type/:name

**Method:** GET

**Parameters:**

- **id** _(integer)_
  Unique group identifier.
- **type** _(string)_
  Subentry type (`class` or `variable`)
- **name** _(string)_
  Subentry name.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/host-groups/v2/shared/5/cmdb/subentry/variable/Namespace:BundleName.Ports
```

**Example response:**

```json
{
  "id": 1,
  "group_id": 5,
  "entry_id": 6,
  "item_name": "Namespace:BundleName.Ports",
  "item_type": "variable",
  "item_value": "[\"80\", \"443\", \"8080\"]"
}
```

## Create configuration

**URI:** https://hub.cfengine.com/api/host-groups/v2/shared/:id/cmdb

**Method:** POST

**Parameters:**

- **id** _(integer)_
  Unique group identifier.

**Request body parameters:**

- **type** _(string)_
  Configuration type. Allowed values: `inventory`, `class`, `variable`, `policy_configuration`
- **name** _(string)_
  Configuration entry name (max 255 characters).
- **description** _(string)_
  Configuration description. Optional parameter.
- **tags** _(array)_
  Array of tags. Optional parameter.
- **meta** _(object)_
  Metadata object. Optional parameter.
- **entries** _(array)_
  Array of sub-entries with the following structure:
  - **item_name** _(string)_ - Name of the item (letters, numbers, dots, colons, underscores only)
  - **item_type** _(string)_ - Type of item (`class` or `variable`)
  - **item_value** _(mixed)_ - Value for variables (not used for classes). Optional parameter.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/host-groups/v2/shared/5/cmdb \
  -H 'content-type: application/json' \
  -d '{
    "type": "class",
    "name": "class1",
    "description": "CMDB class",
    "tags": ["test_tag"],
    "entries": [
      {
        "item_name": "class1",
        "item_type": "class"
      }
    ]
  }'
```

**Example response:**

```json
{
  "id": "6"
}
```

## Update configuration

**URI:** https://hub.cfengine.com/api/host-groups/v2/shared/cmdb/:entry_id

**Method:** PUT

**Parameters:**

- **entry_id** _(integer)_
  Unique entry identifier.

**Request body parameters:**

- **type** _(string)_
  Entry type. Examples: `class`, `variable`, `policy_configuration`, `inventory`

- **name** _(string)_
  Entry name.

- **description** _(string)_
  Entry description. Optional parameter.

- **tags** _(array)_
  Entry tags. Optional parameter.

- **meta** _(object)_
  Additional metadata. Optional parameter.

- **entries** _(array)_
  Array of subentries containing the actual configuration data.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X PUT \
  https://hub.cfengine.com/api/host-groups/v2/shared/cmdb/5 \
  -H 'content-type: application/json' \
  -d '{
    "type": "variable",
    "name": "updated_server_ports",
    "description": "Updated server port configuration",
    "tags": ["network", "config", "updated"],
    "entries": [
      {
        "item_name": "Namespace:BundleName.Ports",
        "item_type": "variable",
        "item_value": ["80", "443", "8080"]
      }
    ]
  }'
```

**Example response:**

```
HTTP 200 Ok
```

## Delete specific configuration entry

**URI:** https://hub.cfengine.com/api/host-groups/v2/shared/cmdb/:entry_id

**Method:** DELETE

**Parameters:**

- **entry_id** _(integer)_
  Unique entry identifier.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X DELETE \
  https://hub.cfengine.com/api/host-groups/v2/shared/cmdb/5
```

**Example response:**

```
HTTP 204 No Content
```
