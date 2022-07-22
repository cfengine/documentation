---
layout: default
title: Inventory API
published: true
tags: [reference, enterprise, API, reporting, URI]
---
Inventory API allows to access inventory reports and attributes dictionary.

## Inventory Reports
   

**URI:** https://hub.cfengine.com/api/inventory

**Method:** POST


**Parameters:**

* **select** *(array)*
    Fields for selecting. Required parameter.

    List of fields name you can obtain through [List of inventory attributes][Inventory API#List of inventory attributes]
    call described below. Extra attributes are `hostkey` for selecting host key
    and `resultCount` for selecting rows count.

* **filter** *(json object)* Optionally filter data. You can use array values for multiple filter, the logic will be AND.  Format is

    ```
    {
      "Attribute name":{
        "operator":["value","value1"],
        "operator2":"value2",
        "operator4":"value2"
      }
    }
    ```

    **Operators:**

    For filtering you can use the operators below:

    |Operator         |
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
    

* **sort** *(string)*
    Field name for sorting with "-" for DESC order. Optional parameter.
* **start** *(integer)*
    Number of results to start from. Optional parameter.
* **limit**  *(integer)*
    Limit the number of results in the query. Default value is 1000, max value is 10000.
* **hostContextExclude** *(array)*
    Includes only results that concern hosts which have all specified CFEngine contexts (class) set. Optional parameter.
* **hostContextInclude** *(array)*
    Excludes results that concern hosts which have specified CFEngine context (class) set. Hosts that have at least one of the specified contexts set will be excluded from the results. Optional parameter.


```
curl -k --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/inventory \
  -H 'content-type: application/json' \
  -d '{
        "sort":"Host name",
        "filter":{
           "Host name":{
              "matches":["value1","value"],
              "not_contain":"value2"
           }
        },
        "select":[
           "Host name",
           "OS type",
           "IPv4 addresses",
           "CFEngine version",
           "Ports listening"
        ],
        "hostContextExclude":[
           "policy_server"
        ]
      }
'
```

**Example Request Body:**


```
{  
   "sort":"Host name",
   "filter":{  
      "Host name":{  
         "matches":"value1",
         "=":"value2"
      }
   },
   "select":[  
      "Host name",
      "OS type",
      "IPv4 addresses",
      "CFEngine version",
      "Ports listening"
   ],
   "hostContextExclude":[  
      "policy_server"
   ]
}
```

**Example response:**


```
{
  "data": [
    {
      "header": [
        {
          "columnName": "Host name",
          "columnType": "STRING"
        },
        {
          "columnName": "OS type",
          "columnType": "STRING"
        },
        {
          "columnName": "IPv4 addresses",
          "columnType": "STRING"
        },
        {
          "columnName": "CFEngine version",
          "columnType": "STRING"
        },
        {
          "columnName": "Ports listening",
          "columnType": "STRING"
        }
      ],
      "queryTimeMs": 30,
      "rowCount": 2,
      "rows": [
        [
          "host1.cfengine.com",
          "linux",
          "128.30.23.33",
          "3.10.0",
          "22, 25, 80, 443, 5308, 9000"
        ],
        [
          "host2.cfengine.com",
          "linux",
          "184.45.1.75",
          "3.10.0",
          null
        ]
      ]
    }
  ],
  "meta": {
    "count": 1,
    "page": 1,
    "timestamp": 1496222472,
    "total": 1
  }
}
```

## List of inventory attributes

**URI:** https://hub.cfengine.com/api/inventory/attributes-dictionary

**Method:** GET

Shows list of all inventory attributes available in the system.

See more details: 
* [Custom Inventory][Custom Inventory]

**CURL request example**
```
curl -k --user admin:admin -X GET https://hub.cfengine.com/api/inventory/attributes-dictionary
```

**Example response:**


```
[
  {
    "id": 2,
    "attribute_name": "BIOS vendor",
    "category": "Hardware",
    "readonly": 1,
    "type": "string",
    "convert_function": null,
    "keyname": "default.cfe_autorun_inventory_dmidecode.dmi[bios-vendor]"
  },
  {
    "id": 3,
    "attribute_name": "BIOS version",
    "category": "Hardware",
    "readonly": 1,
    "type": "string",
    "convert_function": null,
    "keyname": "default.cfe_autorun_inventory_dmidecode.dmi[bios-version]"
  }
]
```

## Edit inventory attribute

**URI:** https://hub.cfengine.com/api/inventory/attributes-dictionary/:id

**Method:** PATCH

Set inventory attribute type (int/string..). This is needed for applying filtering in correct format.
Only `readonly - 0` attribute can be edited

**Parameters:**

* **id** *(integer)*
    Attribute Id
* **category** *(string)*
    Category of attribute
* **type** *(string)*
    Attribute's type. Allowed values: int, real, slist, string
* **convert_function** *(string)*
    Convert Function. 
    Emp.: `cf_clearSlist` - to transform string like `{"1", "2"}` to `1, 2`


**CURL request example**
```
curl -k --user admin:admin -X  PATCH  https://hub.cfengine.com/api/inventory/attributes-dictionary/260  -H 'content-type: application/json'   -d '{
                              "category":"Hardware", 
                              "type": "int"
                             }'
```

**Example Request Body:**

```
{
 "category":"Hardware", 
 "type": "int"
}
```

**Example response:**

```
{
  "id": 1,
  "attribute_name": "Architecture",
  "category": "Hardware",
  "readonly": 0,
  "type": "slist",
  "convert_function": "cf_clearSlist"
}
```
