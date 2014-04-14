---
layout: default
title: Host Monitoring in Mission Portal
sorting: 100
published: true
tags: [overviews, mission portal, hosts, monitoring, host monitoring]
---

## Monitoring App ##

You are also able to filter on the type of `promise`: user defined, system defined, or all.

You can reduce the number of graphs displayed by selecting a sub-set of hosts from the menu on the left.

This app is disabled by default, you can enable it inside the Settings. In case you are still not able to see any data, make sure that

* `cf-monitord` is running on your hosts. This is configurable through the lists `agents_to_be_enabled` and `agents_to_be_disabled` in `masterfiles/update/update_processes.cf`.
* `cf-hub` has access to collecting the monitoring data from your hosts. This is configurable through the `monitoring_include` and `monitoring_exclude` attributes in `report_data_select` in `masterfiles/controls/cf_serverd.cf`.





