---
layout: default
title: User Interface
sorting: 20
published: true
tags: [cfengine enterprise, user interface, mission portal]
---

The challenge in engineering IT infrastructure, especially as it scales
vertically and horizontally, is to recognize the system components, what they do
at any given moment in time (or over time), and when and how they change state.

CFEngine Enterprise's data collection service, the `cf-hub` collector, collects,
organizes, and stores data from every host. The data is stored primarily in a
PostgreSQL database.

CFEngine Enterprise's user interface, the Mission Portal makes that data
available to authorized users as high level reports or alerts and notifications.
The reports can be designed in a GUI report builder or directly with SQL
statements passed to PostgreSQL.

* [Dashboard][User Interface#Dashboard]
* [Hosts and Health][User Interface#Hosts and Health]
* [Reporting][User Interface#Reporting]
* [Sharing][User Interface#Sharing]
* [Monitoring][User Interface#Monitoring]
* [Settings][User Interface#Settings]

## Dashboard

The Mission Portal dashboard allows users to create customized summaries showing
the current state of the infrastructure and its compliance with deployed policy.

The dashboard contains informative widgets that you can customize to create
alerts. All notifications of alert state changes, e.g. from OK to not-OK, are
stored in an event log for later inspection and analysis.

### Alert widgets

![Enterprise UI Alerts](welcome_2nd_screen.png)

Alerts can have three different severity level: low, medium and high. These are
represented by yellow, orange and red rings respectively, along with the
percentage of hosts alerts have triggered on. Hovering over the widget will show
the information as text in a convenient list format.

![Enterprise UI Alerts](widget_1.gif)

You can pause alerts during maintenance windows or while working on resolving an
underlying issue to avoid unnecessary triggering and notifications.

![Enterprise UI Alerts](pause_alerts.gif)

Alerts can have three different states: OK, triggered, and paused. It is easy to
filter by state on each widget's alert overview.

Find out more: [Alerts and Notifications][]

### Changes widget

The changes widget helps to visualize the number of changes (promises repaired)
made by `cf-agent`.

![Dashboard Changes widget](dashboard-widget-changes.png)

### Event log

The event log on the dashboard is filtered to show only information relevant
based on the widgets present. It shows when alerts are triggered and cleared and
when hosts are bootstrapped or decommissioned.

![Dashboard Event log](dashboard-event-log.png)

### Hosts count widget

The hosts count widget helps to visualize the number of hosts bootstrapped to cfengine over time.

![Dashboard Hosts count](dashboard-widget-hosts-count.png)

## Hosts and Health

CFEngine collects data on promise compliance, and sorts hosts according to 3
different categories: erroneous, fully compliant, and lacking data.

Find out more: [Hosts and Health][]

## Reporting

Inventory reports allow for quick reporting on out-of-the-box attributes. The
attributes are also extensible, by tagging any CFEngine variable or class, such
as the role of the host, inside your CFEngine policy. These custom attributes
will be automatically added to the Mission Portal.

![Enterprise UI Reporting](inventory-hover.png)

You can reduce the amount of data or find specific information by filtering on
attributes and host groups. Filtering is independent from the data presented in
the results table: you can filter on attributes without them being presented in
the table of results.

![Enterprise UI Reporting](inventory_filter.gif)

Add and remove columns from the results table in real time, and once you're
happy with your report, save it, export it, or schedule it to be sent by email
regularly.

![Enterprise API Overview](add_columns.png)

Find out more: [Reporting][Reporting UI]

Follow along in the [custom inventory tutorial][Custom Inventory] or read the
[MPF policy that provides inventory][inventory/].

## Sharing

Dashboards, Host categorization views, and Reports can be shared based on role.

Please note that the logic for sharing based on roles is different than the
logic that controls which hosts a given role is allowed access to data for. When
a Dashboard, Host categorization, or report is shared with a role, anyone having
that role is allowed to access it. For example if a dashboard is shared with the
`reporting` and `admin` roles users with either the role `reporting` or the role
`admin` are allowed access.

**For example:**

- `user1` has only the `reporting` role.
- `admin` has the `admin` role.

If the `admin` user creates a new dashboard and shares it with the `reporting`
role, then any user (including `user1` ) having the `reporting` role will be
able to subscribe to the new dashboard. Additionally the dashboard owner in this
case `admin` also has access to the custom dashboard.

## Monitoring

Monitoring allows you to get an overview of your hosts over time.

Find out more: [Monitoring][]

## Settings

A variety of CFEngine and system properties can be changed in the Settings view.

Find out more: [Settings][]
