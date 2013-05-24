---
layout: default
title: Checking-Status
categories: [REST API,Checking Status]
published: true
alias: REST-API-Checking-Status.html
tags: [REST API,Checking Status]
---

1 REST API
----------

-   [Basic Properties of the
    API](/manuals/Enterprise-3-0-API#Basic-Properties-of-the-API)
-   [Differences between the CFEngine Nova 2.2 REST API and the CFEngine
    Enterprise 3.0
    API](/manuals/Enterprise-3-0-API#Differences-between-the-CFEngine-Nova-2_002e2-REST-API-and-the-CFEngine-Enterprise-3_002e0-API)
-   [Checking Status](/manuals/Enterprise-3-0-API#Checking-Status)
-   [Managing Settings](/manuals/Enterprise-3-0-API#Managing-Settings)
-   [Managing Users and
    Roles](/manuals/Enterprise-3-0-API#Managing-Users-and-Roles)
-   [Browsing Host
    Information](/manuals/Enterprise-3-0-API#Browsing-Host-Information)
-   [SQL Queries](/manuals/Enterprise-3-0-API#SQL-Queries)
-   [API Reference](/manuals/Enterprise-3-0-API#API-Reference)

The CFEngine Enterprise API allows HTTP clients to interact with the Hub
of a CFEngine Enterprise 3.0 installation. With the Enterprise API, you
can..

-   Check installation status
-   Manage users, groups and settings
-   Browse host (agent) information and policy
-   Issue flexible SQL queries against data collected by the Hub from
    agents
-   Schedule reports for email and later download

The Enterprise API is a REST API, but a central part of interacting with
the API involves using SQL. This is new in 3.0 and was done to provide
users with maximal flexibility for crafting custom reports based on the
wealth of data residing on the Hub.

