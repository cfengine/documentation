---
layout: default
title: Managing-Users-and-Roles
categories: [REST API,Managing Users and Roles]
published: true
alias: REST-API-Managing-Users-and-Roles.html
tags: [REST API,Managing Users and Roles]
---

### 1.2 Differences between the CFEngine Nova 2.2 REST API and the CFEngine Enterprise 3.0 API

-   [Read vs.
    Read/Write](/manuals/Enterprise-3-0-API#Read-vs_002e-Read_002fWrite)
-   [Built-in Reports vs. Reporting
    Engine](/manuals/Enterprise-3-0-API#Built_002din-Reports-vs_002e-Reporting-Engine)
-   [Content-Type](/manuals/Enterprise-3-0-API#Content_002dType)
-   [New Users](/manuals/Enterprise-3-0-API#New-Users)
-   [Base Path](/manuals/Enterprise-3-0-API#Base-Path)
-   [Still available](/manuals/Enterprise-3-0-API#Still-available)
-   [Mission Portal](/manuals/Enterprise-3-0-API#Mission-Portal)

* * * * *

Next:[Built-in Reports vs. Reporting
Engine](/manuals/Enterprise-3-0-API#Built_002din-Reports-vs_002e-Reporting-Engine),
Previous:[Differences between the CFEngine Nova 2.2 REST API and the
CFEngine Enterprise 3.0
API](/manuals/Enterprise-3-0-API#Differences-between-the-CFEngine-Nova-2_002e2-REST-API-and-the-CFEngine-Enterprise-3_002e0-API),
Up:[Differences between the CFEngine Nova 2.2 REST API and the CFEngine
Enterprise 3.0
API](/manuals/Enterprise-3-0-API#Differences-between-the-CFEngine-Nova-2_002e2-REST-API-and-the-CFEngine-Enterprise-3_002e0-API)

#### 1.2.1 Read vs. Read/Write

The 2.2 API was read-only and users, roles and settings was managed by
the Mission Portal. By contrast, the 3.0 API is read/write and
completely standalone from the Mission Portal. In the CFEngine
Enterprise 3.0, users, roles and settings belong in the API, and the
Mission Portal uses this to determine access to data. Additionally, some
other resources support PUT, POST and DELETE, but most data collected
from agents are read-only.

* * * * *

Next:[Content-Type](/manuals/Enterprise-3-0-API#Content_002dType),
Previous:[Read vs.
Read/Write](/manuals/Enterprise-3-0-API#Read-vs_002e-Read_002fWrite),
Up:[Differences between the CFEngine Nova 2.2 REST API and the CFEngine
Enterprise 3.0
API](/manuals/Enterprise-3-0-API#Differences-between-the-CFEngine-Nova-2_002e2-REST-API-and-the-CFEngine-Enterprise-3_002e0-API)

#### 1.2.2 Built-in Reports vs. Reporting Engine

The 2.2 API provided an almost one-to-one correspondence between the
reports in the Mission Portal and the API. One of the big changes in
CFEngine Enterprise 3.0 is the advent of SQL reports. This is provided
to the Mission Portal through the API, and you can use it too. You may
issue both synchronous and asynchronous reporting requests, and
optionally schedule reports to be received by email.

* * * * *

Next:[New Users](/manuals/Enterprise-3-0-API#New-Users),
Previous:[Built-in Reports vs. Reporting
Engine](/manuals/Enterprise-3-0-API#Built_002din-Reports-vs_002e-Reporting-Engine),
Up:[Differences between the CFEngine Nova 2.2 REST API and the CFEngine
Enterprise 3.0
API](/manuals/Enterprise-3-0-API#Differences-between-the-CFEngine-Nova-2_002e2-REST-API-and-the-CFEngine-Enterprise-3_002e0-API)

#### 1.2.3 Content-Type

The 2.2 API has a HTTP content-type
`application/vnd.cfengine.nova-v1+json`. In the 3.0 API the content-type
is `application/vnd.cfengine.enterprise-v1+json`. This reflects a
branding change away from Nova to Enterprise.

* * * * *

Next:[Base Path](/manuals/Enterprise-3-0-API#Base-Path),
Previous:[Content-Type](/manuals/Enterprise-3-0-API#Content_002dType),
Up:[Differences between the CFEngine Nova 2.2 REST API and the CFEngine
Enterprise 3.0
API](/manuals/Enterprise-3-0-API#Differences-between-the-CFEngine-Nova-2_002e2-REST-API-and-the-CFEngine-Enterprise-3_002e0-API)

#### 1.2.4 New Users

The 2.2 API used credentials from the Mission Portal database to
authenticate and authorize users. These users have been moved into the
Hub database and security has been strengthened. We are now using salted
SHA256 passwords for the user table. Unfortunately, this means that
internal users need to be recreated. The Mission Portal now relies on
the API for authentication and authorization. This was partially done to
support multi-hub installations.

* * * * *

Next:[Still available](/manuals/Enterprise-3-0-API#Still-available),
Previous:[New Users](/manuals/Enterprise-3-0-API#New-Users),
Up:[Differences between the CFEngine Nova 2.2 REST API and the CFEngine
Enterprise 3.0
API](/manuals/Enterprise-3-0-API#Differences-between-the-CFEngine-Nova-2_002e2-REST-API-and-the-CFEngine-Enterprise-3_002e0-API)

#### 1.2.5 Base Path

The 2.2 API had a base path `/rest`. In the 3.0 API the base path is
`/api`.

* * * * *

Next:[Mission Portal](/manuals/Enterprise-3-0-API#Mission-Portal),
Previous:[Base Path](/manuals/Enterprise-3-0-API#Base-Path),
Up:[Differences between the CFEngine Nova 2.2 REST API and the CFEngine
Enterprise 3.0
API](/manuals/Enterprise-3-0-API#Differences-between-the-CFEngine-Nova-2_002e2-REST-API-and-the-CFEngine-Enterprise-3_002e0-API)

#### 1.2.6 Still available

In 3.0, the old 2.2 API is still available along side the new 3.0 API,
so you can keep calling the old API if needed.

* * * * *

Previous:[Still available](/manuals/Enterprise-3-0-API#Still-available),
Up:[Differences between the CFEngine Nova 2.2 REST API and the CFEngine
Enterprise 3.0
API](/manuals/Enterprise-3-0-API#Differences-between-the-CFEngine-Nova-2_002e2-REST-API-and-the-CFEngine-Enterprise-3_002e0-API)

#### 1.2.7 Mission Portal

Starting in 3.0, most of the API is exercised by the Mission Portal
web-UI.

* * * * *

Next:[Managing Settings](/manuals/Enterprise-3-0-API#Managing-Settings),
Previous:[Differences between the CFEngine Nova 2.2 REST API and the
CFEngine Enterprise 3.0
API](/manuals/Enterprise-3-0-API#Differences-between-the-CFEngine-Nova-2_002e2-REST-API-and-the-CFEngine-Enterprise-3_002e0-API),
Up:[REST API](/manuals/Enterprise-3-0-API#REST-API)
