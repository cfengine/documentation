---
layout: default
title: Fist time setup API
published: true
---

The First time setup API enables creation of the initial administrator user.
This API is only accessible when the system hasn't been previously configured.
Once setup is complete, this API becomes permanently inaccessible.

## Generate setup code

The setup code is generated during hub installation.
If you need a new setup code, execute this command on your hub:

```console
sudo cf-hub --new-setup-code
```

**Note:** The setup code will expire after 1 hour.
When you request a new setup code, it invalidates the previous one.

## Check setup status

First, check if the system has already been set up.
This endpoint returns the current setup status of the system.

**URI:** https://hub.example.com/api/setup/status

**Method:** GET

**Example request (curl):**

```console
curl -X GET \
  https://hub.example.com/api/setup/status
```

**Successful response example:**

```
HTTP 200 Ok
{
    "is_setup_complete": false
}
```

**Output:**

* **is_setup_complete**
  Boolean value indicating whether the system has been set up (true) or not (false)

**Responses:**

| HTTP response code        | Description                   |
|---------------------------|-------------------------------|
| 200 OK                    | Setup status check successful |
| 500 Internal server error | Internal server error         |

## Validate setup code

Before completing setup, you must validate a setup code.
This endpoint returns a session ID required for the setup complete API request.

**URI:** https://hub.example.com/api/setup/code/validate

**Method:** POST

**Parameters:**

* **code** *(string)*
  The setup code provided during system initialization

**Example request (curl):**

```console
curl -X POST \
  https://hub.example.com/api/setup/code/validate \
  --data-raw '{"code": "YOUR_SETUP_CODE"}'
```

**Successful response example:**

```
HTTP 200 Ok
{
    "session_id": "abcdef123456789....",
    "valid": true
}
```

**Output:**

* **session_id**
  The session ID to be used in the setup complete API request
* **valid**
  Boolean value indicating whether the provided code is valid

**Responses:**

| HTTP response code        | Description                   |
|---------------------------|-------------------------------|
| 200 OK                    | Code validation successful    |
| 400 Bad request           | Invalid or missing code       |
| 500 Internal server error | Internal server error         |

## Complete setup

This endpoint finalizes the setup process by creating the first administrator user.
It requires a valid session ID obtained from the code validation step.

**URI:** https://hub.example.com/api/setup/complete

**Method:** POST

**Headers:**

* **Cf-Setup-Session-Id** *(string)*
  Session ID obtained from the code validation step

**Parameters:**

* **username** *(string)*
  Alphanumeric username for the administrator account
* **password** *(string)*
  Password for the administrator account
* **email** *(string)*
  Email address for the administrator account

**Example request (curl):**

```console
curl -X POST \
  https://hub.example.com/api/setup/complete \
  --header 'Cf-Setup-Session-Id: abcdef123456789' \
  --data-raw '{
    "username": "admin",
    "password": "SecurePassword123",
    "email": "admin@example.loc"
  }'
```

**Successful response example:**

```
HTTP 201 Created
```

**Responses:**

| HTTP response code        | Description                                       |
|---------------------------|---------------------------------------------------|
| 201 Created               | Setup successfully completed                      |
| 406 Not Acceptable        | Invalid session ID                                |
| 400 Bad request           | Missing or invalid parameters                     |
| 500 Internal server error | Internal server error                             |
