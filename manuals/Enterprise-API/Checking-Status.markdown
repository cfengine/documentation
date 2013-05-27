layout: default
title:  Checking Status
categories: [Manuals,Enterprise 3.0 API, Checking Status]
published: true
alias: Checking-Status.html
tags: [Manuals,Enterprise 3.0 API, Checking Status]
---
### 1.3 Checking Status

You can get basic info about the API by issuing *GET /api*. This status
information may also be useful if you contact support, as it gives some
basic diagnostics.

**Request**

    curl -k --user admin:admin https://test.cfengine.com/api/

**Response**

    {
      "meta": {
        "page": 1,
        "count": 1,
        "total": 1,
        "timestamp": 1351154889
      },
      "data": [
        {
          "apiName": "CFEngine Enterprise API",
          "apiVersion": "v1",
          "enterpriseVersion": "3.0.0a1.81c0d4c",
          "coreVersion": "3.5.0a1.f3649b2",
          "databaseHostname": "127.0.0.1",
          "databasePort": 27017,
          "authenticated": "internal",
          "license": {
            "expires": 1391036400,
            "installTime": 1329578143,
            "owner": "Stage Environment",
            "granted": 20,
            "licenseUsage": {
              "lastMeasured": 1351122120,
              "samples": 1905,
              "minObservedLevel": 7,
              "maxObservedLevel": 30,
              "meanUsage": 21.9689,
              "meanCumulativeUtilization": 109.8446,
              "usedToday": 7
            }
          }
        }
      ]
    }

* * * * *

Next: [Managing Users and
Roles](/manuals/Enterprise-3-0-API#Managing-Users-and-Roles),
Previous: [Checking
Status](/manuals/Enterprise-3-0-API#Checking-Status), Up: [REST
API](/manuals/Enterprise-3-0-API#REST-API)

