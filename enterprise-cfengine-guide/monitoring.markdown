---
layout: default
title: Monitoring
sorting: 60
published: true
tags: [cfengine enterprise, user interface, mission portal]
---

Monitoring allows you to get an overview of your hosts over time.

![Monitoring](Mission-Portal-Monitoring-1.png)

If multiple hosts are selected in the menu on the left, then you can select one of three key measurements that is then displayed for all hosts:

* load average
* Disk free (in %)
* CPU(ALL) (in %)

You can reduce the number of graphs by selecting a sub-set of hosts from the menu on the left. If only a
single host is selected, then a number of graphs for various measurements will be displayed for this host. Which exact measurements are reported depends on how `cf-monitord` is configured and extended via `measurements` promises.

Clicking on an individual graph allows to select different time spans for which monitoring data will be displayed.

<!-- TODO - need screenshots, explanations of the zoom-in graphs, some explanation of the statistics etc -->

If you don't see any data, make sure that:

* `cf-monitord` is running on your hosts.
* `cf-hub` has access to collecting the monitoring data from your hosts. See [Configuring Enterprise Measurement and Monitoring Collection][Masterfiles Policy Framework#Configure Enterprise Measurement/Monitoring Collection] in the Masterfiles Policy Framework.
