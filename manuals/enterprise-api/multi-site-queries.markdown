---
layout: default
title:  Multi-Site Queries
categories: [Manuals, Enterprise API, Multi-Site Queries]
published: true
alias: manuals-enterprise-api-multi-site-queries.html
tags: [manuals, enterprise, rest, api, reporting, sql, queries, multi-site]
---

**TODO: introduction to multi-site queries**

**TODO: Simplified diagram?**

### Definition

* Aggregator

A python script `multidb-query.py` that distributes the queries to available 
CFEngine Database Servers and aggregates the result.

* Virtual table interface **TODO: implementation detail?**

Combines all the sqlite3 result files and presents an interface for the aggregator to send the aggregation query.

* Replica detection

The [Enterprise API](manuals-enterprise-api-checking-status.html) returns the 
available replica set to redirect the query.
**TODO: make sure to update API reference accordingly**

* sqlite3 export

A part of reporting engine that converts the result-set into a sqlite3 db file for transfer to the aggregator.
**TODO: if official part of REST API, document there; otherwise, skip as implementation detail**

### Use cases to be covered

1. Simple query (SELECT * FROM Variables;)
2. Joins between multiple tables
3. Count & Aggregation queries
4. Sorting and Grouping

### Interface

* Input: SQL query, CFEngine Enterprise Servers with replica set defined e.g. [[cfdb1,cfdb2,cfdb3], [cfdb4,cfdb5,cfdb6]], username/password
* Output: query result table as JSON (Note: The output is dumped on the terminal as table, JSON conversion yet to be done)
* Error: HOST_NOT_FOUND, QUERY_FAILURE, TIMEOUT, SUCCESS (add more...)

**TODO: proper command line documentation, including options like -i or -d**



### Limitations:

1. Embedded SQL is not supported at the moment
   eg. you will not be able to do: 
     SELECT count(SELECT DISTINCT HostName From Hosts) from Hosts


### Recommendations and best practices:

Always use aliases for operations involving multiple tables eg. instead of 
this:

    SELECT Hosts.HostKey, PromiseLogs.HostKey FROM Hosts INNER JOIN 
        PromiseLogs ON Hosts.HostKey=PromiseLogs.HostKey;

use:

    SELECT Hosts.HostKey AS hkey, PromiseLogs.HostKey AS pkey FROM Hosts INNER 
        JOIN PromiseLogs ON hkey=pkey;

or even better:

    SELECT h.HostKey AS hkey, p.HostKey AS pkey FROM Hosts AS h INNER JOIN 
        PromiseLogs AS p ON hkey=pkey;

Always use aliases for functions

    eg. SELECT count(*) as column_count from Hosts

Use LIMIT with ORDER BY whenever possible

Instead of:

    SELECT Hosts.HostName AS Name FROM Hosts
        LIMIT 10

(This might return data that come from a single CFDB)

Use:

    SELECT Hosts.HostName AS Name FROM Hosts
        ORDER BY Hosts.ReportTimeStampLIMIT 10


### Troubleshooting:

#### Error in status query

Always check the syslog in the corresponding  CFEngine Database Server if the error output at the 
multi-site client is not sufficient. The ip address for the machine where the 
error occurred is prefixed with every error message. There are --inform(-i) 
and --debug(-d) options available that provide detail about the individual 
steps on the operation.

    ERROR:root:[10.100.100.130] Error exporting results to sqlite3 database file
    ERROR:root:Error in status query

Something went wrong while executing the SQL query at the server. Check the syslog in [10.100.100.130]. If you see something like the following, it means that the Enterprise API received the exact same query:

    Error executing query - message: database is locked, sql: "CREATE TABLE results

Same query from multiple requests at the same time is not supported currently. A simple example would be - trying to query the same  CFEngine Database Server in a multi-site query:

    $ python multidb-query.py -u admin -p admin
        -H '[["10.100.100.130"], ["10.100.100.130"]]' -s"http"
        -q"SELECT HostName, Count(1) as HostCount FROM Hosts GROUP BY HostName LIMIT 100".

#### No hubs available to query

    ERROR:root:Error: No hubs available to query, cannot continue

If one of the hubs in the query cannot be contacted, the query cannot continue 
by default. To override this behavior use the `-e, --continue-on-error` 
option.

If you still get this error with `-e`, then there is probably a problem with 
network connectivity.

#### No hubs available to query for a group

    WARNING:root:No hubs available to query for group: [u'10.100.100.10', u'10.100.100.11']

This warning is displayed when run with *-e, --continue-on-error* option.
This means that none of the members in the replica set could be contacted.

#### Invalid response code

This is the HTTP response code received from the server. Currently only 200 
(success) is regarded as valid

#### Connection Error

Connection errors can be caused due to various reasons. A stack trace is 
printed in case of a connection error.

* Use of incorrect URL Scheme name

Multi-Site reporting uses "HTTPS" by default. If you are hosting CFEngine 
Enterprise API under a different URL Scheme name, you would get

    ConnectionError: HTTPSConnectionPool(host='10.100.100.177', port=443): Max retries exceeded with url: /api (Caused by <class 'socket.error'>: [Errno 111] Connection refused)
    INFO 2013-05-13 15:23:15,168 [10.100.100.177] Hub NOT available for report query

You can specify a different scheme name with the option:

    -s URL_SCHEME_NAME, --url-scheme-name URL_SCHEME_NAME
                            Url scheme name. eg. https(default), http


    $ ./multidb-query.py -u"admin" -p"admin"
      -H'[["10.100.100.177"],["10.100.100.179"]]' -q"SELECT * from hosts;"
      -s"http" -i

