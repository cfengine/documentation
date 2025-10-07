---
layout: default
title: Import & export compliance report API
aliases:
  - "/api-enterprise-api-ref-export-import-compliance-report-api.html"
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

- **data** _(json)_
  Reports and conditions data to be imported. Data json object should have two nested objects: `reports` and `condtions`:
  - **reports**
    JSON object where the key is report ID, which will be used to identify if report already exists in the system.
    - **id** _(text)_
      Report ID
    - **type** _(text)_
      Report's type. Should be set to `complince`
    - **title** _(text)_
      Report's title.
    - **conditions** _(array)_
      Conditions list
  - **conditions**
    JSON object where the key is condition ID, which will be used to identify if condition already exists in the system.
    - **id** _(text)_
      Condition ID
    - **name** _(text)_
      Condition name
    - **description** _(text)_
      Condition description
    - **condition_for** _(text)_
      Condition for `passing` or `failing`.
    - **type** _(text)_
      Condition type. Possible values: `inventory`, `custom`, `fileChanged`, `policy`, `software`
    - **rules** _(json object)_
      JSON object that define rules. Each type has own set of fields:
      - **inventory**
        - **attribute** _(text)_
          Inventory attribute
        - **operator** _(text)_
          Operator. Possible values: `matches`, `not_match`, `contains`, `not_contain`, `regex_matches`, `regex_not_match`, `is_not_reported`, `is_reported`, `<`, `>`, `<=`, `>=`, `=`, `!=`
        - **value** _(text)_
          Value. This field might be skipped in case of `is_reported` or `is_not_reported` operators
      - **custom**
        - **sql** _(text)_
          Custom SQL
      - **fileChanged**
        - **file-name** _(text)_
          File name
        - **condition** _(text)_
          Condition. Possible values: `matches`, `is`
        - **time-period** _(int)_
          Changed within the time period (hours).
      - **policy**
        - **filter-by** _(text)_
          Filter by: `Bundlename`, `Promisees`, `Promiser`
        - **value** _(text)_
          Filter value
        - **promise-handle** _(text)_
          Promise handle
        - **promise-status** _(text)_
          Promise status: `KEPT`, `NOTKEPT`, `REPAIRED`
      - **software**
        - **package-name** _(text)_
          Package name
        - **condition** _(text)_
          Condition: `matches`, `is`
        - **architecture** _(text)_
          Architecture
    - **category** _(text)_
      Conditions category
    - **severity** _(text)_
      Condition severity. Possible values: `low`, `medium`, `high`
    - **host_filter** _(text)_
      Host filter, should be valid class expression.

- **overwrite** _(booleans)_
  Set true to overwrite existing reports or conditions that belong to you. Default: false

- **public** _(booleans)_
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

- **processed-conditions**
  List of processed conditions where the key is condition ID from the data JSON and the value is internal
  ID from the database.
- **processed-reports**
  List of processed reports where the key is condition ID from the data JSON and the value is internal
  ID from the database.

## History

- Introduced in CFEngine 3.19.0, 3.18.1
