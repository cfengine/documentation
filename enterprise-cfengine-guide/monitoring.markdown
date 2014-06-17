---
layout: default
title: Monitoring
sorting: 60
published: true
tags: [cfengine enterprise, user interface, mission portal]
---

Monitoring allows you to get an overview of your hosts over time.

![Monitoring](Mission-Portal-Monitoring-1.png)

You can filter on the type of `promise`: user defined, system defined, or all.

You can display fewer graphs by selecting a sub-set of hosts from the menu on the left.

Monitoring is disabled by default.  You can enable it inside the Mission Portal Settings panel. If you still don't see any data, make sure that:

* `cf-monitord` is running on your hosts. This is configurable through the lists `agents_to_be_enabled` and `agents_to_be_disabled` in `masterfiles/update/update_processes.cf`.
* `cf-hub` has access to collecting the monitoring data from your hosts. This is configurable through the `monitoring_include` and `monitoring_exclude` attributes in `report_data_select` in `masterfiles/controls/cf_serverd.cf`.
