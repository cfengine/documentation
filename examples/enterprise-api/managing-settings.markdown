---
layout: default
title:  Managing Settings
categories: [Examples, Enterprise API, Managing Settings]
published: true
alias: examples-enterprise-api-managing-settings.html
tags: [examples, enterprise, rest, api, reporting, settings, ldap]
---

Most of the settings configurable in the API relate to LDAP authentication of 
users. Settings support two operations, **GET** (view settings) and **POST** 
(update settings). When settings are updated, they are sanity checked 
individually and as a whole. All or no settings will be updated for a request.

## Viewing settings

**Request**

    curl --user admin:admin http://test.cfengine.com/api/settings

**Response**

    {
      "meta": {
        "page": 1,
        "count": 1,
        "total": 1,
        "timestamp": 1350992335
      },
      "data": [
        {
          "rbacEnabled": true,
          "ldapEnabled": false,
          "ldapActiveDirectoryDomain": "ad.cfengine.com",
          "ldapBaseDN": "DC=ad,DC=cfengine,DC=com",
          "ldapEncryption": "plain",
          "ldapHost": "ldap-server.cfengine.com",
          "ldapLoginAttribute": "sAMAccountName",
          "ldapMode": "activeDirectory",
          "ldapPassword": "password",
          "ldapPort": 389,
          "ldapPortSSL": 636,
          "ldapUsername": "test",
          "ldapUsersDirectory": "CN=Users",
          "blueHostHorizon": 900,
          "logLevel": "error"
        }
      ]
    }

## Example: Configuring LDAP

The setting `ldapEnabled` turns external authentication on or off. When turned 
on, the API will check to see that the other LDAP related settings make sense, 
and attempt to authenticate using the configured credentials. If it is not 
successful in doing this, no settings will be changed. The API will notify you 
with a return code an a message describing the error.

**Request**

    curl --user admin:admin http://test.cfengine.com/api/settings -X POST -d
    {
      "ldapEnabled": true,
      "ldapActiveDirectoryDomain": "ad.cfengine.com",
      "ldapBaseDN": "DC=ad,DC=example,DC=com",
      "ldapEncryption": "ssl",
      "ldapHost": "ldap-server.cfengine.com",
      "ldapLoginAttribute": "sAMAccountName",
      "ldapMode": "standard",
      "ldapPassword": "password",
      "ldapUsername": "test",
      "ldapUsersDirectory": "ou",
    }

**Response**

    204 No Content

## Example: Configuring Active Directory

Active Directory is configured in much the same way as OpenLDAP, but the 
additional field `ldapActiveDirectoryDomain` is required. `ldapMode` is also 
changed from `standard` to `activeDirectory`.

**Request**

    curl --user admin:admin http://test.cfengine.com/api/settings -X POST -d
    {
      "ldapEnabled": true,
      "ldapBaseDN": "DC=example,DC=com",
      "ldapEncryption": "plain",
      "ldapHost": "ad-server.cfengine.com",
      "ldapLoginAttribute": "uid",
      "ldapMode": "activeDirectory",
      "ldapPassword": "password",
      "ldapUsername": "test",
      "ldapUsersDirectory": "CN=Users",
    }

**Response**

    204 No Content


## Example: Changing The Log Level

The API uses standard Unix syslog to log a number of events. Additionally, log 
events are sent to `stderr`, which means they may also end up in your Apache 
log. Log events are filtered based on the log level in settings. Suppose you 
wanted to have greater visibility into the processing done at the backend. The 
standard log level is `error`. Changing it to `info` is done as follows.

**Request**

    curl --user admin:admin http://test.cfengine.com/api/settings -X POST -d
    {
      "logLevel": "info"
    }

**Response**

    204 No Content

