layout: default
title:  SQL Queries
categories: [Manuals,Enterprise 3.0 API, SQL Queries]
published: true
alias: SQL-Queries.html
tags: [Manuals,Enterprise 3.0 API, SQL Queries]
---
### 1.7 SQL Queries

-   [Synchronous
    Queries](/manuals/Enterprise-3-0-API#Synchronous-Queries)
-   [Asynchronous
    Queries](/manuals/Enterprise-3-0-API#Asynchronous-Queries)
-   [Subscribed Queries](/manuals/Enterprise-3-0-API#Subscribed-Queries)

The standard way of creating reports in CFEngine Enterprise 3.0 is with
SQL queries. See the chapter on SQL queries for an explanation. The API
has a few ways of creating a report.

-   Synchronous query, where we issue a query and wait for the table to
    be sent back with the response.
-   Asynchronous query, where we get a response immediately with an id
    that we can later query to download the report.
-   Subscribed query, where we specify a query to be run on a schedule
    and have the result emailed to someone.

* * * * *

Next: [Asynchronous
Queries](/manuals/Enterprise-3-0-API#Asynchronous-Queries),
Previous: [SQL Queries](/manuals/Enterprise-3-0-API#SQL-Queries),
Up: [SQL Queries](/manuals/Enterprise-3-0-API#SQL-Queries)

#### 1.7.1 Synchronous Queries

Issuing a synchronous query is the most straight forward way of running
an SQL query. We simply issue the query and wait for a result to come
back.

##### 1.7.1.1 Example: Listing Hostname and IP for Ubuntu Hosts

**Request**(lines split and indented for presentability)

    curl -k --user admin:admin https://test.cfengine.com/api/query -X POST -d
    {
      "query": "SELECT Hosts.HostName, Hosts.IPAddress FROM Hosts JOIN Contexts 
         ON Hosts.Hostkey = Contexts.HostKey WHERE Contexts.ContextName = \"ubuntu\""
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
          "query": "SELECT Hosts.HostName, Hosts.IPAddress FROM Hosts JOIN Contexts ON 
              Hosts.Hostkey = Contexts.HostKey WHERE Contexts.ContextName = \"ubuntu\"",
          "header": [
            "HostName",
            "IPAddress"
          ],
          "rowCount": 3,
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
          "cached": false,
          "sortDescending": false
        }
      ]
    }

The **cached** and **sortDescending** fields here mean that the the
result was not retrieved from cache, and that post-processing sorting
was not applied. It is also possible to specify **skip** and **limit**
fields that will be applied to the result set after it is returned by
the SQL engine. These fields are mainly used by the Mission Portal to
paginate quickly on already processed queries.

* * * * *

Next: [Subscribed
Queries](/manuals/Enterprise-3-0-API#Subscribed-Queries),
Previous: [Synchronous
Queries](/manuals/Enterprise-3-0-API#Synchronous-Queries), Up: [SQL
Queries](/manuals/Enterprise-3-0-API#SQL-Queries)

#### 1.7.2 Asynchronous Queries

Because some queries may take some time to compute, it is possible to
fire off a query and check the status of it later. This is useful for
dumping a lot of data into CSV files for example. The sequence consists
of three steps.

1.  Issue the asynchronous query and get a job id
2.  Check status of processing using the id
3.  When the query is completed, get a download link using the id

##### 1.7.2.1 Issuing The Query

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
          "query": "SELECT Hosts.HostName, Hosts.IPAddress FROM Hosts JOIN Contexts ON 
              Hosts.Hostkey = Contexts.HostKey WHERE Contexts.ContextName = \"ubuntu\""
        }
      ]
    ]

##### 1.7.2.2 Checking Status

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

##### 1.7.2.3 Getting The Completed Report

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

* * * * *

Previous: [Asynchronous
Queries](/manuals/Enterprise-3-0-API#Asynchronous-Queries), Up: [SQL
Queries](/manuals/Enterprise-3-0-API#SQL-Queries)

#### 1.7.3 Subscribed Queries

Subscribed queries happen in the context of a user. Any user can create
a query on a schedule and have it email to someone.

##### 1.7.3.1 Example: Creating A Subscribed Query

Here we create a new query to count file changes by name and have the
result sent to us by email. The schedule field is any CFEngine context
expression. The backend polls subscriptions in a loop and checks whether
it's time to generate a report and send it out. In the following
example, user *milton* creates a new subscription to a report which he
names *file-changes-report*, which will be sent out every Monday night.
His boss will get an email with a link to a PDF version of the report.

**Request**(lines split and indented for presentability)

    curl -k --user admin:admin https://test.cfengine.com/api/user/milton/
       subscription/query/file-changes-report -X PUT -d
    {
      "to": "boss@megaco.com",
      "query": "SELECT Name Count(1) FROM FileChanges GROUP BY Name",
      "schedule": "Monday.Hr23.Min59",
      "title": "A very important file changes report"
      "description": "Text that will be included in email"
      "outputTypes": [ "pdf" ]
    }

**Response**

    204 No Content

##### 1.7.3.2 Example: Listing Report Subscriptions

Milton can list all his current subscriptions by issuing the following.

**Request**

    curl -k --user admin:admin https://test.cfengine.com/api/user/milton/subscription/query

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
          "id": "file-changes-report"
          "to": "boss@megaco.com",
          "query": "SELECT Name Count(1) FROM FileChanges GROUP BY Name",
          "title": "A very important file changes report"
          "description": "Text that will be included in email"
          "schedule": "Monday.Hr23.Min59",
          "outputTypes": [ "pdf" ]
        }
    ]

##### 1.7.3.3 Example: Removing A Report Subscription

**Request** (lines split and indented for presentability)

    curl -k --user admin:admin https://test.cfengine.com/api/user/milton/
       subscription/query/file-changes-report -X DELETE

**Response**

    204 No Content

* * * * *

Previous: [SQL Queries](/manuals/Enterprise-3-0-API#SQL-Queries),
Up: [REST API](/manuals/Enterprise-3-0-API#REST-API)

