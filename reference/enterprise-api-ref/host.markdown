---
layout: default
title: Host REST API
published: true
tags: [reference, enterprise, REST, API, reporting, host, monitoring]
---

Host API allows to access host specific information.

## List hosts

**URI:** https://hub.cfengine.com/api/host

**Method:** GET

**Parameters:**

* **context-include** *(comma delimited string of regular expression
    strings)*
    Includes hosts having context matching the expression.
* **context-exclude** *(comma delimited string of regular expression
    strings)*
    Excludes hosts having context matching the expression.
* **page** *(integer)*
    Number of the page with results. By default 1.
* **count** *(integer)*
    Size of the page. By default 50 results.

**Example response:**

```
{
  "meta": {
    "page": 1,
    "count": 2,
    "total": 2,
    "timestamp": 1437142156
  },
  "data": [
    {
      "id": "SHA=27b88b8a92f1b10b1839ac5b26d022c98d48629bd761c4324d1f1fb0f04f17ba",
      "hostname": "host001",
      "ip": "192.168.33.151",
      "lastreport": "1437141907",
      "firstseen": "1437138906"
    },
    {
      "id": "SHA=4a18877bbb7b79f4dde4b03d3ba05bcd66346124cbcd9373590416a90177fcaa",
      "hostname": "hub",
      "ip": "192.168.33.65",
      "lastreport": "1437141907",
      "firstseen": "1437138666"
    }
  ]
}
```

**Output:**

* **id**
    Unique host identifier.
* **hostname**
    Host name. Can be reconfigured globally to represent variable set in the policy using **hostIdentifier** [setting][Status and Settings REST API#Update settings].
* **ip**
    IP address of the host. If host have multiple network interfaces, IP belongs to the interface that is used to communicate with policy server.
* **lastreport**
    Time of receiving last report from the client, successfully. Represented as UNIX TIMESTAMP.
* **firstseen**
    Time of receiving the first status report from the client. It is equivalent to the time when the client have been bootstrapped to the server for the first time. Represented as UNIX TIMESTAMP.

**Example usage:** `Example: Listing Hosts With A Given Context`, `Example: Looking Up Hosts By Hostname`, `Example: Looking Up Hosts By IP`

## Host Details

**URI:** https://hub.cfengine.com/api/host/:host-id

**Method:** GET

**Example response:**

```
{
  "meta": {
    "page": 1,
    "count": 1,
    "total": 1,
    "timestamp": 1437144171
  },
  "data": [
    {
      "id": "SHA=27b88b8a92f1b10b1839ac5b26d022c98d48629bd",
      "hostname": "host001",
      "ip": "192.168.33.151",
      "lastreport": "1437144007",
      "firstseen": "1437138906"
    }
  ]
}
```

**Output:**

* **id**
    Unique host identifier.
* **hostname**
    Host name. Can be reconfigured globally to represent variable set in the policy using **hostIdentifier** [setting][Status and Settings REST API#Update settings].
* **ip**
    IP address of the host. If host have multiple network interfaces, IP belongs to the interface that is used to communicate with policy server.
* **lastreport**
    Time of receiving last report from the client, successfully. Represented as UNIX TIMESTAMP.
* **firstseen**
    Time of receiving the first status report from the client. It is equivalent to the time when the client have been bootstrapped to the server for the first time. Represented as UNIX TIMESTAMP.

## Remove host from the hub

**URI:** https://hub.cfengine.com/api/host/:host-id

**Method:** DELETE

Remove data about the host from reporting database and stop collecting reports from the host. API call schedules a job for purging authentication keys exchanged during bootstrap which prevents host from being collected in the future. Key purging usually take an effect within 5-10 minutes.

Deleted host need to be re-bootstrapped if it was deleted by accident.

## List monitoring attributes for host

**URI:** https://hub.cfengine.com/api/host/:host-id/vital

**Method:** GET

List all available vital attributes monitored by CFEngine on the client.

Note: Collecting monitoring data by default is disabled.

**Example response:**

```
{
  "meta": {
    "page": 1,
    "count": 24,
    "total": 24,
    "timestamp": 1437144887
  },
  "data": [
    {
      "id": "mem_free",
      "timestamp": 1437144300,
      "description": "Free system memory",
      "units": "megabytes"
    },
    {
      "id": "mem_total",
      "timestamp": 1437144300,
      "description": "Total system memory",
      "units": "megabytes"
    },
    {
      "id": "loadavg",
      "timestamp": 1437144300,
      "description": "Kernel load average utilization",
      "units": "jobs"
    },
    {
      "id": "diskfree",
      "timestamp": 1437144300,
      "description": "Free disk on / partition",
      "units": "percent"
    }
  ]
}
```

**Output:**

* **id**
    Unique vital identifier.
* **timestamp**
    Last measurement time. Represented as UNIX TIMESTAMP.
* **description**
    Vital short description.
* **units**
    Units for the samples.

**Example usage:** `Example: Listing Available Vital Signs For A Host`

## Get samples from vital

**URI:** https://hub.cfengine.com/api/host/:host-id/vital/:vital-id

**Method:** GET

**Parameters:**

* **from** *(integer)*
    Timestamp marking the start of the interval for which to fetch data. Data is only available going back one week.
* **to** *(integer)*
    End of data interval to be fetched.

**Example response:**

```
{
  "meta": {
    "page": 1,
    "count": 1,
    "total": 1,
    "timestamp": 1437146605
  },
  "data": [
    {
      "id": "mem_free",
      "description": "Free system memory",
      "units": "megabytes",
      "timestamp": 1437146100,
      "values": [
        [
          1437140700,
          1229.8600
        ],
        [
          1437141000,
          1216.4500
        ],
        [
          1437141300,
          1218.3800
        ]
      ]
    }
  ]
}
```

**Output**:

*  **id**
    ID of vital sign.
*   **description**
    Description of vital sign.
*   **units**
    Measurement unit of vital sign.
*   **timestamp**
    Timestamp of the last received data point.
*   **values**
    Vital sign data. *(array of [ t, y ], where t is the sample timestamp)*

**Example usage:** `Example: Retrieving Vital Sign Data`

