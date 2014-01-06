---
layout: default
title: Enterprise Reporting
categories: [Manuals, Enterprise Reporting]
published: true
sorting: 80
alias: manuals-enterprise-reporting.html
tags: [manuals, enterprise, reporting]
---

The CFEngine Enterprise edition offers a framework for configuration 
management that goes beyond building and deploying systems. Features include 
compliance management, reporting and business integration, and tools for 
handling the necessary complexity.

In a CFEngine Enterprise installation, the CFEngine Server aggregates 
information about the environment in a centralized database. Data is collected 
every 5 minutes from all bootstrapped hosts, and includes information about:

* logs about promises kept, not kept and repaired
* current host contexts and classifications
* variables
* software information
* file changes

This data can be mined using SQL queries, and then be used for inventory 
management, compliance reporting, system diagnostics, capacity planning etc.

Access to the data is provided through the [Enterprise API][Enterprise API] 
and the Mission Portal web front-end.
