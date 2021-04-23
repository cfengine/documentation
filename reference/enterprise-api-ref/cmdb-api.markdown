---
layout: default
title: CMDB API
published: true
tags: [reference, enterprise, API, CMDB, classes, variables]
---

Configuration management database API enables you to manage classes and variables for specific hosts.

## List CMDB 

You can see a list of stored hosts-specific configurations

**URI:** https://hub.cfengine.com/cmdb

**Method:** GET

**Parameters:**
* **fromEpoch** *(integer)*
  Returns configurations with epoch value greater than set in the filter.
  Epoch is the sequence number of the latest CMDB change. In every API list request, you
  might see `most_recent_cmdb_change` property on the meta section, which contains the maximum
  epoch value among selected items. Optional parameter.
* **fromTime** *(timestamp)*
  Include changes performed within interval. Format: `YYYY-mm-dd HH:MM:SS` or `YYYY-mm-dd`
* **toTime** *(timestamp)*
  Include changes performed within interval. Format: `YYYY-mm-dd HH:MM:SS` or `YYYY-mm-dd`
* **skip** *(integer)*
  Number of results to skip for the processed
  query. The Mission Portal uses this for pagination. Optional parameter.
* **limit**  *(integer)*
  Limit the number of results in the query.
* **hostContextInclude** *(array)*
  Includes only results that concern hosts which have all specified CFEngine contexts (class) set. Optional parameter.
* **hostContextExclude** *(array)*
  Excludes results that concern hosts which have specified CFEngine context (class) set. Hosts that have at least one of the specified contexts set will be excluded from the results. Optional parameter.

    
**Example request (curl):**
 
```
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/cmdb?epochFrom=2&hostContextInclude[]=ubuntu \
  -H 'content-type: application/json' 
```

**Example response:**

```
HTTP 200 Ok
{
    "data": {
        "SHA=fdab725e8fb18aa0ad194477be8a2a1338b4b29f6a8597819af89697e432418f": {
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
        "most_recent_cmdb_change": "13"
    }
}
```

## Get configuration by hostkey

**URI:** https://hub.cfengine.com/cmdb/:hostkey

**Method:** GET

**Parameters:**
* **hostkey** *(string)*
  Unique host identifier.

**Example request (curl):**

```
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/cmdb/SHA=f622992fa4525070f47da086041a38733496f03a77880f70b1ce6784c38f79ab 
```

**Example response:**

```
HTTP 200 Ok
{
    "hostkey": "SHA=f622992fa4525070f47da086041a38733496f03a77880f70b1ce6784c38f79ab",
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

## Create new configuration

**URI:** https://hub.cfengine.com/cmdb

**Method:** POST

**Parameters:**
* **hostkey** *(string)*
  Unique host identifier.
* **classes** *(JSON object)*
  The format is a JSON object where the key is class name and value is another JSON object
  with an optional `comment` property.
  Example:
```
{
   "classes":{
      "My_class":{
         
      },
      "My_class2":{
         "comment":"comment body"
      }
   }
}
```
  
* **variables** *(JSON object)*
  The format is a JSON object where the key is variable name and value is another JSON object
  with a required `value` property and an optional `comment` property.
  Example:
```
{
   "variables":{
      "Namespace:BundleName.VariableName":{
         "value":"myvalue"
      },
      "HubCMDB:My.hostname":{
         "value":"host1.cfengine.com",
         "comment":"My hostname should be set to this"
      }
   }
}
```


**Example request (curl):**

```
curl -k --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/cmdb \
  -H 'content-type: application/json' \
  -d '{
   "hostkey":"SHA=f622992fa4525070f47da086041a38733496f03a77880f70b1ce6784c38f79ab",
   "classes":{
      "My_class2":{
         "comment" : ""
      },
      "My_class": {}
   },
   "variables":{
      "Namespace:BundleName.VariableName":{
         "value":"myvalue"
      },
      "HubCMDB:My.hostname":{
         "value":"host1.cfengine.com",
         "comment":"My hostname should be set to this"
      }
   }
}'
```

**Example response:**

```
HTTP 201 Created
```

## Update configuration

**URI:** https://hub.cfengine.com/cmdb/:hostkey

**Method:** PATCH

**Parameters:**
* **hostkey** *(string)*
  Unique host identifier.
* **classes** *(JSON object)*
  The format is a JSON object where the key is class name and value is another JSON object
  with an optional `comment` property.
  Example:
```
{
   "classes":{
      "My_class":{
         
      },
      "My_class2":{
         "comment":"comment body"
      }
   }
}
```

If you need to delete all classes from host you need to set null value:
```
{
    "classes": null
}
```
If your request body misses classes then the previous value will be preserved.

* **variables** *(JSON object)*
  The format is a JSON object where the key is variable name and value is another JSON object
  with a required `value` property and an optional `comment` property.
  Example:
```
{
   "variables":{
      "Namespace:BundleName.VariableName":{
         "value":"myvalue"
      },
      "HubCMDB:My.hostname":{
         "value":"host1.cfengine.com",
         "comment":"My hostname should be set to this"
      }
   }
}
```
If you need to delete all variables from host you need to set null value:
```
{
    "variables": null
}
```
If your request body misses variables then the previous value will be preserved.

**Example request (curl):**

```
curl -k --user <username>:<password> \
  -X PATCH \
  https://hub.cfengine.com/api/cmdb/SHA=f622992fa4525070f47da086041a38733496f03a77880f70b1ce6784c38f79ab \
  -H 'content-type: application/json' \
  -d '{
   "classes":{
      "My_class2":{
         "comment" : ""
      },
      "My_class": {}
   },
   "variables":{
      "Namespace:BundleName.VariableName":{
         "value":"myvalue"
      },
      "HubCMDB:My.hostname":{
         "value":"host1.cfengine.com",
         "comment":"My hostname should be set to this"
      }
   }
}'
```

**Example response:**

```
HTTP 200 Ok
```

## Delete configuration

**URI:** https://hub.cfengine.com/cmdb/:hostkey

**Method:** DELETE

**Parameters:**
* **hostkey** *(string)*
  Unique host identifier.

**Example request (curl):**

```
curl -k --user <username>:<password> \
  -X DELETE \
  https://hub.cfengine.com/api/cmdb/SHA=f622992fa4525070f47da086041a38733496f03a77880f70b1ce6784c38f79ab 
```

**Example response:**

```
HTTP 204 No Content
```