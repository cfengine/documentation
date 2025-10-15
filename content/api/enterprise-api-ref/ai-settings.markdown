---
layout: default
title: AI settings API
---

The AI settings API allows you to configure and manage LLM configurations for the [AI chat][AI chat API].

## List AI settings

**URI:** https://hub.cfengine.com/api/ai-settings

**Method:** GET

List all configured LLM settings.

**Example request (curl):**

```console
curl --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/ai-settings
```

**Example response:**

```
HTTP 200 OK
[
  {
    "id": 1,
    "provider": "openai",
    "model": "gpt-4",
    "token": "token is set",
    "base_url": null,
    "name": "OpenAI GPT-4",
    "description": "Production OpenAI configuration",
    "meta": {},
    "created_at": "2025-01-15 10:30:00",
    "updated_at": "2025-01-15 10:30:00"
  }
]
```

**Output:**

- **id** _(number)_
  Unique configuration ID.
- **provider** _(string)_
  LLM provider type. Required. Allowed values: `openai`, `gemini`, `mistral`, `ollama`, `anthropic`, `openai_like`.
- **model** _(string)_
  Model name to use. Required. Maximum 255 characters.
- **token** _(string)_
  API token for authentication. Required for all providers except `ollama`. Maximum 255 characters.
  Note: in the output it returns "token is set" to mask the actual token value for security purposes.
- **base_url** _(string)_
  Custom base URL for API endpoint. Required for `ollama` and `openai_like` providers. Must be a valid URL, maximum 500 characters.
- **name** _(string)_
  Name for this configuration. Optional. Maximum 255 characters.
- **description** _(string)_
  Description of the configuration. Optional. Maximum 4012 characters.
- **meta** _(object)_
  Additional metadata as key-value pairs. Optional. Values must be scalar types (string, integer, float, boolean, or null).
- **created_at** _(string)_
  Timestamp when the configuration was created.
- **updated_at** _(string)_
  Timestamp when the configuration was last updated.

## Get AI setting

**URI:** https://hub.cfengine.com/api/ai-settings/:id

**Method:** GET

Get a specific LLM configuration by ID.

**Parameters:**

- **id** _(integer)_
  Configuration ID. Required.

**Example request (curl):**

```console
curl --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/ai-settings/1
```

**Example response:**

```
HTTP 200 OK
{
  "id": 1,
  "provider": "openai",
  "model": "gpt-4",
  "token": "token is set"
  "base_url": null,
  "name": "OpenAI GPT-4",
  "description": "Production OpenAI configuration",
  "meta": {},
  "created_at": "2025-01-15 10:30:00",
  "updated_at": "2025-01-15 10:30:00"
}
```

**Responses:**

| HTTP response code | Description             |
| ------------------ | ----------------------- |
| 200 OK             | Successful response     |
| 404 Not found      | Configuration not found |

## Create AI setting

**URI:** https://hub.cfengine.com/api/ai-settings

**Method:** POST

Create a new LLM configuration.

**Parameters:**

- **provider** _(string)_
  LLM provider type. Required. Allowed values: `openai`, `gemini`, `mistral`, `ollama`, `anthropic`, `openai_like`.
- **model** _(string)_
  Model name to use. Required. Maximum 255 characters.
- **token** _(string)_
  API token for authentication. Required for all providers except `ollama`. Maximum 255 characters.
- **base_url** _(string)_
  Custom base URL for API endpoint. Required for `ollama` and `openai_like` providers. Must be a valid URL, maximum 500 characters.
- **name** _(string)_
  Name for this configuration. Optional. Maximum 255 characters.
- **description** _(string)_
  Description of the configuration. Optional. Maximum 4012 characters.
- **meta** _(object)_
  Additional metadata as key-value pairs. Optional. Values must be scalar types (string, integer, float, boolean, or null).

**Example request (curl):**

```console
curl --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/ai-settings \
  -H 'Content-Type: application/json' \
  -d '{
    "provider": "openai",
    "model": "gpt-4",
    "token": "sk-proj-xxxxxxxxxxxxx",
    "name": "OpenAI GPT-4",
    "description": "Production OpenAI configuration"
  }'
```

**Example with Ollama (no token required):**

```console
curl --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/ai-settings \
  -H 'Content-Type: application/json' \
  -d '{
    "provider": "ollama",
    "model": "llama2",
    "base_url": "http://localhost:11434",
    "name": "Local Ollama",
    "description": "Local development LLM"
  }'
```

**Example response:**

```
HTTP 201 Created
{
  "id": 3
}
```

**Responses:**

| HTTP response code | Description                               |
| ------------------ | ----------------------------------------- |
| 201 Created        | Configuration successfully created        |
| 400 Bad Request    | Invalid request data or validation errors |

**Validation errors response example:**

```
HTTP 400 Bad Request
{
  "success": false,
  "errors": [
    {
      "field": "[token]",
      "message": "API Token is required for all providers except ollama"
    }
  ]
}
```

## Update AI setting

**URI:** https://hub.cfengine.com/api/ai-settings/:id

**Method:** PATCH

Update an existing LLM configuration.

**Parameters:**

- **id** _(integer)_
  Configuration ID. Required (in URL path).
- **provider** _(string)_
  LLM provider type. Required. Allowed values: `openai`, `gemini`, `mistral`, `ollama`, `anthropic`, `openai_like`.
- **model** _(string)_
  Model name to use. Required. Must be 1-255 characters.
- **token** _(string)_
  API token for authentication. Required for all providers except `ollama`. Maximum 255 characters.
- **base_url** _(string)_
  Custom base URL for API endpoint. Optional. Must be a valid URL, maximum 500 characters.
- **name** _(string)_
  Human-readable name for this configuration. Optional. Must be 1-255 characters.
- **description** _(string)_
  Description of the configuration. Optional. Maximum 4012 characters.
- **meta** _(object)_
  Additional metadata as key-value pairs. Optional. Values must be scalar types (string, integer, float, boolean, or null).

**Example request (curl):**

```console
curl --user <username>:<password> \
  -X PATCH \
  https://hub.cfengine.com/api/ai-settings/1 \
  -H 'Content-Type: application/json' \
  -d '{
    "provider": "openai",
    "model": "gpt-4-turbo",
    "token": "sk-proj-xxxxxxxxxxxxx",
    "name": "OpenAI GPT-4 Turbo",
    "description": "Updated to use GPT-4 Turbo model"
  }'
```

**Example response:**

```
HTTP 202 Accepted
```

**Responses:**

| HTTP response code | Description                               |
| ------------------ | ----------------------------------------- |
| 202 Accepted       | Configuration successfully updated        |
| 400 Bad Request    | Invalid request data or validation errors |
| 404 Not found      | Configuration not found                   |

## Delete AI setting

**URI:** https://hub.cfengine.com/api/ai-settings/:id

**Method:** DELETE

Delete an LLM configuration.

**Parameters:**

- **id** _(integer)_
  Configuration ID. Required.

**Example request (curl):**

```console
curl --user <username>:<password> \
  -X DELETE \
  https://hub.cfengine.com/api/ai-settings/1
```

**Example response:**

```
HTTP 202 Accepted
```

**Responses:**

| HTTP response code | Description                        |
| ------------------ | ---------------------------------- |
| 202 Accepted       | Configuration successfully deleted |
| 404 Not found      | Configuration not found            |
