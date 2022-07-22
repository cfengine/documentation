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
      "ip": "192.168.56.151",
      "lastreport": "1437141907",
      "firstseen": "1437138906"
    },
    {
      "id": "SHA=4a18877bbb7b79f4dde4b03d3ba05bcd66346124cbcd9373590416a90177fcaa",
      "hostname": "hub",
      "ip": "192.168.56.65",
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
      "ip": "192.168.56.151",
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

Remove data about the host from reporting database and stop collecting reports from the host.
This should be done when the host is no longer active.

If host is found and scheduled for deletion, status code `202 ACCEPTED` is returned.
If host is not found, status code `404 NOT FOUND` is returned.
Other response codes are also possible (access denied, server error, etc.).
Only users with the admin role are allowed to delete hosts.

Reporting data associated with the host is immediately purged.
This includes SQL tables like `agentstatus`,  `hosts`, `contexts`, `variables`, etc.
In order to completely delete the host, a deletion job is scheduled by adding the host to the internal table `KeysPendingForDeletion`.
To see what hosts are pending deletion, run the query `SELECT HostKey FROM KeysPendingForDeletion;` against the `cfsettings` database.

After 5-10 minutes (one reporting iteration based on the [hub schedule][cf-hub#hub_schedule]), the main thread of cf-hub will pick up the deletion job.
The hostkey is then removed from:

 * "Last seen" database, which contains network connection info (`/var/cfengine/state/cf_lastseen.lmdb`).
 * Public key directory, containing cryptographic keys exchaned during bootstrap (`/var/cfengine/ppkeys`).
 * The previously mentioned `KeysPendingForDeletion` table.

Note: There is a record of the host retained that includes the time when the host was deleted and this record also prevents further collection from this host identity.

## Hosts list grouped by hard classes

**URI:** https://hub.cfengine.com/api/hosts/by-class

**Method:** GET

**Parameters:**

* **context-include** *(comma delimited string of regular expression strings)*
* **format** *(string)*
    Output format. Default value is `json`. Allowed values: `json`, `yaml`.
* **withInventory** *(boolean)*
    Include inventory data to the API response. Default value is `false`. Allowed values: `true`, `false`  
* **inventoryFile** *(boolean)*
    Make hosts' children values objects which aligns with Ansible inventory that is sourced from a file (so this format is appropriate for caching responses), by default when `inventoryFile` is `false`, the output format aligns with Ansible inventory sourced from a script. Default value is `false`. Allowed values: `true`, `false`
    
**CURL unfiltered request example**

```
curl -k --user admin:admin -X GET https://hub.example.com/api/hosts/by-class
```

**Example response:**    

```
{
    "10_0_2_15": {
            "hosts": [
                "ubuntu-xenial"
            ]
    },
    "127_0_0_1": {
            "hosts": [
                "ubuntu-xenial"
            ]
    },
    "ubuntu_16": {
            "hosts": [
                "ubuntu-xenial"
            ]
    }
}
```

**inventoryFile=true**

```
curl -k --user admin:admin -X GET https://hub.example.com/api/hosts/by-class?inventoryFile=true
```

**Example response:**

```
{
    "10_0_2_15": {
            "hosts": [
                "ubuntu-xenial": {}
            ]
    },
    "127_0_0_1": {
            "hosts": [
                "ubuntu-xenial": {}
            ]
    },
    "ubuntu_16": {
            "hosts": [
                "ubuntu-xenial": {}
            ]
    }
}
```

**CURL request with inventory data example**

```
curl -k --user admin:admin -X GET https://hub.example.com/api/hosts/by-class?withInventory=true
```

**Example response:**

```
{
    "_meta": {
        "hostvars": {
            "ubuntu-xenial": {
                "CFEngine Inventory": {
                    "OS": "Ubuntu 16.04.6 LTS",
                    "OS type": "linux",
                    "Timezone": "UTC"
                }
            }
        }
    },
    "10_0_2_15": {
            "hosts": [
                "ubuntu-xenial"
            ]
    },
    "127_0_0_1": {
            "hosts": [
                "ubuntu-xenial"
            ]
    },
    "ubuntu_16": {
            "hosts": [
                "ubuntu-xenial"
            ]
    }
}
```

## Get deleted hosts list

**URI:** https://hub.cfengine.com/api/hosts/deleted

**Method:** GET

**Parameters:**

* **skip** *(integer)*
  Number of results to skip for the processed query.  
  Optional parameter.
* **limit**  *(integer)*
  Limit the number of results in the query.  
  No limit when parameter is not set. Optional parameter.

**Example request (curl):**
```
curl -k --user admin:admin -X GET https://hub.example.com/api/hosts/deleted
```
**Example response:**

```
HTTP 200 Ok
{
    "data": [
        {
            "hostkey": "SHA=2123f85b38189008ae12be159fb961584dda1249c94efed43fec2c70f233975d",
            "iscallcollected": false,
            "lastreporttimestamp": "2017-02-17 18:00:17+00",
            "firstreporttimestamp": "2017-01-09 17:35:35.427063+00",
            "hostkeycollisions": 0,
            "deleted": "2021-08-19 09:20:02.752463+00",
            "ipaddress": "10.0.2.15"
        }
    ],
    "meta": {
        "total": 1,
        "page": 1,
        "count": 1,
        "timestamp": 1629365174
    }
}
```


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


## Get count of bootstrapped hosts by date range

**URI:** https://hub.cfengine.com/api/host-count

**Method:** POST

**Parameters:**

* **from** *(string)*
    Timestamp marking the start of the interval for which to fetch data. `Emp: 2017-11-28`
* **to** *(string)*
    End of data interval to be fetched. `Emp: 2017-12-28`
* **period** *(string)*
    Group data by period. Allowed values: `day, week, month, year`.

**Example request (curl):**
```
curl -k --user admin:admin -X POST https://hub.cfengine.com/api/host-count  -H 'content-type: application/json'   -d '{"period": "month", "from": "2017-11-28", "to" : "2017-12-06"}'
```
**Example response:**

```
HTTP 200 Ok
{
    "period": "month",
    "data": [
        {
            "date": "Nov 2017",
            "count": 0
        },
        {
            "date": "Dec 2017",
            "count": 15
        }
    ]
}
```

**Output**:

*  **period**
    Period of grouping the data. Allowed values: `day, week, month, year`.
*   **date**
    The date of statistic.
*   **count**
    The bootstrapped hosts to the hub count.

## History

* `inventoryFile=true` parameter added in CFEngine 3.19.0, 3.18.1
