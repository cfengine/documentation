layout: default
title:  Browsing Host Information
categories: [Manuals,Enterprise 3.0 API, Browsing Host Information]
published: true
alias: Browsing-Host-Information.html
tags: [Manuals,Enterprise 3.0 API, Browsing Host Information]
---
### 1.6 Browsing Host Information

-   [Example - Listing Hosts With A Given
    Context](/manuals/Enterprise-3-0-API#Example-_002d-Listing-Hosts-With-A-Given-Context)
-   [Example - Looking Up Hosts By
    Hostname](/manuals/Enterprise-3-0-API#Example-_002d-Looking-Up-Hosts-By-Hostname)
-   [Example - Looking Up Hosts By
    IP](/manuals/Enterprise-3-0-API#Example-_002d-Looking-Up-Hosts-By-IP)
-   [Example - Removing Host
    Data](/manuals/Enterprise-3-0-API#Example-_002d-Removing-Host-Data)
-   [Example - Listing Available Vital Signs For A
    Host](/manuals/Enterprise-3-0-API#Example-_002d-Listing-Available-Vital-Signs-For-A-Host)
-   [Example - Retrieving Vital Sign
    Data](/manuals/Enterprise-3-0-API#Example-_002d-Retrieving-Vital-Sign-Data)

A resource */api/host* is added as an alternative interface for browsing
host information. For full flexibility we recommend using SQL reports
via */api/query* for this, however, currently vital signs (data gathered
from cf-monitord) is not part of the SQL reports data model.

* * * * *

Next: [Example - Looking Up Hosts By
Hostname](/manuals/Enterprise-3-0-API#Example-_002d-Looking-Up-Hosts-By-Hostname),
Previous: [Browsing Host
Information](/manuals/Enterprise-3-0-API#Browsing-Host-Information),
Up: [Browsing Host
Information](/manuals/Enterprise-3-0-API#Browsing-Host-Information)

#### 1.6.1 Example: Listing Hosts With A Given Context

**Request**

    curl --user admin:admin http://test.cfengine.com/api/host?context-include=windows.*

**Response**

    {
      "meta": {
        "page": 1,
        "count": 2,
        "total": 2,
        "timestamp": 1350997528
      },
      "data": [
        {
          "id": "1c8fafe478e05eec60fe08d2934415c81a51d2075aac27c9936e19012d625cb8",
          "hostname": "windows2008-2.test.cfengine.com",
          "ip": "172.20.100.43"
        },
        {
          "id": "dddc95486d97e4308f164ddc1fdbbc133825f35254f9cfbd59393a671015ab99",
          "hostname": "windows2003-2.test.cfengine.com",
          "ip": "172.20.100.42"
        }
      ]
    }

* * * * *

Next: [Example - Looking Up Hosts By
IP](/manuals/Enterprise-3-0-API#Example-_002d-Looking-Up-Hosts-By-IP),
Previous: [Example - Listing Hosts With A Given
Context](/manuals/Enterprise-3-0-API#Example-_002d-Listing-Hosts-With-A-Given-Context),
Up: [Browsing Host
Information](/manuals/Enterprise-3-0-API#Browsing-Host-Information)

#### 1.6.2 Example: Looking Up Hosts By Hostname

Contexts are powerful, as you can use them to categorize hosts according
to a rich set of tags. For example, each host is automatically tagged
with a canonicalized version of its hostname and IP-address. So we could
lookup the host with hostname *windows2003-2.test.cfengine.com* as
follows (lines split and indented for presentability).

**Request**

    curl --user admin:admin http://test.cfengine.com/api/host?context-include=
       windows2003_2_stage_cfengine_com

**Response**

    {
      "meta": {
        "page": 1,
        "count": 1,
        "total": 1,
        "timestamp": 1350997528
      },
      "data": [
        {
          "id": "dddc95486d97e4308f164ddc1fdbbc133825f35254f9cfbd59393a671015ab99",
          "hostname": "windows2003-2.test.cfengine.com",
          "ip": "172.20.100.42"
        }
      ]
    }

* * * * *

Next: [Example - Removing Host
Data](/manuals/Enterprise-3-0-API#Example-_002d-Removing-Host-Data),
Previous: [Example - Looking Up Hosts By
Hostname](/manuals/Enterprise-3-0-API#Example-_002d-Looking-Up-Hosts-By-Hostname),
Up: [Browsing Host
Information](/manuals/Enterprise-3-0-API#Browsing-Host-Information)

#### 1.6.3 Example: Looking Up Hosts By IP

Similarly we can lookup the host with hostname
*windows2008-2.test.cfengine.com* by IP as follows (lines split and
indented for presentability).

**Request**

    curl --user admin:admin http://test.cfengine.com/api/host?
       context-include=172_20_100_43

**Response**

    {
      "meta": {
        "page": 1,
        "count": 1,
        "total": 1,
        "timestamp": 1350997528
      },
      "data": [
        {
          "id": "1c8fafe478e05eec60fe08d2934415c81a51d2075aac27c9936e19012d625cb8",
          "hostname": "windows2008-2.stage.cfengine.com",
          "ip": "172.20.100.43"
        }
      ]
    }

* * * * *

Next: [Example - Listing Available Vital Signs For A
Host](/manuals/Enterprise-3-0-API#Example-_002d-Listing-Available-Vital-Signs-For-A-Host),
Previous: [Example - Looking Up Hosts By
IP](/manuals/Enterprise-3-0-API#Example-_002d-Looking-Up-Hosts-By-IP),
Up: [Browsing Host
Information](/manuals/Enterprise-3-0-API#Browsing-Host-Information)

#### 1.6.4 Example: Removing Host Data

If a host has been decommissioned from a Hub, we can explicitly remove
data associated with the host from the Hub, by issuing a DELETE request
(lines split and indented for presentability).

**Request**

    curl --user admin:admin http://test.cfengine.com/api/host/
       1c8fafe478e05eec60fe08d2934415c81a51d2075aac27c9936e19012d625cb8 -X DELETE

**Response**

    204 No Content

* * * * *

Next: [Example - Retrieving Vital Sign
Data](/manuals/Enterprise-3-0-API#Example-_002d-Retrieving-Vital-Sign-Data),
Previous: [Example - Removing Host
Data](/manuals/Enterprise-3-0-API#Example-_002d-Removing-Host-Data),
Up: [Browsing Host
Information](/manuals/Enterprise-3-0-API#Browsing-Host-Information)

#### 1.6.5 Example: Listing Available Vital Signs For A Host

Each host record on the Hub has a set of vital signs collected by
cf-monitord on the agent. We can view the list of vitals signs from as
host as follows (lines split and indented for presentability).

**Request**

    curl --user admin:admin http://test.cfengine.com/api/host/
       4e913e2f5ccf0c572b9573a83c4a992798cee170f5ee3019d489a201bc98a1a/vital

**Response**

    {
      "meta": {
        "page": 1,
        "count": 4,
        "total": 4,
        "timestamp": 1351001799
      },
      "data": [
        {
          "id": "messages",
          "description": "New log entries (messages)",
          "units": "entries",
          "timestamp": 1351001400
        },
        {
          "id": "mem_swap",
          "description": "Total swap size",
          "units": "megabytes",
          "timestamp": 1351001400
        },
        {
          "id": "mem_freeswap",
          "description": "Free swap size",
          "units": "megabytes",
          "timestamp": 1351001400
        },
        {
          "id": "mem_free",
          "description": "Free system memory",
          "units": "megabytes",
          "timestamp": 1351001400
        },
    }

* * * * *

Previous: [Example - Listing Available Vital Signs For A
Host](/manuals/Enterprise-3-0-API#Example-_002d-Listing-Available-Vital-Signs-For-A-Host),
Up: [Browsing Host
Information](/manuals/Enterprise-3-0-API#Browsing-Host-Information)

#### 1.6.6 Example: Retrieving Vital Sign Data

Each vital sign has a collected time series of values for up to one
week. Here we retrieve the time series for the *mem\_free* vital sign at
host *4e913e2f5ccf0c572b9573a83c4a992798cee170f5ee3019d489a201bc98a1a*
for October 23rd 2012 12:20pm to 12:45pm GMT (lines split and indented
for presentability).

**Request**

    curl --user admin:admin http://test.cfengine.com/api/host/
       4e913e2f5ccf0c572b9573a83c4a992798cee170f5ee3019d489a201bc98a1a/
       vital/mem_free?from=1350994800&to=1350996300

**Response**

    "meta": {
        "page": 1,
        "count": 1,
        "total": 1,
        "timestamp": 1351002265
      },
      "data": [
        {
          "id": "mem_free",
          "description": "Free system memory",
          "units": "megabytes",
          "timestamp": 1351001700,
          "values": [
            [
              1350994800,
              36.2969
            ],
            [
              1350995100,
              36.2969
            ],
            [
              1350995400,
              36.2969
            ],
            [
              1350995700,
              36.2969
            ],
            [
              1350996000,
              36.1758
            ],
            [
              1350996300,
              36.2969
            ]
          ]
        }
      ]

* * * * *

Next: [API Reference](/manuals/Enterprise-3-0-API#API-Reference),
Previous: [Browsing Host
Information](/manuals/Enterprise-3-0-API#Browsing-Host-Information),
Up: [REST API](/manuals/Enterprise-3-0-API#REST-API)

