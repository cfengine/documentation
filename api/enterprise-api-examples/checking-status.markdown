---
layout: default
title:  Checking Status
published: true
sorting: 20
tags: [examples, enterprise, rest, api, reporting, status]
---

You can get basic info about the API by issuing [/api][Status and Settings REST API#Get server status]. This status
information may also be useful if you contact support, as it gives some basic
diagnostics.

**Request**

    curl -k --user admin:admin --location https://test.cfengine.com/api/

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

