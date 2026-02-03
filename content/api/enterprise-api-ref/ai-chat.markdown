---
layout: default
title: AI chat API
---

The AI chat API converts natural language questions into SQL queries for running custom reports.

## Send message to AI chat

Converts a question into a SQL query and explanation. The AI chat uses LLM configured via [AI settings][AI settings API].

**URI:** https://hub.cfengine.com/api/ai/text-to-sql

**Method:** POST

**Prerequisites:**

At least one LLM configuration must be created using the [AI settings API][AI settings API#Create AI setting].

**Parameters:**

- **question** _(string)_
  The question to ask. Required.
- **history** _(array)_
  Optional conversation history for context. Array of previous question/answer pairs to maintain conversation context.

**Example request (curl):**

```console
curl --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/ai/text-to-sql \
  -H 'Content-Type: application/json' \
  -d '{
    "question": "Hosts that have SSH port open"
  }'
```

**Example request with conversation history:**

```console
curl --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/ai/text-to-sql \
  -H 'Content-Type: application/json' \
  -d '{
    "question": "What about their uptime?",
    "history": [
      {
        "question": "Hosts that have SSH port open",
        "sql": "SELECT h.hostname, i.values ->> '\''OS'\'' AS os, h.ipaddress, i.values ->> '\''Ports listening'\'' AS open_ports FROM hosts h JOIN inventory_new i ON h.hostkey = i.hostkey WHERE COALESCE(i.values ->> '\''Ports listening'\'', '\''　'\'') ~ '\''(,\\s|^)22(,|$)'\''"
      }
    ]
  }'
```

**Example response:**

```
HTTP 200 OK
{
  "explanation": "This query lists hosts with SSH port open, including their hostname, OS, IP address, open ports, and uptime in minutes.",
  "sql": "SELECT h.hostname, i.values ->> 'OS' AS os, h.ipaddress, i.values ->> 'Ports listening' AS open_ports, i.values ->> 'Uptime minutes' AS uptime_minutes FROM hosts h JOIN inventory_new i ON h.hostkey = i.hostkey WHERE COALESCE(i.values ->> 'Ports listening', '\u3000') ~ '(,\\s|^)22(,|$)'",
  "meta": {
    "provider": "openai",
    "model": "gpt-4.1"
  }
}
```

**Output:**

- **explanation**
  Explanation of what the SQL query does and what data it retrieves.
- **sql**
  The generated SQL query that can be executed against the CFEngine reporting database.
- **meta**
  Metadata about the LLM used to generate the response.
  - **provider** - The LLM provider used (e.g., `openai`, `anthropic`, `ollama`).
  - **model** - The specific model used (e.g., `gpt-4`, `claude-3-opus`).

**Responses:**

| HTTP response code       | Description                                  |
| ------------------------ | -------------------------------------------- |
| 200 OK                   | Successful response with SQL query           |
| 400 Bad Request          | Invalid request data or LLM processing error |
| 422 Unprocessable Entity | No LLM configuration found                   |

**Error response examples:**

Missing LLM configuration:

```
HTTP 422 Unprocessable Entity
Add an LLM configuration before using the chat.
```

Invalid request:

```
HTTP 400 Bad Request
{
  "success": false,
  "errors": [
    {
      "field": "[question]",
      "message": "This value should be of type string."
    }
  ]
}
```

## Security considerations

The AI chat does not execute SQL queries automatically - it only generates them. You must execute the queries separately through the [Query API][Query REST API#Execute SQL query].
The AI does not have access to any of your data unless it is sent to the chat by a user.
