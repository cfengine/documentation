---
layout: default
title: Enterprise Reporting
sorting: 50
published: true
tags: [cfengine enterprise, user interface, mission portal]
---

CFEngine Enterprise can report on variables, classes, and
monitoring data. Being an autonomous system all of the information about
promise outcomes is stored locally on the agent. Currently what is
stored (on disk) is not user configurable, but can currently be
correlated with anything you see in Mission Portal as far as reporting
options are concerned. For example, promise handles, promise outcomes
(kept/notkept/repaired), the value of a variable, and the existence of
classes are good examples but also extends to things like the file a
promise is in, which line number the promise was from, and more. You
can explore all the options by checking out the custom reports section
of the Enterprise Reporting module.

Specifically which information allowed to be collected by the hub for
reporting is configured in `report_data_select`. `default_data_select_host`
defines the data to be collected for a non policy hub and
`default_data_select_policy_hub` defines the data that should be
collected for a policy hub. Both body definitions can be found in the
`masterfiles/lib/<VERSION>/reports.cf`. As of CFEngine 3.6.0 a list of regular
expressions matching promise meta tags for either
[inclusion][access#metatags_include] or [exclusion][access#metatags_exclude]
are how you control which variables and classes are collected for central
reporting. By default we collect `variables` and `classes` that are tagged with
either `report` or `inventory`. Instead of extending this list of tags we
recommend that you tag variables and classes with `report`. If it's desirable
to make available in specialized inventory reporting interface then you it
should be tagged with `inventory` and given an additional `attribute_name=` tag
as described in the [Custom Inventory Example][Custom Inventory].  By default
CFEngine collects information for all promise outcomes. This can be further
restricted by specifying [promise_handle_include][access#promise_handle_include]
or [promise_handle_exclude][access#promise_handle_exclude]. Controlling which
measurements taken by `cf-monitord`are reported is controlled via the
`report_data_select` attributes `monitoring_include` and `monitoring_exclude`.

For information on accessing reported information please see the
[Reporting UI guide][Reporting UI].
