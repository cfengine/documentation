---
layout: default
title: Enterprise Reporting database
published: true
sorting: 90
tags: [getting started, installation, faq]
---

# Can I use an existing PostgreSQL installation?

No. Although CFEngine keeps its assumptions about Postgres to a bare minimum,
CFEngine should use a dedicated PostgreSQL database instance to ensure there is
no conflict with an existing installation.

# Do I need experience with PostgreSQL?

PostgreSQL is highly configurable and you should have some in-house expertise to
properly configure your database installation. The defaults are well tuned for
common cases but you may find optimizations depending on your hardware and OS.

# What is the system user for the CFEngine dedicated PostgreSQL database?

The database runs under the `cfpostgres` user.

# What are the requirements for installing CFEngine Enterprise?

## General Information

* [Pre-Installation Checklist][Pre-Installation Checklist]
* [Supported Platforms and Versions][Supported Platforms and Versions]

## Users and Permissions

* CFEngine Enterprise makes an attempt to create the local users `cfapache` and
  `cfpostgres`, as well as group `cfapache` during install.

# How does Enterprise Scale?

See best practices on [scalability][Best Practices#Scalability]

# Is it normal to have many cf-hub processes running?

* Yes, it is expected to have ~ 50 `cf-hub` processes running on a hub.

# What steps should I take after installing CFEngine Enterprise?

There are general steps to be taken outlined in
[Post-Installation Configuration][General Installation#Post-Installation Configuration].

In addition to this, Enterprise uses the local mail relay, and it is assumed
that the server where CFEngine Enterprise is installed on has proper mail setup.
