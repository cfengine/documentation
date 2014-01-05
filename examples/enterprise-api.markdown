---
layout: default
title:  Enterprise API
categories: [Examples, Enterprise API]
published: true
alias: examples-enterprise-api.html
tags: [examples, enterprise, rest, api, reporting]
---
The CFEngine Enterprise API allows HTTP clients to interact with the Policy server (hub) 
of a CFEngine Enterprise installation. With the Enterprise API, you can do the following:

* Check installation status

* Manage users, groups, and settings

* Browse host (agent) information and policy

* Issue flexible SQL queries against data collected by the Policy server from hosts

* Schedule reports for email and later download

The Enterprise API is a REST API, but a central part of interacting with the API involves 
using SQL. This provides users with maximum flexibility for 
crafting custom reports based on the wealth of data residing on the Policy server.