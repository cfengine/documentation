---
layout: default
title:  Managing Settings
published: true
sorting: 30
tags: [examples, enterprise, rest, api, reporting, settings, ldap]
---

Settings support two operations, **GET** (view settings) and **POST**
(update settings). When settings are updated, they are sanity checked
individually and as a whole. All or no settings will be updated for a request.

## Example: Viewing settings

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
          "hostIdentifier": "default.sys.fqhost",
          "rbacEnabled": true,
          "ldapEnabled": true,
          "blueHostHorizon": 900,
          "sketchActivationAlertTimeout": 60
        }
      ]
    }

## Example: Configuring LDAP

The setting `ldapEnabled` turns external authentication on or off. LDAP settings
are managed by the LDAP API and not this Settings API.

**Request**

    curl --user admin:admin http://test.cfengine.com/api/settings -X POST -d
    {
      "ldapEnabled": true
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

