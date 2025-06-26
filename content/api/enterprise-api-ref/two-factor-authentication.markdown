---
layout: default
title: Two-factor authentication API
---
The Two-factor authentication API enables users to add an extra layer of security to their accounts
by requiring a TOTP (time-based one-time password) in addition to their primary credentials.

Once two-factor authentication is enabled, requests to obtain an OAuth token, change a password, or
disable two-factor authentication must include an additional header: `Cf-2fa-Token: <code>`.
Basic authentication also requires this header each time it is used.

Currently, only TOTP (Time-based One-Time Password) two-factor authentication
is supported, providing users with a time-sensitive code for enhanced security.

## Start two-factor authentication configuration

First, you need to request two-factor authentication secrets to complete the configuration.
The secret token should be added to a third-party authentication app such as Google Authenticator or Authy.
A 6-digit code should then be obtained from the application to complete the action.

**URI:** https://hub.cfengine.com/api/2fa/totp/configure

**Method:** GET

**Example request (curl):**

```console
curl --user <username>:<password> \
  -X GET \
  https://hub.cfengine.com/api/2fa/totp/configure
```

**Successful response example:**

```
HTTP 200 Ok
{
    "secret": "SYSZJJVQUIOG5ITA6HPH5PZWLZ3VUP52",
    "2faUrl": "otpauth://totp/Mission%20Portal:admin?secret=SYSZJJVQUIOG5ITA6HPH5PZWLZ3VUP52&issuer=Mission%20Portal&algorithm=SHA1&digits=6&period=30",
    "algorithm": "sha1",
    "digits": 6,
    "period": 30,
    "issuer": "Mission Portal",
    "holder": "admin"
}
```

**Output:**

* **secret**
  The secret key used to generate the one-time password (OTP)
* **2faUrl**
  The URL that can be converted into QR code and scanned with an authenticator app to set up two-factor authentication
* **algorithm**
  The cryptographic algorithm used to generate the OTP
* **digits**
  The number of digits in the generated OTP code
* **period**
  The time period in seconds for which the OTP code is valid
* **issuer**
  The name of the service that is providing the two-factor authentication
* **holder**
  The username for whom the two-factor authentication is being configured

**Responses:**

| HTTP response code        | Description                            |
|---------------------------|----------------------------------------|
| 200 OK                    | 2FA configuration successfully created |
| 500 Internal server error | Internal server error                  |



## Complete two-factor authentication configuration

**URI:** https://hub.cfengine.com/api/2fa/totp/configure

**Method:** POST

**Parameters:**

* **code** *(string)*
  6-digit code from the authentication application

**Example request (curl):**

```console
curl --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/2fa/totp/configure \
  --data-raw '{"code": "000000"}'
```

**Successful response example:**

```
HTTP 200 Ok
2FA successfully enabled for this user.
```

**Responses:**

| HTTP response code        | Description                 |
|---------------------------|-----------------------------|
| 200 OK                    | 2FA successfully configured |
| 400 Bad request           | 2FA verification failed.    |
| 500 Internal server error | Internal server error       |


## Disable two-factor authentication for the current user

**URI:** https://hub.cfengine.com/api/2fa/totp/disable

**Method:** POST

**Headers:**

* **Cf-2FA-Token** *(string)*
  6-digit code from the authentication application

**Example request (curl):**

```console
curl --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/2fa/totp/disable \
  --header 'Cf-2FA-Token: 537987'
```

**Successful response example:**

```
HTTP 200 Ok
2FA successfully disabled for this user.
```

**Responses:**

| HTTP response code        | Description                            |
|---------------------------|----------------------------------------|
| 200 OK                    | 2FA successfully disabled              |
| 401 Unauthorized          | Invalid two-factor authentication code |
| 409 Conflict              | 2FA is not enabled for this user       |
| 500 Internal server error | Internal server error                  |

## Disable two-factor authentication for other users

In case if a regular user loses access to the authentication application, specific users (admin role by default)
with the `Disable 2FA for any user` RBAC role (alias `2fa.any-user.disable`) will be able to
disable two-factor authentication for that user.

**URI:** https://hub.cfengine.com/api/2fa/totp/disable/user/:username

**Method:** POST

**Example request (curl):**

```console
curl --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/2fa/totp/disable/user/giorgio
```

**Successful response example:**

```
HTTP 200 Ok
2FA successfully disabled for `giorgio` user.
```

**Responses:**

| HTTP response code        | Description                            |
|---------------------------|----------------------------------------|
| 200 OK                    | 2FA successfully disabled              |
| 401 Unauthorized          | Invalid two-factor authentication code |
| 409 Conflict              | 2FA is not enabled for this user       |
| 500 Internal server error | Internal server error                  |



## Verify two-factor authentication code

This API endpoint verifies the authentication code. If OAuth authentication is used and the code is valid,
your authorization token will be flagged as verified for 5 minutes. During this 5-minute period after successful
verification, you will not need to provide the authorization code from the authentication application.

**URI:** https://hub.cfengine.com/api/2fa/totp/verify

**Method:** POST

**Parameters:**

* **code** *(string)*
  6-digit code from the authentication application

**Example request (curl):**

```console
curl --user <username>:<password> \
  -X POST \
  https://hub.cfengine.com/api/2fa/totp/veify \
  --data-raw '{"code": "000000"}'
```

**Successful response example:**

```
HTTP 200 Ok
2FA successfully verified.
```

**Responses:**

| HTTP response code        | Description                      |
|---------------------------|----------------------------------|
| 200 OK                    | 2FA successfully verified        |
| 409 Conflict              | 2FA is not enabled for this user |
| 500 Internal server error | Internal server error            |


## Check if verification is needed

This API endpoint checks if 2FA verification is needed. Only needed for OAuth authentication method
as for the Basic authentication is needed every time.

**URI:** https://hub.cfengine.com/api/2fa/verification-needed

**Method:** GET


**Example request (curl):**

```console
curl -X GET \
  https://hub.cfengine.com/api/2fa/verification-needed \
  --header 'Authorization: Bearer 627135e5a0b142cfdc738c38ad0c0067bc0960e5'
```

**Successful response example:**

```
HTTP 200 Ok
{
    "result": true
}
```

**Responses:**

| HTTP response code        | Description                      |
|---------------------------|----------------------------------|
| 200 OK                    | 2FA successfully checked         |
| 409 Conflict              | 2FA is not enabled for this user |
| 500 Internal server error | Internal server error            |
