---
layout: default
title: CMDB API
aliases:
  - "/api-enterprise-api-ref-cmdb-api.html"
---

The configuration management database (CMDB) API v2 enables you to manage configuration entries for specific hosts.

## Get CMDB for specific host

Get all configuration entries for a specific host.

**URI:** https://hub.cfengine.com/api/cmdb/v2/:hostkey

**Method:** GET

**Parameters:**

- **hostkey** _(string)_
  Unique host identifier.
- **sortColumn** _(string)_
  Column to sort by. Optional parameter.
- **sortDescending** _(boolean)_
  Sort in descending order. Optional parameter.
- **skip** _(integer)_
  Number of results to skip for pagination. Optional parameter.
- **limit** _(integer)_
  Limit the number of results (max 100). Optional parameter.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/cmdb/v2/SHA=f622992fa4525070f47da086041a38733496f03a77880f70b1ce6784c38f79ab?limit=10&skip=0
```

**Example response:**

```json
{
  "data": [
    {
      "id": 1,
      "hostkey": "SHA=f622992fa4525070f47da086041a38733496f03a77880f70b1ce6784c38f79ab",
      "created_at": "2025-09-08 13:53:37.303128",
      "name": "my_class_config",
      "description": "Sample class configuration",
      "tags": ["test_tag", "production"],
      "type": "class",
      "meta": {},
      "entries": [
        {
          "id": 1,
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

## Create configuration entry

Create a new configuration entry for a host.

**URI:** https://hub.cfengine.com/api/cmdb/v2/:hostkey

**Method:** POST

**Parameters:**

- **hostkey** _(string)_
  Unique host identifier.

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

**Example request for class (curl):**

```console
curl -k --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/cmdb/v2/SHA=f622992fa4525070f47da086041a38733496f03a77880f70b1ce6784c38f79ab \
  -H 'content-type: application/json' \
  -d '{
    "type": "class",
    "name": "class1",
    "description": "CMDB class",
    "tags": ["test_tag"],
    "entries": [{
      "item_name": "class1",
      "item_type": "class"
    }]
  }'
```

**Example request for variable (curl):**

```console
curl -k --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/cmdb/v2/SHA=f622992fa4525070f47da086041a38733496f03a77880f70b1ce6784c38f79ab \
  -H 'content-type: application/json' \
  -d '{
    "type": "variable",
    "name": "my_variables",
    "description": "Sample variables configuration",
    "tags": ["variables", "config"],
    "entries": [
      {
        "item_name": "HubCMDB:My.hostname",
        "item_type": "variable",
        "item_value": "host1.cfengine.com"
      }
    ]
  }'
```

**Example response:**

```json
{
  "id": 123
}
```

## Get specific sub-entry

Get a specific sub-entry by type and name.

**URI:** https://hub.cfengine.com/api/cmdb/v2/subentry/:hostkey/:type/:name

**Method:** GET

**Parameters:**

- **hostkey** _(string)_
  Unique host identifier.
- **type** _(string)_
  Sub-entry type (`class` or `variable`).
- **name** _(string)_
  Sub-entry name.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/cmdb/v2/subentry/SHA=f622992fa4525070f47da086041a38733496f03a77880f70b1ce6784c38f79ab/variable/HubCMDB:My.hostname
```

**Example response:**

```json
{
  "id": 1,
  "entry_id": 123,
  "item_name": "HubCMDB:My.hostname",
  "item_value": "host1.cfengine.com"
}
```

## Update configuration entry

Update an existing configuration entry by ID.

**URI:** https://hub.cfengine.com/api/cmdb/v2/entry/:id

**Method:** PUT

**Parameters:**

- **id** _(integer)_
  Configuration entry ID.

**Request body parameters:**

Same as create request: `type`, `name`, `description`, `tags`, `meta`, `entries`

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X PUT \
  https://hub.cfengine.com/api/cmdb/v2/entry/123 \
  -H 'content-type: application/json' \
  -d '{
    "type": "variable",
    "name": "updated_variables",
    "description": "Updated variables configuration",
    "tags": ["variables", "updated"],
    "entries": [
      {
        "item_name": "HubCMDB:My.hostname",
        "item_type": "variable",
        "item_value": "newhost.cfengine.com"
      }
    ]
  }'
```

**Example response:**

```
HTTP 200 Ok
```

## Delete configuration entry

Delete a configuration entry by ID.

**URI:** https://hub.cfengine.com/api/cmdb/v2/entry/:id

**Method:** DELETE

**Parameters:**

- **id** _(integer)_
  Configuration entry ID.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X DELETE \
  https://hub.cfengine.com/api/cmdb/v2/entry/123
```

**Example response:**

```
HTTP 204 No Content
```

## Get policy configuration IDs

Get all policy configuration IDs for a host.

**URI:** https://hub.cfengine.com/api/cmdb/v2/:hostkey/policy-configuration-ids

**Method:** GET

**Parameters:**

- **hostkey** _(string)_
  Unique host identifier.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/cmdb/v2/SHA=f622992fa4525070f47da086041a38733496f03a77880f70b1ce6784c38f79ab/policy-configuration-ids
```

**Example response:**

```json
[
  "policy-123",
  "policy-456"
]
```

## View Host-Specific JSON Configuration

Get the rendered JSON configuration file for a host.

**URI:** https://hub.cfengine.com/api/cmdb/v2/:hostkey/json

**Method:** GET

**Parameters:**

- **hostkey** _(string)_
  Unique host identifier.

**Example request (curl):**

```console
curl -k --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/cmdb/v2/SHA=f622992fa4525070f47da086041a38733496f03a77880f70b1ce6784c38f79ab/json
```

**Example response:**

```json
{
  "classes": {
    "default:cfengine_internal_masterfiles_update": {
      "comment": "Enable automatic VCS policy deployments",
      "tags": []
    },
    "default:services_autorun": {
      "comment": "Automatically evaluate bundles tagged with autorun.",
      "tags": []
    }
  },
  "variables": {
    "variable_name": {
      "comment": "test variable",
      "tags": ["test"],
      "value": "value"
    }
  }
}
```
