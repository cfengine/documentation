---
layout: default
title: Import & Export Compliance Report API
published: true
tags: [reference, enterprise, API, import, export, compliance report]
---

This provides users the ability to transfer compliance reports between hubs or create reports from a JSON definition file.

## Export

**URI:** https://hub.example/advancedreports/complianceReport/export?id=:ID

**Method:** GET

**Example request (curl):**

```
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/advancedreports/complianceReport/export?id=20
```

**Example response:**

```
HTTP 200 Ok
{
    "reports": {
        "example-compliance-report": {
            "id": "example-compliance-report",
            "type": "compliance",
            "title": "Example Compliance Report",
            "conditions": [
                "software-updates-available",
                "entire-cfengine-policy"
            ]
        }
    },
    "conditions": {
        "software-updates-available": {
            "id": "software-updates-available",
            "name": "Software updates available",
            "description": "Available software updates to any package.",
            "type": "softwareupdate",
            "condition_for": "failing",
            "rules": {
                "package-name": null,
                "condition": null,
                "architecture": null
            },
            "category": "uncategorized",
            "severity": null,
            "host_filter": null
        },
        "entire-cfengine-policy": {
            "id": "entire-cfengine-policy",
            "name": "Entire CFEngine policy",
            "description": "Promises not kept in the entire policy.",
            "type": "policy",
            "condition_for": "failing",
            "rules": {
                "filter-by": null,
                "value": null,
                "promise-handle": null,
                "promise-status": "NOTKEPT"
            },
            "category": "uncategorized",
            "severity": null,
            "host_filter": null
        }
    }
}
```

    
## Import

**URI:** https://hub.example/advancedreports/complianceReport/import

**Method:** POST

**Parameters:**

* **data** *(json)*
    Reports and conditions data to be imported. Data json object should have two nested objects: `reports` and `condtions`:
    * **reports**
        JSON object where the key is report ID, which will be used to identify if report already exists in the system.
        * **id** *(text)*
            Report ID
        * **type** *(text)*
            Report's type. Should be set to `complince`
        * **title** *(text)*
            Report's title.
        * **conditions** *(array)*
            Conditions list
    * **conditions**
        JSON object where the key is condition ID, which will be used to identify if condition already exists in the system.
        * **id** *(text)*
             Condition ID
        * **name** *(text)*
            Condition name 
        * **description** *(text)*
            Condition description
        * **condition_for** *(text)*
            Condition for `passing` or `failing`. 
        * **type** *(text)*
            Condition type. Possible values: `inventory`, `custom`, `fileChanged`, `policy`, `software`
        * **rules** *(json object)*
            JSON object that define rules. Each type has own set of fields:
            * **inventory**
                * **attribute** *(text)*
                    Inventory attribute
                * **operator** *(text)*
                    Operator. Possible values: `matches`, `not_match`, `contains`, `not_contain`, `regex_matches`, `regex_not_match`, `is_not_reported`, `is_reported`, `<`, `>`, `<=`, `>=`, `=`, `!=`
                * **value** *(text)*
                    Value. This field might be skipped in case of `is_reported` or `is_not_reported` operators
            * **custom**
                * **sql** *(text)*
                    Custom SQL
            * **fileChanged**
                * **file-name** *(text)*
                    File name
                * **condition** *(text)*
                    Condition. Possible values: `matches`, `is`
                * **time-period** *(int)*
                    Changed within the time period (hours).
            * **policy**  
                * **filter-by** *(text)*
                    Filter by: `Bundlename`, `Promisees`, `Promiser`
                * **value** *(text)*
                    Filter value
                * **promise-handle** *(text)*
                    Promise handle
                * **promise-status** *(text)*
                    Promise status: `KEPT`, `NOTKEPT`, `REPAIRED`
            * **software**
                * **package-name** *(text)*
                    Package name
                * **condition** *(text)*
                    Condition: `matches`, `is`
                * **architecture** *(text)*
                    Architecture
        * **category** *(text)*
            Conditions category
        * **severity** *(text)*
            Condition severity. Possible values: `low`, `medium`, `high`
        * **host_filter** *(text)*
            Host filter, should be valid class expression. 


* **overwrite** *(booleans)*
    Set true to overwrite existing reports or conditions that belong to you. Default: false

* **public** *(booleans)*
    Set true to make report publicly accessible. Default: false

**Example request (curl):**

```
curl -k --user <username>:<password> \
-X POST https://hub.cfengine.com/advancedreports/complianceReport/import \
--form 'data={
  "reports": {
    "example-report-1": {
      "id": "example-report-1",
      "type": "compliance",
      "title": "Example report #1",
      "conditions": ["os-is-reported", "supported-ubuntu"]
    }
  },
  "conditions": {
    "os-is-reported": {
      "id": "os-is-reported",
      "name": "Operating system is reported",
      "description": "",
      "condition_for": "passing",
      "type": "inventory",
      "rules": [
        {
          "attribute": "OS",
          "operator": "is_reported"
        }
      ],
      "category": "Operating System",
      "severity": "high",
      "host_filter": "linux"
    },
    "supported-ubuntu": {
      "id": "supported-ubuntu",
      "name": "Ubuntu version is supported",
      "description": "Only Ubuntu 18+ are supported",
      "condition_for": "passing",
      "type": "inventory",
      "rules": [
        {
          "attribute": "OS",
          "operator": "matches",
          "value": "Ubuntu"
        }
      ],
      "category": "Operating System",
      "severity": "high",
      "host_filter": "linux"
    }
  }
}' \
--form 'public=true' \
--form 'overwrite=true'
```

**Example response:**

```
HTTP 200 OK
{
    "processed-conditions": {
        "os-is-reported": 13,
        "supported-ubuntu": 14
    },
    "processed-reports": {
        "example-report-1": 22
    }
}
```

**Output:**

* **processed-conditions**
    List of processed conditions where the key is condition ID from the data JSON and the value is internal
    ID from the database.
* **processed-reports**
    List of processed reports where the key is condition ID from the data JSON and the value is internal
    ID from the database.

## History
* Introduced in CFEngine 3.19.0, 3.18.1
