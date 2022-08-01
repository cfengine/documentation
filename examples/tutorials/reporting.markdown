---
layout: default
title: Reporting
published: true
sorting: 80
tags: [overviews, reports, reporting]
---

No promises made in CFEngine imply automatic aggregation of data to a central location. In
CFEngine Enterprise (our commercial version), an optimized aggregation of standardized
reports is provided, but the ultimate decision to aggregate must be yours.

Monitoring and reporting capabilities in CFEngine depend on your installation:

### Enterprise Edition Reporting

The CFEngine Enterprise edition offers a framework for configuration
management that goes beyond building and deploying systems. Features include
compliance management, reporting and business integration, and tools for
handling the necessary complexity.

In a CFEngine Enterprise installation, the CFEngine Server aggregates
information about the environment in a centralized database. By default data is collected
every 5 minutes from all bootstrapped hosts and includes information about:

* logs about promises kept, not kept and repaired
* current host contexts and classifications
* variables
* software information
* file changes

This data can be mined using SQL queries and then used for inventory
management, compliance reporting, system diagnostics, and capacity planning.

Access to the data is provided through:

* The [Mission Portal console][Reporting UI]
* The [Enterprise Report API][API].

### Command-Line Reporting

Community Edition

Basic output to file or logs can be customized on a per-promise basis.
Users can design their own log and report formats, but data processing and extraction from
CFEngine's embedded databases must be scripted by the user.

**Note:**

If you have regular reporting needs, we recommend using our commercially-supported version
of CFEngine, Enterprise. It will save considerable time and resources in
programming, and you will have access to the latest developments through the software
subscription.
