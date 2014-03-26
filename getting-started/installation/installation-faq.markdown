---
layout: default
title: Installation FAQ
categories: [Getting Started, Installation, Installation FAQ]
published: true
sorting: 50
alias: getting-started-installation-installation-faq.html
tags: [getting started, installation, enterprise, faq]
---

* [Enterprise Installation](#enterprise-installation)

### Enterprise Installation ###

#### Can I use an existing PostgreSQL installation? ####

Although CFEngine keeps its assumptions about Postgres to a bare minimum, CFEngine should use a dedicated PostgreSQL database instance to ensure there is no conflict with an existing installation.

#### What is the username that CFEngine uses for accessing the PostgreSQL database?

Starting with CFEngine 3.6.0 the system will use ```cfpostgresql``` as the username for the dedicated CFEngine PostgreSQL database installation. 

#### Do I need experience with PostgreSQL? ####

PostgreSQL is highly configurable, and you should have some in-house expertise to properly configure your database installation. 
