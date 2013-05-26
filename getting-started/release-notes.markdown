---
layout: default
title: Release Notes
sortkey: 0
categories: [Getting Started, Release Notes]
published: true
alias: getting-started-release-notes.html
---

**IMPORTANT NOTE:** *This is a pre-release of 3.5, intended for testing and showcase only.
This version is not supported, not covered by service level agreements (SLAs) and not
intended for production environments. Do not upgrade or use in conjunction with other
versions at this point. We are planning monthly snapshot (alpha) releases going forward,
but official release date for 3.5 has not been set.*

<!--- TODO: move up when no longer a pre-release
-->

## Easier to Use

No matter if you are just starting with configuration management and system automation,
if you are a CFEngine novice or a battle-hardened policy coder, the new features
in CFEngine 3.5 will make it easy for you to get stuff done.

### Design Center, with UI in CFEngine Enterprise

**TODO:** screenshot, video, messaging?

### Significantly improved parsing and evaluation of policies

Policy developers get clear and consistent messages from the parser,
and operators benefit from a range of improvements in logging output, both to
the syslog and to the standard output.

**TODO:** screenshot, example, ???

### New built-in functions and capabilities

A broad range of new built-in functions simplify the coding of policies
significantly and offer completely new functionality.

* set operation functions that test for set membership and find
    intersections/differences:
    * [`every`](reference-functions-every.html)
    * [`none`](reference-functions-none.html)
    * [`some`](reference-functions-every.html)
    * [`intersection`](reference-functions-intersection.html),
    * [`difference`](reference-functions-difference.html)
* list functions  to look up a specific element, find the list length, extract a
  portion of the list, reduce it to unique element, sort it, and filter it
    * [`nth`](reference-functions-nth.html)
    * [`length`](reference-functions-length.html)
    * [`sublist`](reference-functions-sublist.html)
    * [`uniq`](reference-functions-uniq.html)
    * [`sort`](reference-functions-sort.html)
    * [`filter`](reference-functions-filter.html)
* function that returns an slist of all the classes that match a regular
  expression
    * [`classesmatching`](reference-functions-classesmatching.html)
* function that prints the time now or at a particular point
    * [`strftime`](reference-functions-strftime.html)
* function for building strings using sprintf semantics
    * [`format`](reference-functions-format.html)
* function for making logical decisions in a function call based on classes
    * [`ifelse`](reference-functions-ifelse.html)
* mapping function for arrays
    * [`maparray`](reference-functions-maparray.html)
* function for getting detailed file information
    * [`filestat`](reference-functions-filestat.html)

**TODO:** screenshot or code snippet?

### Improved out-of-the-box installation for Enterprise customers

The CFEngine Server and the Mission Portal UI are all up and running as soon
as the package installation is completed.

## Report collection at arbitrary scale

### Infinite scalability across multiple sites

* first support for multi-site reporting
* improved performance of cf-serverd, handling more connections in parallel

**TODO:** Link to demo video

### Improved SQL reporting

* Promise logs, file, software and compliance information are available
  through SQL Report app
* Regular expressions are supported in SQL queries
* **TODO:[Enterprise API](reference-enterprise-api.html)** supports host
  and promise filtering

## Better tools for CFEngine operators

* Self-diagnostics of agent binaries **TODO:**link to --self-diagnosics
* Collect data for hub diagnostics
** performance data from MongoDB
** Include lastseen report data
** FirstReportTimeStamp is recorded for all hosts
** diagnostic data from cf-hub
** data is available through SQL queries
* Configurable data collection for Enterprise
** Host-side report content filter, controlled by `report_data_select` body
   in **TODO**[access promise](reference-bundles-for-server-access-in-server-promises.html)
** filters for class, variable, promise log and monitoring reports

## Streamlined Mission Portal

**TODO:** screenshot

* slick UI design
* improved SQL reporting with access to more data
* performance improvements in the Mission Portal navigation tree

## Microsoft Windows specific improvements

* Windows PowerShell support in [commands promises](reference-bundles-for-agent-commands.html),
  [`execresult`](reference-functions-execresult.html) and [`returnszero`](reference-functions-returnszero.html)
* Improved ACL handling on Windows
** Note the syntax changes in the **TODO**[ChangeLog]


For a complete list of changes in the CFEngine Core, see the
[ChangeLog](https://github.com/cfengine/core/blob/3.5.x/ChangeLog).
**TODO: check package contents for ChangeLog files**
