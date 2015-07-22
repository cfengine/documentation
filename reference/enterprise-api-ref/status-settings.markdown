---
layout: default
title: Status and Settings
published: true
tags: [reference, enterprise, REST, API, reporting, status, URI, ldap, settings]
---

REST API for managing settings, checking hub status.

## Get server status

**URI:** http://192.168.122.1/api

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

**URI:** http://192.168.122.1/api/settings

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
      "ldapPort": 389,
      "ldapPortSSL": 636,
      "hostIdentifier": "default.sys.fqhost",
      "rbacEnabled": true,
      "logLevel": "error",
      "ldapEnabled": true,
      "ldapUsername": "",
      "ldapPassword": "",
      "ldapEncryption": "ssl",
      "ldapLoginAttribute": "uid",
      "ldapHost": "ldap.example.com",
      "ldapBaseDN": "ou=people,dc=example,dc=com",
      "ldapFilter": "(objectClass=inetOrgPerson)",
      "blueHostHorizon": 900,
      "sketchActivationAlertTimeout": 60
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
* **ldapBaseDN** *(string)* 
    LDAP BaseDN to use for external LDAP requests.
* **ldapEncryption** *("plain", "ssl", "tls")* 
    Type of LDAP binding to establish to external LDAP server. (Default: "plain"). 
* **ldapHost** *(string)* 
    Hostname of external LDAP server.
* **ldapLoginAttribute** *(string)* 
    LDAP attribute to use for usernames. (default: "uid").
* **ldapUsername** *(string)* 
    LDAP username.
* **ldapPassword** *(string)* 
    LDAP password.
* **ldapUsersDirectory** *(string)* 
    Attribute and value to qualify the directory in which to look up users, e.g. "ou=people". 
* **ldapPort** *(integer)* 
    Port for external LDAP connections not using SSL. (default 389).
* **ldapPortSSL** *(integer)* 
    Port for external LDAP connections using SSL. (default 636). 
* **logLevel** *("emergency", "alert", "critical", "error", "warning", "notice", "info", "debug")* 
    Syslog filter specifying the severity level at which messages produced by the API should be emitted to syslog and apache.log. (default: error). 
* **sketchActivationAlertTimeout** *(integer)* 
    Global timeout in minutes for sketch activation alerts.

**Example usage:** `Example: Viewing settings`

## Update settings

**URI:** http://192.168.122.1/api/settings

**Method:** POST

Update settings for Mission Portal and API's.
API call allowed only for administrator.

**Fields**:

* **rbacEnabled** *(boolean)* 
    Whether RBAC is applied to requests.
* **hostIdentifier** *(string)* 
    The identfying string for hosts, such as name or IP. 
* **ldapEnabled** *(boolean)* 
    Whether external authentication is activated.
* **ldapBaseDN** *(string)* 
    LDAP BaseDN to use for external LDAP requests.
* **ldapEncryption** *("plain", "ssl", "tls")* 
    Type of LDAP binding to establish to external LDAP server. (Default: "plain"). 
* **ldapHost** *(string)* 
    Hostname of external LDAP server.
* **ldapLoginAttribute** *(string)* 
    LDAP attribute to use for usernames. (default: "uid").
* **ldapUsername** *(string)* 
    LDAP username.
* **ldapPassword** *(string)* 
    LDAP password.
* **ldapUsersDirectory** *(string)* 
    Attribute and value to qualify the directory in which to look up users, e.g. "ou=people". 
* **ldapPort** *(integer)* 
    Port for external LDAP connections not using SSL. (default 389).
* **ldapPortSSL** *(integer)* 
    Port for external LDAP connections using SSL. (default 636). 
* **logLevel** *("emergency", "alert", "critical", "error", "warning", "notice", "info", "debug")* 
    Syslog filter specifying the severity level at which messages produced by the API should be emitted to syslog and apache.log. (default: error). 
* **sketchActivationAlertTimeout** *(integer)* 
    Global timeout in minutes for sketch activation alerts.

**Example Request Body:**

```
{
  "rbacEnabled": false
}
```

**Example usage:** `Example: Configuring LDAP`, `Example: Changing The Log Level`