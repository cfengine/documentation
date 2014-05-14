---
layout: default
title: FAQ
published: true
sorting: 5
tags: [getting started, installation, enterprise, faq]
---

* [Enterprise Installation](#enterprise-installation)
* [Enterprise Scalability](#enterprise-scalability)

### Enterprise Installation ###

#### Can I use an existing PostgreSQL installation? ####

Although CFEngine keeps its assumptions about Postgres to a bare minimum, CFEngine should use a dedicated PostgreSQL database instance to ensure there is no conflict with an existing installation.

#### What is the system user for the CFEngine dedicated PostgreSQL database?

Starting with CFEngine 3.6.0 there will be a system user called ```cfpostgres``` for running the dedicated CFEngine PostgreSQL database installation. 

#### Do I need experience with PostgreSQL? ####

PostgreSQL is highly configurable, and you should have some in-house expertise to properly configure your database installation. 

### Enterprise Scalability ###
