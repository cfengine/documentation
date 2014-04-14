---
layout: default
title: Enterprise API Overview
published: true
sorting: 2 
tags: [overviews, enterprise, REST, API, reporting]
---

The CFEngine Enterprise API allows HTTP clients to interact with the Policy server (hub) 
of a CFEngine Enterprise installation. 

![Enterprise API Overview](enterprise-api-architecture-overview.png)

In CFEngine Enterprise 3.5 and later, [Multi-Site Query][Multi-Site Queries] 
support allows centralized collection of data from multiple CFEngine 
Enterprise installations and sites.

The Enterprise API is a REST API, but a central part of interacting with the 
API involves using SQL. With the simplicity of REST, the flexibility of 
SQL and the scalability through Multi-Site queries, users can craft custom 
reports about systems of arbitrary scale, mining a wealth of data residing 
on globally distributed CFEngine Database Servers.

Refer to the [Enterprise API Reference][Enterprise API Reference] section for the SQL schema 
and URI resources. 

See also the [Enterprise API Examples][Enterprise API Examples]:

* [Check installation status][Checking Status]
* [Manage users, roles][Managing Users and Roles]
* [Managing Settings][Managing Settings]
* [Browse host information][Browsing Host Information]
* [Issue flexible SQL queries][SQL Queries] against data collected from hosts by the CFEngine Server
* [Schedule reports][SQL Queries#Subscribed Queries] for email and later download
