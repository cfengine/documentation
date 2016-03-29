---
layout: default
title:  SQL Query Examples
published: true
tags: [examples, enterprise, rest, api, reporting, sql, queries]
---

### Synchronous Example: Listing Hostname and IP for Ubuntu Hosts

**Request:**

```bash
    curl -k --user admin:admin https://test.cfengine.com/api/query -X POST -d '{ "query": "SELECT Hosts.HostName, Hosts.IPAddress FROM Hosts"}'
```

**Response:**

```
{
  "data": [
    {
      "header": [
        {
          "columnName": "hostname",
          "columnType": "STRING"
        },
        {
          "columnName": "ipaddress",
          "columnType": "STRING"
        }
      ],
      "query": "select hostname, ipaddress from hosts",
      "queryTimeMs": 152,
      "rowCount": 1001,
      "rows": [
        [
          "ubuntu10-2.stage.cfengine.com",
          "172.20.100.1"
        ],
        [
          "ubuntu10-3.stage.cfengine.com",
          "172.20.100.2"
        ],
        [
          "ubuntu10-4.stage.cfengine.com",
          "172.20.100.3"
        ]
      ],
    }
  ],
  "meta": {
    "count": 1,
    "page": 1,
    "timestamp": 1437051092,
    "total": 1
  }
}
```

### Subscribed Query Example: Creating A Subscribed Query

Here we create a new query to count file changes by name and have the result
sent to us by email. The schedule field is any CFEngine context expression.
The backend polls subscriptions in a loop and checks whether it's time to
generate a report and send it out. In the following example, user `milton`
creates a new subscription to a report which he names `file-changes-report`,
which will be sent out every Monday night. His boss will get an email with a
link to a PDF version of the report.

**Request:**

```bash
    curl -k --user admin:admin https://test.cfengine.com/api/user/milton/ subscription/query/file-changes-report -X PUT -d '{"to": "boss@megaco.com", "query": "SELECT FileName, Count(*) FROM FileChangesLog GROUP BY FileName", "schedule": "Monday.Hr23.Min59", "title": "A very important file changes report""description": "Text that will be included in email""outputTypes": [ "pdf" ] }'
```

**Response:**

```
    204 No Content
```

### Subscribed Query Example: Listing Report Subscriptions

Milton can list all his current subscriptions by issuing the following.

**Request:**

```bash
    curl -k --user admin:admin https://test.cfengine.com/api/user/milton/subscription/query
```

**Response:**

```
{
  "meta": {
    "page": 1,
    "count": 1,
    "total": 1,
    "timestamp": 1351003514
  },
  "data": [
    {
      "id": "file-changes-report",
      "to": "boss@megaco.com",
      "query": "SELECT FileName, Count(*) FROM FileChangesLog GROUP BY FileName",
      "title": "A very important file changes report",
      "description": "Text that will be included in email",
      "schedule": "Monday.Hr23.Min59",
      "outputTypes": [
        "pdf"
      ]
    }
  ]
}
```

### Subscribed Query Example: Removing A Report Subscription

**Request:**

```bash
    curl -k --user admin:admin https://test.cfengine.com/api/user/milton/subscription/query/file-changes-report -X DELETE
```

**Response:**

```
    204 No Content
```