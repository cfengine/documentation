---
layout: default
title: Shared groups API
---
The shared groups API enables creating host groups based on host filters (the same ones used in inventory) and assigning CMDB data to them.

## Create group

**URI:** https://hub.cfengine.com/api/host-groups/shared/

**Method:** POST

**Parameters:**

* **name** *(string)*
  Group name.

* **description** *(string)*
  Group description.

* **priority** *(number)*
  Group priority. Groups with a higher priority will take precedence in case of conflicts when merging CMDB data. (A lower number indicates higher priority, so 1 means 1st priority, 2 means 2nd most important, and so on).

* **filter** *(json object)*  Group filter object. Includes inventory filter and classes filters
  * **filter** *(json object)*  Optional parameter.
    Inventory filter data. You can use array values for multiple filter, the logic will be AND. Format is
  * **hostContextInclude** *(array)* Optional parameter.
    Includes only results that concern hosts which have all specified CFEngine contexts (class) set.
  * **hostContextExclude** *(array)*  Optional parameter.
    Excludes results that concern hosts which have specified CFEngine context (class) set. Hosts that have at least one
    of the specified contexts set will be excluded from the results.
  * **hostFilter** *(json object)* Optional parameter.
    * **includes** *(json object)* Optional parameter.
      Object that specifies hosts to be included.
      * **includeAdditionally** *(boolean)* Default: `false`
        Defines if hosts will be added to the results returned by inventory filters or class filters.
      * **entries** *(json object)* Filter entries object. Where the key is an entry type and the value is an array of strings
        Allowed entry types: `hostkey`, `hostname`, `ip`, `mac`, `ip_mask`
    * **excludes** *(json object)* Optional parameter.
      Object that specifies hosts to be excluded.
      * **entries** *(json object)* Filter entries object. Where the key is an entry type and the value is an array of strings
        Allowed entry types: `hostkey`, `hostname`, `ip`, `mac`, `ip_mask`

  ```json
  {
    "filter": {
      "filter": { "Attribute name": {"operator": "value2"} },
      "hostFilter": {
        "includes": {
          "includeAdditionally": false,
          "entries": {
            "ip": ["192.168.56.5"],
            "hostkey": [],
            "hostname": ["ubuntu-bionic"],
            "mac": ["08:00:27:0b:a4:99", "08:00:27:dd:e1:59", "02:9f:d3:59:7e:90"],
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
|-----------------|
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

* **id** *(integer)*
  Unique group identifier.

* **name** *(string)*
  Group name.

* **priority** *(number)*
  Group priority. Groups with a higher priority will take precedence in case of conflicts when merging CMDB data. (A lower number indicates higher priority, so 1 means 1st priority, 2 means 2nd most important, and so on).

* **description** *(string)*
  Group description.

* **filter** *(json object)*  Group filter object. Includes inventory filter and classes filters
  * **filter** *(json object)*  Optional parameter.
    Inventory filter data. You can use array values for multiple filter, the logic will be AND. Format is
  * **hostContextInclude** *(array)* Optional parameter.
    Includes only results that concern hosts which have all specified CFEngine contexts (class) set.
  * **hostContextExclude** *(array)*  Optional parameter.
    Excludes results that concern hosts which have specified CFEngine context (class) set. Hosts that have at least one
    of the specified contexts set will be excluded from the results.
  * **hostFilter** *(json object)* Optional parameter.
    * **includes** *(json object)* Optional parameter.
      Object that specifies hosts to be included.
      * **includeAdditionally** *(boolean)* Default: `false`
        Defines if hosts will be added to the results returned by inventory filters or class filters.
      * **entries** *(json object)* Filter entries object. Where the key is an entry type and the value is an array of strings
        Allowed entry types: `hostkey`, `hostname`, `ip`, `mac`, `ip_mask`
    * **excludes** *(json object)* Optional parameter.
      Object that specifies hosts to be excluded.
      * **entries** *(json object)* Filter entries object. Where the key is an entry type and the value is an array of strings
        Allowed entry types: `hostkey`, `hostname`, `ip`, `mac`, `ip_mask`

```json
{
  "filter": {
    "filter": { "Attribute name": {"operator": "value2"} },
    "hostFilter": {
      "includes": {
        "includeAdditionally": false,
        "entries": {
          "ip": ["192.168.56.5"],
          "hostkey": [],
          "hostname": ["ubuntu-bionic"],
          "mac": ["08:00:27:0b:a4:99", "08:00:27:dd:e1:59", "02:9f:d3:59:7e:90"],
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
|-----------------|
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

* **id** *(integer)*
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
    "filter": { "Architecture": {"matches": "86"} },
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

* **id** *(integer)*
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
        "filter": { "Architecture": {"matches": "86"} },
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

* **id** *(integer)*
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

## List CMDB

You can see a list of stored group-specific configurations

**URI:** https://hub.cfengine.com/api/host-groups/shared/:id/cmdb

**Method:** GET

**Parameters:**

* **id** *(integer)*
  Unique group identifier.
* **fromEpoch** *(integer)*
  Returns configurations with epoch value greater than set in the filter.
  Epoch is the sequence number of the latest CMDB change. In every API list request,
  `cmdb_epoch` will be present in the meta section, which contains the maximum
  epoch value among selected items. Optional parameter.
* **fromTime** *(timestamp)*
  Include changes performed within interval. Format: `YYYY-mm-dd HH:MM:SS` or `YYYY-mm-dd`. Optional parameter.
* **toTime** *(timestamp)*
  Include changes performed within interval. Format: `YYYY-mm-dd HH:MM:SS` or `YYYY-mm-dd`. Optional parameter.
* **skip** *(integer)*
  Number of results to skip for the processed
  query. The Mission Portal uses this for pagination. Optional parameter.
* **limit**  *(integer)*
  Limit the number of results in the query. Optional parameter.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/host-groups/shared/4/cmdb?epochFrom=2
```

**Example response:**

```
HTTP 200 Ok
{
    "data": {
        "5": {
            "classes": {
                "My_class": {},
                "My_class2": {
                    "comment": "comment helps to understand what this class serves for"
                }
            },
            "variables": {
                "HubCMDB:My.hostname": {
                    "value": "host1.cfengine.com",
                    "comment": "comment"
                },
                "Namespace:BundleName.VariableName": {
                    "value": "myvalue"
                }
            }
        }
    },
    "meta": {
        "count": "1",
        "page": 1,
        "timestamp": 1619116399,
        "total": "1",
        "cmdb_epoch": "13"
    }
}
```

## Get group's specific configuration

**URI:** https://hub.cfengine.com/api/host-groups/shared/:id/cmdb/:type/:name/

**Method:** GET

**Parameters:**

* **id** *(integer)*
  Unique group identifier.

* **type** *(string)*
  Configuration type. Allowed value: `variables`, `classes`

* **name** *(string)*
  Configuration name. Classes or variables name.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/host-groups/shared/5/cmdb/variables/HubCMDB:My.hostname/
```

**Example response:**

```
HTTP 200 Ok
{
    "group_id": "5",
    "variables": {
        "default:def.augment_inputs": {
            "tags": [
                "suggestion-004"
            ],
            "value": [],
            "comment": "Add filenames to this list to make the CFEngine agent parse them. Note: Update the bundle sequence to evaluate bundles from these policy files."
        }
    }
}
```

## Get group's configurations

**URI:** https://hub.cfengine.com/api/host-groups/shared/:id/cmdb

**Method:** GET

**Parameters:**

* **id** *(string)*
  Unique group identifier.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/host-groups/shared/5/cmdb
```

**Example response:**

```
HTTP 200 Ok
{
    "group_id": "5",
    "value": {
        "classes": {
            "My_class": {},
            "My_class2": {
                "comment": ""
            }
        },
        "variables": {
            "HubCMDB:My.hostname": {
                "value": "host1.cfengine.com",
                "comment": "My hostname should be set to this"
            },
            "Namespace:BundleName.VariableName": {
                "value": "myvalue"
            }
        }
    }
}
```

## Create configuration

**URI:** https://hub.cfengine.com/api/host-groups/shared/:id/cmdb/:type/:name/

**Method:** POST

**Parameters:**

* **id** *(string)*
  Unique group identifier.

* **type** *(string)*
  Configuration type. Allowed value: `variables`, `classes`

* **name** *(string)*
  Configuration name. Classes or variables name.

**Request body parameters:**

* **value** *(string|array)*
  Variable value, can be array or text. Classes do not support values.

* **comment** *(string)*
  Variables or classes description. Optional parameter.

* **tags** *(array)*
  Variables or classes tags. Optional parameter.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/host-groups/shared/5/cmdb/variables/Namespace:BundleName.Ports/ \
  -H 'content-type: application/json' \
  -d '
  { "value": ["80", "443"],
    "comment":"Openning ports",
    "tags" : ["ports", "tag"]
  }'
```

**Example response:**

```
HTTP 200 Ok
```

## Update configuration

**URI:** https://hub.cfengine.com/api/host-groups/shared/:id/cmdb/:type/:name/

**Method:** PATCH

**Parameters:**

* **id** *(string)*
  Unique group identifier.

* **type** *(string)*
  Configuration type. Allowed value: `variables`, `classes`

* **name** *(string)*
  Configuration name. Classes or variables name.

**Request body parameters:**

* **value** *(string|array)*
  Variable value, can be array or text. Classes do not support values.

* **comment** *(string)*
  Variables or classes description. Optional parameter.

* **tags** *(array)*
  Variables or classes tags. Optional parameter.

* **name** *(string)*
  New name, in case of renaming. Optional parameter.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X PATCH \
  https://hub.cfengine.com/api/host-groups/shared/5/cmdb/variables/Namespace:BundleName.Ports/ \
  -H 'content-type: application/json' \
  -d '
  { "value": ["80", "443"],
    "comment":"Openning ports",
    "tags" : ["ports", "tag"]
  }'
```

**Example response:**

```
HTTP 200 Ok
```

## Delete group's configurations

**URI:** https://hub.cfengine.com/api/host-groups/shared/:id/cmdb

**Method:** DELETE

**Parameters:**

* **id** *(string)*
  Unique group identifier.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X DELETE \
  https://hub.cfengine.com/api/host-groups/shared/5/cmdb
```

**Example response:**

```
HTTP 204 No Content
```

## Delete specific configuration

**URI:** https://hub.cfengine.com/api/host-groups/shared/:id/cmdb/:type/:name/

**Method:** DELETE

**Parameters:**

* **id** *(string)*
  Unique group identifier.

* **type** *(string)*
  Configuration type. Allowed value: `variables`, `classes`

* **name** *(string)*
  Configuration name. Classes or variables name.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X DELETE \
  https://hub.cfengine.com/api/host-groups/shared/5/cmdb/classes/My_class2/
```

**Example response:**

```
HTTP 204 No Content
```
