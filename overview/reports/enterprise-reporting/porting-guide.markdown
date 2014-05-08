---
layout: default
title:  API Porting Guide
published: true
sorting: 90
tags: [manuals, enterprise, rest, api, reporting, porting]
---

In CFEngine Enterprise 3.5, the old 2.2 API is still available along 
side the new API, so you can keep calling the old API if needed. Starting in 
CFEngine Enterprise 3.0, most of the API is exercised by the Mission Portal
web-UI.


## Read vs. Read/Write

The 2.2 API was read-only and users, roles and settings were managed by
the Mission Portal. In contrast, the 3.0 API is read/write and
completely independent from the Mission Portal. In CFEngine
Enterprise 3.0, users, roles and settings belong in the API, and the
Mission Portal uses this to determine access to data. Additionally, some
other resources support PUT, POST and DELETE, but most data collected
from agents are read-only.


## Built-in Reports vs. Reporting Engine

The 2.2 API provided an almost one-to-one correspondence between the
reports in the Mission Portal and the API. One of the big changes in
CFEngine Enterprise 3.0 is the advent of SQL reports. This is provided
to the Mission Portal through the API, and you can use it too. You may
issue both synchronous and asynchronous reporting requests, and
optionally schedule reports to be received by email.


## Content-Type

The 2.2 API has a HTTP content-type `application/vnd.cfengine.nova-v1+json`. 
In the 3.0 API the content-type is 
`application/vnd.cfengine.enterprise-v1+json`. This reflects a
branding change away from Nova to Enterprise.

## New Users

The 2.2 API used credentials from the Mission Portal database to
authenticate and authorize users. These users have been moved into the
Hub database and security has been strengthened. We are now using salted
SHA256 passwords for the user table. Unfortunately, this means that
internal users need to be recreated. The Mission Portal now relies on
the API for authentication and authorization. This was partially done to
support multi-hub installations.

## Base Path

The 2.2 API had a base path `/rest`. In the 3.0 API the base path is
`/api`.
