---
layout: default
title: New in CFEngine
published: true
sorting: 10
tags: [overviews, releases, latest release, "3.6", platforms, versions, what's new]
---

<!--- TODO: move up when no longer a pre-release

**IMPORTANT NOTE:** This is a pre-release of CFEngine, intended for testing and
showcase only.

-->

CFEngine 3.6 is the latest version of CFEngine. The [Enterprise edition][New in CFEngine#CFEngine Enterprise] introduces
numerous improvements to the Mission Portal - a dashboard for getting a quick overview
of the system status and compliance, alerts and notifications for changes to the
system, a new user interface for inventory management and a tighter integration with
Design Center.

Policy writers and community users, CFEngine 3.6 introduces a broad range of improvements and new
functionality to the policy language, new capabilities for configuration management
and tighter integration with data from external sources.

## Improvements for Policy Writers ##

A number of changes have been made to the CFEngine core to further improve stability,
scalability and security.

### User Account Management ###

The new `users` promise type allows for management and configuration of local user
accounts with CFEngine.

### Data Containers for Structured Data ###

The new variable type `data` allows handling of structured data within CFEngine policy.
Structured data can be read from JSON strings and files, which allows integrating of
CFEngine policies with any external data source that can export to JSON.

A range of new functions allow creating and operating on structured data.

### Tagging with Meta Data ###

Classes and variables can be tagged with meta data for extended annotation and
documentation of knowledge directly in the language. Classes and variables can be
searched by tags in policy, and CFEngine Enterprise uses tags to identify relevant
information reported by the host. CFEngine sets a number of tags on hard classes and
special variables by default.

### Improved File Templating Engine ###

CFEngine 3.6 introduces support for [`mustache`][files#template_method] templates, which
is tightly integrated with data containers and provides easy and data-driven configuration
file management.

### New and Improved Functions ###

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


### Network Protocol on top of TLS ###

CFEngine 3.6 introduces a new networking protocol, which uses TLS for authentication.
After the authentication, all dialog is encrypted within the established TLS session.

To ease with the upgrade process, `cf-serverd` is still able to speak the legacy
protocol with old agents, and new agents can speak the legacy protocol with old servers.
CFEngine operators should turn off support for the legacy protocol as soon as all hosts
are running 3.6 to benefit from the full encryption and future improvements.

The new network protocol supports a range of new attributes for more precise access
control to server resources.

### Other Core Changes ###

CFEngine 3.6 uses [LMDB][] as the default embedded database. LMDB is both robust and fast,
and replaces TokyoCabinet on the majority of supported platforms.

Logging output of the CFEngine binaries has been further improved: `cf-serverd` now includes
the relevant client IP address in all messages; `reports` promises generate messages without
prefix except ```R:```, and execution state information (such as passes or promise type
changes) are included in the log.

Relative paths are supported in `copy_from` promises, and can used together with the
`shortcut` aliasing based on `connection` data in `access` promises to implement simple
and dynamic multi-tenancy within a single policy server.

## CFEngine Enterprise ##



### Mission Portal ###

CFEngine 3.6 introduces a flexible and dynamic dashboard with [alerts and notifications][]
to the Mission Portal. Users can create conditions and group those together in dashboard
widgets that provide a quick overview over various business-critical aspects of the CFEngine
managed system.

[Inventory reports][Reporting UI] provide fast access to the managed assets, be it hosts or software.
Inventory data can be added through policy to read additional information from sources
available to each host, such as a CMDB.

### Enterprise Platform and API ###

The Enterprise platform in 3.6 is using PostgreSQL, which significantly improves the
speed of reports in the Mission Portal and through the Enterprise APIs. The Enterprise
Server uses an optimized data collection protocol that reduces the network traffic and
allows for even greater scalability.

The [Enterprise API][] provides faster access to more data about hosts, promise compliance,
software inventories, classes and variables. Thanks to the PostgreSQL backend the API supports
complex SQL queries. The API from CFEngine Enterprise 2.2 is no longer supported.

The integration with authentication services (LDAP or ActiveDirectory) has changed to allow
filter stings to be specified, providing greater flexibility in controlling access to CFEngine
Enterprise.

### Windows Support ###

A number of improvements to CFEngine's string handling on Windows makes sure that
line endings are preserved in modified files, and use Windows compliance CRLF endings
in newly created files.

## Change History ##

For a complete history of changes in CFEngine, see the `ChangeLog` and
`Enterprise ChangeLog`.
