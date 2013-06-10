---
layout: default
title: Enterprise API
categories: [Manuals, Enterprise Reporting, API]
published: true
sorting: 20
alias: manuals-enterprise-api.html
tags: [manuals, enterprise, REST, API, reporting]
---

The CFEngine Enterprise API allows HTTP clients to interact with the CFEngine 
Database Server of a CFEngine Enterprise installation. With the Enterprise 
API, you can:

- [Check installation status][Checking Status]
- [Manage users, roles][Managing Users and Roles] and
  [settings][Managing Settings]
- [Browse host information][Browsing Host Information]
- [Issue flexible SQL queries][SQL Queries] against data collected from hosts 
  by the CFEngine Server
- [Schedule reports][SQL Queries#Subscribed Queries] for email and later 
  download

In CFEngine Enterprise 3.5 and later, [Multi-Site Query][Multi-Site Queries] 
support allows centralized collection of data from multiple CFEngine 
Enterprise installations and sites.

The Enterprise API is a REST API, but a central part of interacting with the 
API involves using SQL. With the simplicity of REST, the flexibility of 
SQL and the scalability through Multi-Site queries, users can craft custom 
reports about systems of arbitrary scale, mining a wealth of data residing 
on globally distributed CFEngine Database Servers.
