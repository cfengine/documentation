---
layout: default
title: Hosts
sorting: 30
published: true
---

The Hosts app provides a customizable global overview of _promise_ compliance. A summary of compliant vs non-compliant hosts is provided at each branch in the tree.

Each host is in one of two groups: out of compliance or fully compliant.

* A host is considered out of compliance if less than 100% of its promises were kept.
* A host is considered fully compliant if 100% of its promises were kept.

<img src="Hosts-app-overview.png" alt="Hosts app overview" width="700px">

A host tree based on OS (Operating system) is present by default. Host trees map hosts based on reported classes into a hierarchy. Additional host trees can be added based on classes, which could be used to view different perspectives such as geographic location, production tier, business unit, etc. Furthermore, each host tree can be shared based on Mission Portal role.

<img src="Hosts-app-custom-tree-geographic-region.png" alt="Hosts app custom tree for geographic region" width="439px">

Visiting a leaf node provides a summary of host specific information.

## Host info ##

The host info page provides extensive information for an individual host.

<img src="Host-info-page.png" alt="Host info page" width="700px">

### Host actions ###

Take action on a host.

<img src="host-action-buttons.png" alt="Host action buttons" width="280px">

* <img src="host-info-run-agent.png" alt="Run agent" width="50px"> :: Request an unscheduled policy run
* <img src="host-info-collect-reports.png" alt="Collect reports" width="50px"> :: Request report collection
* <img src="host-info-get-url.png" alt="Get URL" width="50px"> :: Get the URL to the specific hosts info page
* <img src="host-info-delete-host.png" alt="Delete host" width="50px"> :: Delete the host

### Host specific data ###

Assign host specific _Variables_ and _Classes_.

<img src="host-specific-data-variables.png" alt="Host specific data variables" width="488px">

Note: When defined via host specific data, variables default to the `variables` _bundle_ of the `data` _namespace_. Qualify the variable with the desired bundle and namespace to override the default. For example `my_bundle.myvariable` to define `my_bundle.myvariable` in the `data` namespace, or `my_namespace:my_bundle.myvariable` to define `myvariable` in the `my_bundle` bundle of the `my_namespace` namespace.

<img src="host-specific-data-classes.png" alt="Host specific data classes" width="488px">

Note: When defined via host specific data classes default to the `data` _namespace_. Qualify the class with the desired namespace to override the default. For example `default:my_class`, or `my_namespace:my_class`.
