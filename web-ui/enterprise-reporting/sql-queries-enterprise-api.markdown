---
layout: default
title: SQL Queries Using the Enterprise API
published: true
sorting: 20
tags: [manuals, enterprise, reporting]
---

The CFEngine Enterprise Hub collects information about the
environment in a centralized database. Data is collected every 5
minutes from all bootstrapped hosts. This data can be accessed through
the Enterprise Reporting API.

Through the API, you can run CFEngine Enterprise reports with SQL
queries. The API can create the following report queries:

-   Synchronous query: Issue a query and wait for the table to
    be sent back with the response.
-   Asynchronous query: A query is issued and an immediate response with an ID is sent
    so that you can check the query later to download the report.
-   Subscribed query: Specify a query to be run on a schedule
    and have the result emailed to someone.

### Synchronous Queries ###

Issuing a synchronous query is the most straightforward way of running
an SQL query. We simply issue the query and wait for a result to come
back.

**Request:**

    curl -k --user admin:admin https://test.cfengine.com/api/query -X POST -d
    {
      "query": "SELECT ..."
    }

**Response:**

    {
      "meta": {
        "page": 1,
        "count": 1,
        "total": 1,
        "timestamp": 1351003514
      },
      "data": [
        {
          "query": "SELECT ...",
          "header": [
            "Column 1",
            "Column 2"
          ],
          "rowCount": 3,
          "rows": [
          ]
          "cached": false,
          "sortDescending": false
        }
      ]
    }

## Asynchronous Queries

Because some queries can take some time to compute, you can
fire off a query and check the status of it later. This is useful for
dumping a lot of data into CSV files for example. The sequence consists
of three steps:

1.  Issue the asynchronous query and get a job id.
2.  Check the processing status using the id.
3.  When the query is completed, get a download link using the id.

### Issuing the query

**Request:**

    curl -k --user admin:admin https://test.cfengine.com/api/query/async -X POST -d
    {
      "query": "SELECT Hosts.HostName, Hosts.IPAddress FROM Hosts JOIN Contexts ON Hosts.Hostkey = Contexts.HostKey WHERE Contexts.ContextName = 'ubuntu'"
    }

**Response:**

    {
      "meta": {
        "page": 1,
        "count": 1,
        "total": 1,
        "timestamp": 1351003514
      },
      "data": [
        {
          "id": "32ecb0a73e735477cc9b1ea8641e5552",
          "query": "SELECT ..."
        }
      ]
    ]

### Checking the status

**Request:**

    curl -k --user admin:admin https://test.cfengine.com/api/query/async/:id

**Response:**

    {
      "meta": {
        "page": 1,
        "count": 1,
        "total": 1,
        "timestamp": 1351003514
      },
      "data": [
        {
          "id": "32ecb0a73e735477cc9b1ea8641e5552",
          "percentageComplete": 42,
        ]
    }

### Getting the completed report

This is the same API call as checking the status. Eventually, the
**percentageComplete** field will reach 100 and a link to
the completed report will be available for downloading.

**Request:**

    curl -k --user admin:admin https://test.cfengine.com/api/query/async/:id

**Response:**

    {
      "meta": {
        "page": 1,
        "count": 1,
        "total": 1,
        "timestamp": 1351003514
      },
      "data": [
        {
          "id": "32ecb0a73e735477cc9b1ea8641e5552",
          "percentageComplete": 100,
          "href": "https://test.cfengine.com/api/static/32ecb0a73e735477cc9b1ea8641e5552.csv"
        }
      ]
    }

## Subscribed Queries

Subscribed queries happen in the context of a user. Any user can create
a query on a schedule and have it emailed to someone.

**Request:**

    curl -k --user admin:admin https://test.cfengine.com/api/user/name/
       subscription/query/file-changes-report -X PUT -d
    {
      "to": "email@domain.com",
      "query": "SELECT ...",
      "schedule": "Monday.Hr23.Min59",
      "title": "Report title"
      "description": "Text that will be included in email"
      "outputTypes": [ "pdf" ]
    }

**Response:**

    204 No Content



