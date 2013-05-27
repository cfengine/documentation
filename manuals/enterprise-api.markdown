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
  against data collected by the Hub from agents
- [Schedule 
  reports](manuals-enterprise-api-sql-queries.html#SubscribedQueries) for 
  email and later download

The Enterprise API is a REST API, but a central part of interacting with the API involves using SQL. With the simplicity of REST and the flexibility of SQL, users can craft custom reports based on the wealth of data residing on the CFEngine Database Server.

