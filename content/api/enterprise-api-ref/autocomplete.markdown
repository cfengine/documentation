---
layout: default
title: Autocomplete API
---

The Autocomplete API provides search functionality for CFEngine classes and variables.

## Search classes

Searches for CFEngine classes by name using case-insensitive pattern matching.

**URI:** https://hub.cfengine.com/api/autocomplete/classes

**Method:** GET

**RBAC permission:** `autocomplete.get.classes` (allowed by default)

**Parameters:**

- **query** _(string)_
  Search pattern for class names. Required. Must be 1-100 characters and containonly letters,
  numbers, dots, colons, or underscores.

**Example request (curl):**

```console
curl --user <username>:<password> \
  https://hub.cfengine.com/api/autocomplete/classes?query=cfe
```

**Example response:**

```
HTTP 200 OK
[
    "cfengine",
    "cfengine_3",
    "cfengine_3_28",
    "cfengine_3_28_0a",
    "cfengine_3_28_0a_0a2e3af8b",
    "cfengine_reporting_hub"
]
```

**Output:**

Returns an array of class names matching the search pattern,
sorted alphabetically.

**Responses:**

| HTTP response code       | Description         |
| ------------------------ | ------------------- |
| 200 OK                   | Successful response |
| 422 Unprocessable Entity | Validation errors   |

**Error response examples:**

Missing required field:

```
HTTP 422 Unprocessable Entity
{
  "success": false,
  "errors": [
    {
      "field": "[query]",
      "message": "This field is missing."
    }
  ]
}
```

## Search variables

Searches for CFEngine variables by name using case-insensitive pattern matching.

**URI:** https://hub.cfengine.com/api/autocomplete/variables

**Method:** GET

**RBAC permission:** `autocomplete.get.variables` (allowed by default)

**Parameters:**

- **query** _(string)_
  Search pattern for variable names. Required. Must be 1-100 characters and contain only letters, numbers, dots, colons, or underscores.

**Example request (curl):**

```console
curl --user <username>:<password> \
  https://hub.cfengine.com/api/autocomplete/variables?query=cf
```

**Example response:**

```
HTTP 200 OK
{
    "default:sys.cfengine_roles": "cfengine_roles",
    "default:sys.cf_version": "cf_version",
    "default:def.mpf_admit_cf_runagent_shell_selected": "mpf_admit_cf_runagent_shell_selected",
    "default:sys.cf_edition": "cf_edition"
}
```

**Output:**

Returns an object where keys are fully qualified variable names (namespace:bundle.variablename)
and values are the variable names, sorted alphabetically by variable name.

**Responses:**

| HTTP response code       | Description         |
| ------------------------ | ------------------- |
| 200 OK                   | Successful response |
| 422 Unprocessable Entity | Validation errors   |

**Error response examples:**

Missing required field:

```
HTTP 422 Unprocessable Entity
{
  "success": false,
  "errors": [
    {
      "field": "[query]",
      "message": "This field is missing."
    }
  ]
}
```

## Search inventory attributes

Searches for inventory attribute names using case-insensitive pattern matching.

**URI:** https://hub.cfengine.com/api/autocomplete/inventory

**Method:** GET

**RBAC permission:** No RBAC restrictions (inventory attributes are publicly available)

**Parameters:**

- **query** _(string)_
  Search pattern for inventory attribute names. Required. Must be 1-100 characters and contain only letters, numbers, dots, colons, or underscores.

**Example request (curl):**

```console
curl --user <username>:<password> \
  https://hub.cfengine.com/api/autocomplete/inventory?query=os
```

**Example response:**

```
HTTP 200 OK
[
    "OS",
    "OS type",
    "OS kernel",
    "OS release"
]
```

**Output:**

Returns an array of inventory attribute names matching the search pattern,
sorted alphabetically.

**Responses:**

| HTTP response code       | Description         |
| ------------------------ | ------------------- |
| 200 OK                   | Successful response |
| 422 Unprocessable Entity | Validation errors   |

**Error response examples:**

Missing required field:

```
HTTP 422 Unprocessable Entity
{
  "success": false,
  "errors": [
    {
      "field": "[query]",
      "message": "This field is missing."
    }
  ]
}
```

## Security considerations

The Autocomplete API bypasses database RBAC restrictions and allows users to see any class or variable name in the system. Inventory attributes are available without any restrictions.
