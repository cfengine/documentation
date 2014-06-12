---
layout: default
title: Enterprise Scalability
published: true
sorting: 11
---

When running CFEngine Enterprise in a large-scale IT environment, where the number of hosts runs into the thousands, certain issues arise that require different approaches compared with smaller installations.

With CFEngine 3.6.0, significant testing was performed to identify the issues surrounding scalability and to determine best practices in large-scale installations of CFEngine. 

## Moving PostgreSQL to Separate Hard Drive ##

From analysis of an installation of 3700 hosts, it was observed that most of the time required for data processing was spent in Redis waiting for the data to be stored in CFEngine's PostgreSQL database. This is especially visible when I/O utilization gets close to 100%.

When the PostgreSQL database is located on the same hard drive where LMDB is located, one might encounter a serious issue with hard drive serialization access to both the PostgreSQL database and LMDB. This causies hundreds of threads to wait for last seen access, and leads to problems with collecting data form all hosts, and might not collect data from all hosts.

In follow up testing, moving the PostgreSQL database to another physical hard drive greatly improved stability of large-scale installations.

### Using SSD for Hosting the PostgreSQL Database ###

The way data is processed uses a huge number of random IO operations, with small chunks of data. SSD may give the best performance because it is designed for these types of scenarios.

## Setting the splaytime ##

`splaytime` is a value that tells CFEngine hosts what window of time they have to decide when they should communicate with the `policy server`. What this means in practise is that when `splaytime` is set to a value such as 4 that the hosts will not attempt to communicate with the policy server all at the same time during a 4 minute window, which limits the number of concurrent connections at any given moment.












