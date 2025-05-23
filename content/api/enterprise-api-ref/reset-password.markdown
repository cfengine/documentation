---
layout: default
title: Reset password API
published: true
---

## Request reset password link and token

This call initiates the password reset process by sending a reset password
link and token to the user's registered email address. User can click the link from the email
and set a new password in the Mission Portal or invalidate the request.
Every request has an expiration time equal to 48 hours.

**URI:** https://hub.cfengine.com/api/auth/password/forgot/:username

**Method:** POST

**Example request (curl):**

```console
curl -X POST \
  https://hub.cfengine.com/api/auth/password/forgot/admin
```

**Successful response example:**

```
HTTP 200 Ok

Reset password email successfully sent.
```

**Responses:**

| HTTP response code       | Description                                                   |
|--------------------------|---------------------------------------------------------------|
| 200 OK                   | Check your email for the link to reset your password.         |
| 422 Unprocessable Entity | We are unable to reset the password at this time.             |


## Reset password by token

This call provides possibility to change password by reset password token
from the [Request reset password link and token][Reset password API#Request reset password link and token] endpoint.

**URI:** https://hub.cfengine.com/api/auth/password/reset/:token

**Method:** POST

**Example request (curl):**

```console
curl -X POST \
  --data-raw '{"password": "new password"}' \
  https://hub.cfengine.com/api/auth/password/reset/v1twknmrLWos
```

**Successful response example:**

```
HTTP 200 Ok

Reset password email successfully sent.
```

**Responses:**

| HTTP response code       | Description                                                     |
|--------------------------|-----------------------------------------------------------------|
| 200 OK                   | Password successfully changed.                                  |
| 422 Unprocessable Entity | Password validation error or the request cannot be processed.   |
| 429 Too Many Requests    | We have detected multiple unsuccessful reset password attempts. |


## Invalidate reset password token

This call provides possibility to invalidate reset password token
from the [Request reset password link and token][Reset password API#Request reset password link and token] endpoint.

**URI:** https://hub.cfengine.com/api/auth/password/reset/:token

**Method:** DELETE

**Example request (curl):**

```console
curl -X DELETE  https://hub.cfengine.com/api/auth/password/reset/v1twknmrLWos
```

**Successful response example:**

```
HTTP 202 Accepted

Reset password token successfully invalidated.
```

**Responses:**

| HTTP response code       | Description                                    |
|--------------------------|------------------------------------------------|
| 202 Accepted             | Reset password token successfully invalidated. |
| 422 Unprocessable Entity | Unable to process request.                     |
