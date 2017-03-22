---
layout: default
title: Query REST API
published: true
tags: [reference, enterprise, REST, API, SQL, reporting, URI]
---

In case of a need for full flexibility, Query API allow users to execute SQL queries on CFEngine Database.

Database schema available can be found [here][SQL Schema].

## Execute SQL query

**URI:** https://hub.cfengine.com/api/query

**Method:** POST

Execute user SQL query. Accepts SQL compatible with PostgreSQL database. Query is a subject to Role Base Access Control and will include data for hosts that issuing user have permissions to access. Read-only SQL is allowed.

API performance depend on the query result size, to achieve fastest results consider narrowing result set at much as possible.

**Parameters:**

* **query** *(string)*
    SQL query string.
* **sortColumn** *(string)*
    Column name on which to sort results. Optional parameter.
* **sortDescending** *(boolean)*
    Sorting order. Optional parameter.
* **skip** *(integer)*
    Number of results to skip for the processed
    query. The Mission Portal uses this for pagination. Optional parameter.
* **limit**  *(integer)*
    Limit the number of results in the query.
* **hostContextInclude** *(array)*
    Includes only results that concern hosts which have all specified CFEngine contexts (class) set. Optional parameter.
* **hostContextExclude** *(array)*
    Excludes results that concern hosts which have specified CFEngine context (class) set. Hosts that have at lest one of the specified contexts set will be excluded from the results. Optional parameter.

**Example Request Body:**

```
{
  "query": "select hostname, ipaddress from hosts",
  "limit": 2,
  "hostContextExclude": ["policy_server"]
}
```

**Example response:**

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
          "ab84e58e4287",
          "172.17.16.251"
        ],
        [
          "293b3c9647fb",
          "172.17.16.6"
        ]
      ]
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

**Example usage:**  `Synchronous Example: Listing Hostname and IP for Ubuntu Hosts`

## Schedule SQL query as long running job

**URI:** https://hub.cfengine.com/api/query/async

**Method:** POST

Execute user SQL query as a async job. Result is available as file to download within specified format after job is finished.

Accepts SQL compatible with PostgreSQL database. Query is a subject to Role Base Access Control and will include data for hosts that issuing user have permissions to access. Read-only SQL is allowed.

Returns JOB ID which can be used to check query status and get query results.

API returns entire query result. Make sure that result size is sensible.

**Parameters:**

* **query** *(string)*
    SQL query string.
* **outputType** *(string)*
    Supported types: 'csv' (default). Optional parameter.
* **hostContextInclude** *(array)*
    Includes only results that concern hosts which have all specified CFEngine contexts (class) set. Optional parameter.
* **hostContextExclude** *(array)*
    Excludes results that concern hosts which have specified CFEngine context (class) set. Hosts that have at lest one of the specified contexts set will be excluded from the results. Optional parameter.

**Example Request Body:**

```
{
  "query": "select hostname, ipaddress from hosts",
  "outputType": "csv",
  "hostContextExclude": "policy_server"
}
```

**Example response:**

```
{
  "data": [
    {
      "id": "7b7de87ade18f337d62df26881ff39b1",
      "query": "select hostname, ipaddress from hosts limit 10"
    }
  ],
  "meta": {
    "count": 1,
    "page": 1,
    "timestamp": 1437054235,
    "total": 1
  }
}
```

Value of **ID** field is a unique job identifier that can be used to check job status and retrieve query results.

## Check async query status

**URI:** https://hub.cfengine.com/api/query/async/:id

**Method:** GET

Check the status of async scheduled job. When the query is finished it will return a URI to file available to download as a **href** field in the response.

**Example response:**

```
{
  "data": [
    {
      "href": "https://hub.cfengine.com/api/static/7b7de87ade18f337d62df26881ff39b1.csv",
      "id": "7b7de87ade18f337d62df26881ff39b1",
      "percentageComplete": 100
    }
  ],
  "meta": {
    "count": 1,
    "page": 1,
    "timestamp": 1437054427,
    "total": 1
  }
}
```

## Cancel async query

**URI:** https://hub.cfengine.com/api/query/async/:id

**Method:** DELETE


