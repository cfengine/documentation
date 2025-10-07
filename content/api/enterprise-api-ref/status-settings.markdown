---
layout: default
title: Status and settings REST API
aliases:
  - "/api-enterprise-api-ref-status-settings.html"
---

REST API for managing settings, checking hub status.

## Get server status

**URI:** https://hub.cfengine.com/api

**Method:** GET

**Example response:**

```
{
  "meta": {
    "page": 1,
    "count": 1,
    "total": 1,
    "timestamp": 1437396760
  },
  "data": [
    {
      "apiName": "CFEngine Enterprise API",
      "apiVersion": "v1",
      "enterpriseVersion": "3.6.4",
      "uiVersion": "ed2766c",
      "coreVersion": "3.6.5",
      "authenticated": "internal",
      "userId": "admin",
      "license": {
        "expires": "2222-12-25 00:00:00+00",
        "owner": "FREE ENTERPRISE - http://cfengine.com/terms for terms",
        "licenseType": "Enterprise Free",
        "granted": 25
      }
    }
  ]
}
```

**Output:**

- **apiName**
  Human-friendly API name.
- **apiVersion**
  API version string.
- **enterpriseVersion**
  Version of the CFEngine Enterprise build.
- **uiVersion**
  The internal build number of the Enterprise UI.
- **coreVersion**
  The version of CFEngine Core (Community) the Enterprise version was built against.
- **authenticated** _("internal", "external")_
  Whether the request was authenticated using the internal users table or an external source.
- **license.expires**
  Time when the license expires.
- **license.owner**
  The name of the license owner.
- **license.granted**
  Host number capacity granted by the license.
- **license.licenseType**
  License description.

**Example usage:** `Checking status`

## Get settings

**URI:** https://hub.cfengine.com/api/settings

**Method:** GET

Check all settings of Mission Portal and REST API.
API call allowed only for administrator.

**Example response:**

```
{
  "meta": {
    "page": 1,
    "count": 1,
    "total": 1,
    "timestamp": 1350992335
  },
  "data": [
    {
       "blueHostHorizon": 2400,
       "enforce2FA": false,
       "hostIdentifier": "default.sys.fqhost",
       "hostsCollisionsThreshold": 3,
       "logLevel": "error",
       "minPasswordLength": 8,
       "passwordComplexity": 3,
       "passwordExpirationAfterResetHours": 48,
       "rbacEnabled": true
    }
  ]
}
```

**Output**:

See [Update settings][Status and settings REST API#Update settings] field section for output descriptions

**Example usage:** `Example: Viewing settings`

## Update settings

**URI:** https://hub.cfengine.com/api/settings

**Method:** POST

Update settings for Mission Portal and API's. API call allowed only for
administrator.

**Fields**:

- **rbacEnabled** _(boolean)_
  Whether RBAC is applied to requests.
- **hostIdentifier** _(string)_
  The identfying string for hosts, such as name or IP.
- **ldapEnabled** _(boolean)_
  Whether external authentication is activated.
- **logLevel** _("emergency", "alert", "critical", "error", "warning", "notice", "info", "debug")_
  Syslog filter specifying the severity level at which messages produced by the API should be emitted to syslog and apache.log. (default: error).
- **blueHostHorizon** _(900)_
  Threshold in minutes that hosts are unreachable before they are considered a health issue.
- **sameHostsNumberOfRuns** _(integer)_
  Number of samples used to identify a duplicate identity. Default value is 3.
- **enforce2FA** _(boolean)_
  Determines if two-factor authentication (2FA) is mandatory for all users.
  If set to `true`, users must enable 2FA; otherwise, they will be locked out within 48 hours after the first login.
  Default value: `false`
- **minPasswordLength** _(integer)_
  Sets the minimum required length for user passwords.
  The value represents the number of characters.
  Default value: `8`
- **passwordComplexity** _(integer)_
  Defines the level of password complexity required.
  The range is from 0 to 4, where zero turns of the password complexity check and four turns on the maximum level.
  Default value: `3`
- **passwordExpirationAfterResetHours** _(integer)_
  Specifies the number of hours after which a password must expire following a reset.
  Default value: `48`

**Example Request Body:**

```
{
  "hostIdentifier": "default.sys.fqhost",
  "rbacEnabled": false,
  "logLevel": "error",
  "ldapEnabled": true,
  "blueHostHorizon": 900,
  "sameHostsNumberOfRuns": 5,
  "minPasswordLength": 12,
  "passwordComplexity": 4,
  "passwordExpirationAfterResetHours": 24,
  "enforce2FA": true
}
```

**Example usage:** `Example: Configuring LDAP`, `Example: Changing the log level`
