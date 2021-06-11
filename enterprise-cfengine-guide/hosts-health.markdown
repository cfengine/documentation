---
layout: default
title: Hosts and Health
sorting: 30
published: true
tags: [cfengine enterprise, user interface, mission portal]
---

## Hosts ##

The Hosts app provides a customizable global overview of _promise_ compliance. A summary of compliant vs non-compliant hosts is provided at each branch in the tree.

Each host is in one of two groups: out of compliance or fully compliant.

* A host is considered out of compliance if less than 100% of its promises were kept.
* A host is considered fully compliant if 100% of its promises were kept.

![Hosts app overview](Hosts-app-overview.png)

A host tree based on OS (Operating system) is present by default. Host trees map hosts based on reported classes into a hierarchy. Additional host trees can be added based on classes, which could be used to view different perspectives such as geographic location, production tier, business unit, etc.... Furthermore, Each host tree can be shared based on Mission Portal role.

![Hosts app custom tree for geographic region](Hosts-app-custom-tree-geographic-region.png)

Visiting a leaf node provides a summary of host specific information.

### Host Info ###

The host info page provides extensive information for an individual hosts including information about:

* Identity
* Operating System
* Network details
* Reporting Status
* Software
* Health
* Inventory
* Measurements

![Host info page](Host-info-page.png)

## Host Health ##

![Hosts](Mission-portal-health-dignostics-header.png)

You can get quick access to the health of hosts, including direct links to reports, from the Health drop down at the top of every Enterprise UI screen. Hosts are listed as unhealthy if:

* the hub was not able to connect to and collect data from the host within a set time interval (unreachable host). The time interval can be set in the Mission Portal settings.
* the policy did not get executed for the last three runs. This could be caused by `cf-execd` not running on the host (scheduling deviation) or an error in policy that stops its execution. The hub is still able to contact the host, but it will return stale data because of this deviation.
* two or more hosts use the same key. This is detected by "reporting cookies", randomized tokens generated every report collection. If the client presents a mismatching cookie (compared to last collection) a collision is detected. The number of collisions (per hostkey) that cause the unhealthy status is configurable in [settings][Settings#Preferences].
* reports have recently been collected, but cf-agent has not recently run. "Recently" is defined by the configured run-interval of their cf-agent.

These categories are non-overlapping, meaning a host will only appear in one category at at time even if conditions satisfying multiple categories might be present. This makes reports simpler to read, and makes it easier to detect and fix the root cause of the issue. As one issue is resolved the host might then move to another category.
In either situation the data from that host will be from old runs and probably not reflect the current state of that host.

