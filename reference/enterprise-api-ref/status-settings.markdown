---
layout: default
title: Status and Settings REST API
published: true
tags: [reference, enterprise, REST, API, reporting, status, URI, ldap, settings]
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

* **apiName**
    Human-friendly API name.
* **apiVersion**
    API version string.
* **enterpriseVersion**
    Version of the CFEngine Enterprise build.
* **uiVersion**
    The internal build number of the Enterprise UI.
* **coreVersion**
    The version of CFEngine Core (Community) the Enterprise version was built against.
* **authenticated** *("internal", "external")*
    Whether the request was authenticated using the internal users table or an external source.
* **license.expires**
    Time when the license expires.
* **license.owner**
    The name of the license owner.
* **license.granted**
    Host number capacity granted by the license.
* **license.licenseType**
    License description.

**Example usage:** `Checking Status`

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
      "hostIdentifier": "default.sys.fqhost",
      "rbacEnabled": true,
      "logLevel": "error",
      "ldapEnabled": true,
      "blueHostHorizon": 900,
      "sameHostsNumberOfRuns": 3
    }
  ]
}
```

**Output**:

* **rbacEnabled** *(boolean)*
    Whether RBAC is applied to requests.
* **hostIdentifier** *(string)*
    The identfying string for hosts, such as name or IP.
* **ldapEnabled** *(boolean)*
    Whether external authentication is activated.
* **logLevel** *("emergency", "alert", "critical", "error", "warning", "notice", "info", "debug")*
    Syslog filter specifying the severity level at which messages produced by the API should be emitted to syslog and apache.log. (default: error).
* **sameHostsNumberOfRuns** *(integer)*    
    Number of samples used to identify a duplicate identity. Default value is 3.


**Example usage:** `Example: Viewing settings`

## Update settings

**URI:** https://hub.cfengine.com/api/settings

**Method:** POST

Update settings for Mission Portal and API's. API call allowed only for
administrator.

**Fields**:

* **rbacEnabled** *(boolean)*
    Whether RBAC is applied to requests.
* **hostIdentifier** *(string)*
    The identfying string for hosts, such as name or IP.
* **ldapEnabled** *(boolean)*
    Whether external authentication is activated.
* **logLevel** *("emergency", "alert", "critical", "error", "warning", "notice", "info", "debug")*
    Syslog filter specifying the severity level at which messages produced by the API should be emitted to syslog and apache.log. (default: error).
* **blueHostHorizon** *(900)*
    Threshold in minutes that hosts are unreachable before they are considered a health issue.
* **sameHostsNumberOfRuns** *(integer)*    
    Number of samples used to identify a duplicate identity. Default value is 3.


**Example Request Body:**

```
{
  "hostIdentifier": "default.sys.fqhost",
  "rbacEnabled": false,
  "logLevel": "error",
  "ldapEnabled": true,
  "blueHostHorizon": 900,
  "sameHostsNumberOfRuns": 5
}
```

**Example usage:** `Example: Configuring LDAP`, `Example: Changing The Log Level`
