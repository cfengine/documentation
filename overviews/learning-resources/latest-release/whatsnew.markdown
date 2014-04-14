---
layout: default
title: New in CFEngine
published: true
sorting: 10
tags: [overviews, releases, latest release, 3.6.0, platforms, versions, what's new]
---

**IMPORTANT NOTE:** This is a pre-release of CFEngine, intended for testing and 
showcase only.

<!--- TODO: move up when no longer a pre-release
-->

CFEngine 3.6 is the upcoming version of CFEngine. The Enterprise edition introduces
numberous improvements to the Mission Portal -a dashboard for getting a quick overview
of the system status and compliance, alerts and notifications for changes to the
system, a new user interface for inventory management and a tighter integration with
Design Center.

The Enterprise platform in 3.6 is using PostgreSQL, which significantly improves the
speed of reports in the Mission Portal and through the Enterprise APIs. The Enterprise
Server uses an optimized data collection protocol that reduces the network traffic and
allows for even greater scalability.

## Improvements for Policy Writers

For policy writers, CFEngine 3.6 introduces a broad range of improvements and new
functionality to the policy language, new capabilities for configuration management
and tighter integration with data from external sources.


### User Account Management

The new `users` promise type allows for management and configuration of local user
accounts with CFEngine.

### Data Containers for Structured Data

The new variable type `data` allows handling of structured data within CFEngine policy.
Structured data can be read from JSON strings and files, which allows integrating of
CFEngine policies with any external data source that can export to JSON.

A range of new functions allow creating and operating on structured data.

### Tagging with Meta Data

Classes and variables can be tagged with meta data for extended annotation and 
documentation of knowledge directly in the language. Classes and variables can be
searched by tags in policy, and CFEngine Enterprise uses tags to identify relevant
information reported by the host. CFEngine sets a number of tags on hard classes and
special variables by default.

### New and Improved Functions

CFEngine 3.6 adds a list of new built-in functions:

* `bundlesmatching()` - returns list of defined bundles matching a regex
* `canonifyuniquely()` - converts a string into a unique, legal class name
* `classesmatching()` - returns list of set classes matching a regex
* `eval()` - evaluates mathematical expressions
* `findfiles()` - returns list of files matching a search pattern
* `makerule()` - evaluates whether a target file needs to be rebuilt from sources
* `max()`, `mean()`, `min()` - returns maximum, mean and minimum in a container or list
* `packagesmatching()` - returns a filtered list of installed packages.
* `string_downcase()`, `string_upcase()` - returns the lower-/upper-case version of a string
* `string_head()`, `string_tail()` - returns the beginning/end of a string
* `string_length()` - returns the length of a string
* `string_reverse()` - reverses a string
* `variablesmatching()` - returns a list of variables matching a regex
* `variance()` - returns the variance of numbers in a list

The following functions are added and improved to work with the new `data` container
type:

* `data_readstringarray()` - read a delimited file into a data map
* `data_readstringarrayidx()` - read a delimited file into a data array
* `datastate()` - create a `data` variable with currently set classes and variables
* `datatype()` - 
* `format()` - `%S` can be used to serialize 'data' containers into a string
* `mergedata()` - merge two data containers
* `parsejson()` - create a data container from a JSON string
* `readjson()` - create a data container from a file that contains JSON
* `storejson()` - serialize a data container into a string


## Changes to the CFEngine Core

A number of changes have been made to the CFEngine core to further improve stability,
scalability and security; most importantly, the network protocol has been moved on top
of TLS for full encryption of all network traffic.

### Network Protocol on top of TLS

CFEngine 3.6 introduces a new networking protocol, which uses TLS for authentication.
After the authentication, all dialog is encrypted within the established TLS session.

To ease with the upgrade process, `cf-serverd` is still able to speak the legacy
protocol with old agents, and new agents can speak the legacy protocol with old servers.
CFEngine operators should turn off support for the legacy protocol as soon as all hosts
are running 3.6 to benefit from the full encryption and future improvements.

## ChangeLog

For a complete list of changes in the CFEngine, see the `ChangeLog` and 
`ChangeLog.Enterprise` files in `/var/cfengine/share/doc`. The Core change log
is also available 
[online](https://github.com/cfengine/core/blob/master/ChangeLog).
