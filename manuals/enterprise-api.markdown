---
layout: default
title: Enterprise API
categories: [Manuals, Enterprise API]
published: true
alias: manuals-enterprise-api.html
tags: [manuals, enterprise, REST, API, reporting]
---

The CFEngine Enterprise API allows HTTP clients to interact with the CFEngine 
Database Server of a CFEngine Enterprise installation. With the Enterprise 
API, you can:

- [Check installation status](manuals-enterprise-api-checking-status.html)
- [Manage users, groups and
  settings](manuals-enterprise-api-managing-users-and-roles.html)
- [Browse host information and
  policy](manuals-enterprise-api-browsing-host-information.html)
- [Issue flexible SQL queries](manuals-enterprise-api-sql-queries.html) 
  against data collected from hosts by the CFEngine Server
- [Schedule 
  reports](manuals-enterprise-api-sql-queries.html#SubscribedQueries) for 
  email and later download

In CFEngine Enterprise 3.5 and later, [Multi-Site
Query](manuals-enterprise-api-multi-site-queries.html) support allows 
centralized collection of data from multiple CFEngine Enterprise installations
and sites.

The Enterprise API is a REST API, but a central part of interacting with the 
API involves using SQL. With the simplicity of REST, the flexibility of 
SQL and the scalability through Multi-Site queries, users can craft custom 
reports about systems of arbitrary scale, mining a wealth of data residing 
on the CFEngine Database Server.
