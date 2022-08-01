---
layout: default
title: Hosts
sorting: 30
published: true
tags: [cfengine enterprise, user interface, mission portal]
---

The Hosts app provides a customizable global overview of _promise_ compliance. A summary of compliant vs non-compliant hosts is provided at each branch in the tree.

Each host is in one of two groups: out of compliance or fully compliant.

* A host is considered out of compliance if less than 100% of its promises were kept.
* A host is considered fully compliant if 100% of its promises were kept.

![Hosts app overview](Hosts-app-overview.png)

A host tree based on OS (Operating system) is present by default. Host trees map hosts based on reported classes into a hierarchy. Additional host trees can be added based on classes, which could be used to view different perspectives such as geographic location, production tier, business unit, etc.... Furthermore, Each host tree can be shared based on Mission Portal role.

![Hosts app custom tree for geographic region](Hosts-app-custom-tree-geographic-region.png)

Visiting a leaf node provides a summary of host specific information.

## Host Info ##

The host info page provides extensive information for an individual host.

![Host info page](Host-info-page.png)

### Host Actions ###

Take action on a host.

![Host action buttons](host-action-buttons.png)

* ![Run agent](host-info-run-agent.png) :: Request an unscheduled policy run
* ![Collect reports](host-info-collect-reports.png):: Request report collection
* ![Get URL](host-info-get-url.png):: Get the URL to the specific hosts info page
* ![Delete host](host-info-delete-host.png) :: Delete the host

### Host specific data ###

Assign host specific _Variables_ and _Classes_.

![Host specific data](host-specific-data.png)

