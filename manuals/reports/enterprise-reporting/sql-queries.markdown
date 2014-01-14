---
layout: default
title:  SQL Queries
categories: [Manuals, Reports, Enterprise Reports API, SQL Queries]
published: true
sorting: 30
alias: manuals-enterprise-reporting-sql-queries.html
tags: [manuals, enterprise, rest, api, reporting, sql, queries]
---

Through the API, you can can create reports in CFEngine Enterprise with SQL 
queries. The API can creating the following report queries:

-   Synchronous query, where we issue a query and wait for the table to
    be sent back with the response.
-   Asynchronous query, where we get a response immediately with an id
    that we can later query to download the report.
-   Subscribed query, where we specify a query to be run on a schedule
    and have the result emailed to someone.

## Synchronous Queries

Issuing a synchronous query is the most straight forward way of running
an SQL query. We simply issue the query and wait for a result to come
back.

**Request**(lines split and indented for presentability)

    curl -k --user admin:admin https://test.cfengine.com/api/query -X POST -d
    {
      "query": "SELECT ..."
    }

**Response**

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

Because some queries may take some time to compute, it is possible to
fire off a query and check the status of it later. This is useful for
dumping a lot of data into CSV files for example. The sequence consists
of three steps.

1.  Issue the asynchronous query and get a job id
2.  Check status of processing using the id
3.  When the query is completed, get a download link using the id

### Issuing The Query

**Request**

    curl -k --user admin:admin https://test.cfengine.com/api/query/async -X POST -d
    {
      "query": "SELECT Hosts.HostName, Hosts.IPAddress FROM Hosts JOIN Contexts ON Hosts.Hostkey = Contexts.HostKey WHERE Contexts.ContextName = \"ubuntu\""
    }

**Response**(lines split and indented for presentability)

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

### Checking Status

**Request**

    curl -k --user admin:admin https://test.cfengine.com/api/query/async/:id

**Response**

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

### Getting The Completed Report

This is the same API call as checking the status. Eventually, the
**percentageComplete** field will reach 100 and there will be a link to
the completed report available for downloading.

**Request**

    curl -k --user admin:admin https://test.cfengine.com/api/query/async/:id

**Response**

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
a query on a schedule and have it email to someone.

**Request** (lines split and indented for presentability)

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

**Response**

    204 No Content

