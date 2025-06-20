---
layout: default
title: Personal groups API
---
The personal groups API enables creating host groups based on host filters (the same ones used in inventory reports).

## Create group

**URI:** https://hub.cfengine.com/api/host-groups/personal/

**Method:** POST

**Parameters:**

* **name** *(string)*
  Group name.

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
      "filter":{
        "Attribute name": {
          "operator":"value2"
        }
      },
      "hostFilter": {
            "includes": {
              "includeAdditionally":  false,
              "entries": {
                  "ip": [
                "192.168.56.5"
              ],
              "hostkey": [],
              "hostname": [
                "ubuntu-bionic"
              ],
              "mac": [
                "08:00:27:0b:a4:99",
                "08:00:27:dd:e1:59",
                "02:9f:d3:59:7e:90"
              ],
              "ip_mask": [
                "10.0.2.16/16"
              ]
              }
            },
            "excludes": {
              "entries":{
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
  https://hub.cfengine.com/api/host-groups/personal/ \
  -H 'content-type: application/json' \
  -d '{
        "name":"AIX hosts with additional SHA=first1 host",
        "description":"Host name",
        "filter":{
            "filter": {
                "Architecture": {
                    "matches": "86"
                }
            },
            "hostFilter": {
              "includes": {
                "includeAdditionally":  false,
                "entries": {
                    "ip": [
                  "192.168.56.5"
                ],
                "hostkey": [],
                "hostname": [
                  "ubuntu-bionic"
                ],
                "mac": [
                  "08:00:27:0b:a4:99",
                  "08:00:27:dd:e1:59",
                  "02:9f:d3:59:7e:90"
                ],
                "ip_mask": [
                  "10.0.2.16/16"
                ]
                }
              },
              "excludes": {
                "entries":{
                "ip": [],
                "hostkey": [],
                "hostname": [],
                "mac": [],
                "ip_mask": []
                   }
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
{"id":"4"}
```

## Update group

**URI:** https://hub.cfengine.com/api/host-groups/personal/:id

**Method:** PATCH

**Parameters:**

* **id** *(integer)*
  Group id.
* **name** *(string)*
  Group name.

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
      "filter":{
          "Attribute name": {
              "operator":"value2"
          }
      },
      "hostFilter": {
          "includes": {
            "includeAdditionally":  false,
            "ip": [
              "192.168.56.5"
            ],
            "hostkey": [],
            "hostname": [
              "ubuntu-bionic"
            ],
            "mac": [
              "08:00:27:0b:a4:99",
              "08:00:27:dd:e1:59",
              "02:9f:d3:59:7e:90"
            ],
            "ip_mask": [
              "10.0.2.16/16"
            ]
          },
          "excludes": {
            "ip": [],
            "hostkey": [],
            "hostname": [],
            "mac": [],
            "ip_mask": []
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
  https://hub.cfengine.com/api/host-groups/personal/5 \
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
{"id":"4"}
```

## Get group

**URI:** https://hub.cfengine.com/api/host-groups/personal/:id

**Method:** GET

**Parameters:**

* **id** *(integer)*
  Group id.

**Example request:**

```
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/host-groups/personal/4 \
  -H 'content-type: application/json'
```

**Example response:**

```json
{
    "id": 4,
    "name": "AIX hosts",
    "description": "Host name",
    "owner": "admin",
    "creation_time": "2023-06-14 10:41:25.601112+00",
    "filter": {
        "filter": {
            "Architecture": {
                "matches": "86"
            }
        },
        "hostContextExclude": "",
        "hostContextInclude": [
            "aix"
        ]
    },
    "type": "personal"
}
```


## Remove group

**URI:** https://hub.cfengine.com/api/host-groups/personal/:id

**Method:** DELETE

**Parameters:**

* **id** *(integer)*
  Group id.

**Example request:**

```
curl -k --user <username>:<password> \
  -X DELETE \
  https://hub.cfengine.com/api/host-groups/personal/4 \
  -H 'content-type: application/json'
```


## Groups list

**URI:** https://hub.cfengine.com/api/host-groups/personal

**Method:** GET

**Example request:**

```
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/host-groups/personal\
  -H 'content-type: application/json'
```

**Example response:**

```json
{
  "data": [
    {
      "id": 1,
      "name": "All hosts",
      "description": "",
      "owner": "admin",
      "creation_time": "2023-05-29 09:55:36.878271+00",
      "filter": []
    },
    {
      "id": 4,
      "name": "AIX hosts",
      "description": "Host name",
      "owner": "admin",
      "creation_time": "2023-06-14 10:41:25.601112+00",
      "filter": {
        "filter": {
          "Architecture": {
            "matches": "86"
          }
        },
        "hostContextExclude": "",
        "hostContextInclude": [
          "aix"
        ]
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


## Share personal group

**URI:** https://hub.cfengine.com/api/host-groups/personal/:id/share

**Method:** POST

**Parameters:**

* **id** *(integer)*
  Group id.

**Example request:**

```
curl -k --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/host-groups/personal/4/share
```

**Example response:**

API returns new ID of the shared group.

```json
{"id":"5"}
```
