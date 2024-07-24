---
layout: default
title: Web UI
published: true
sorting: 40
---

The challenge in engineering IT infrastructure, especially as it scales
vertically and horizontally, is to recognize the system components, what they do
at any given moment in time (or over time), and when and how they change state.

CFEngine Enterprise's data collection service, `cf-hub`, collects,
organizes, and stores data from every host. The data is stored primarily in a
PostgreSQL database.

CFEngine Enterprise's user interface, Mission Portal, makes that data
available to authorized users as high level reports or alerts and notifications.
The reports can be designed in a GUI report builder or directly with SQL
statements passed to PostgreSQL.

## Dashboard

The Mission Portal dashboard allows users to create customized summaries showing
the current state of the infrastructure and its compliance with deployed policy.

The dashboard contains informative widgets that you can customize to create
alerts. All notifications of alert state changes, e.g. from OK to not-OK, are
stored in an event log for later inspection and analysis.

### Make changes to a shared dashboard

<img src="clone-dashboard.png" alt="Clone dashboard possibility" width="490px">

Create an editable copy by clicking the edit button (pencil icon) that appears when you hover over
the dashboard's row.

### Alert widgets

<img src="welcome_2nd_screen.png" alt="Enterprise UI Alerts" width="520px">

Alerts can have three different severity levels: low, medium and high. These are
represented by yellow, orange and red rings respectively, along with the
percentage of hosts alerts have triggered on. Hovering over the widget will show
the information as text in a convenient list format.

<img src="widget_1.gif" alt="Enterprise UI Alerts" width="300px">

You can pause alerts during maintenance windows or while working on resolving an
underlying issue to avoid unnecessary triggering and notifications.

<img src="pause_alerts.gif" alt="Enterprise UI Alerts" width="670px">

Alerts can have three different states: OK, triggered, and paused. It is easy to
filter by state on each widget's alert overview.

Find out more: [Alerts and notifications][]

### Changes widget

The changes widget helps to visualize the number of changes (promises repaired)
made by `cf-agent`.

<img src="dashboard-widget-changes.png" alt="Dashboard Changes widget" width="490px">

### Event log

The Event Log records a time-line of *significant events*.

Examples of significant events include:

- A new host registering to a hub (aka bootstrapping a host)
- Deleting a host
- Alert status change

Events are accessible {% comment %}via the Events API {% endcomment %}from every Mission Portal
dashboard. The event log on the dashboard is filtered to show only information
relevant based on the widgets present. It shows when alerts are triggered and
cleared and when hosts are bootstrapped or decommissioned.

<img src="dashboard-event-log.png" alt="Dashboard Event log" width="380px">

- The Events API Role Based Access Control (RBAC) for `Get event list` and `Get event` are required to view event log entries.

<img src="web-ui-events-api-rbac-get-event-list-event-checked.png" alt="Events API - Get event list & Get event RBAC" width="380px">

All Events can be searched and viewed from the Event Log page.

<img src="web-ui-event-log.png" alt="Events Log page" width="670px">

-  The Mission Portal RBAC for `View whole system events` is required to view the Event Log page.

<img src="web-ui-mission-portal-api-view-whole-system-events-rbac.png" alt="Mission Portal - Events View whole system events RBAC page" width="380px">


### Newly bootstrapped hosts widget

The Newly bootstrapped hosts widget helps to visualize the number of hosts bootstrapped to CFEngine over time.

<img src="dashboard-widget-newly-bootstrapped.png" alt="Dashboard Newly bootstrapped" width="412px">

## Hosts

CFEngine collects data on promise compliance, and sorts hosts into two categories: 100% compliant, and not.

Find out more: [Hosts][]

## Health

Mission Portal highlights potential issues related to the correct function of CFEngine Enterprise.

Find out more: [Health][]

## Reporting

Inventory reports allow for quick reporting on out-of-the-box attributes. The
attributes are also extensible, by tagging any CFEngine variable or class, such
as the role of the host, inside your CFEngine policy. These custom attributes
will be automatically added to the Mission Portal.

You can reduce the amount of data or find specific information by filtering on
attributes and host groups. Filtering is independent from the data presented in
the results table: you can filter on attributes without them being presented in
the table of results.

![Enterprise UI Reporting](inventory_filter.gif)

Add and remove columns from the results table in real time, and once you're
happy with your report, save it, export it, or schedule it to be sent by email
regularly.

<img src="add_columns.png" alt="Enterprise API Overview" width="650px">

Find out more: [Reporting][Reporting UI]

Follow along in the [custom inventory tutorial][Custom inventory] or read the
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

## Measurements

Monitoring allows you to get an overview of your hosts over time.

Find out more: [Measurements][Measurements app]

## Settings

A variety of CFEngine and system properties can be changed in the Settings view.

Find out more: [Settings][]

## User profile

The user profile is accessible from any view of the mission portal, from the drop down in the top right hand corner.

<img src="Settings-1.png" alt="Opening Profile" width="400px">

From the profile, you can adjust timezone options.

<img src="User-profile.png" alt="User Profile" width="412px">

* Time zone
  * You can select any time zone from the searchable drop-down.
* Autodetect time zone change and ask for update
  * If this option is selected Mission portal will ask you to update time zone when a difference is detected from your browser.
  <img src="Time-zone-modal.png" alt="Time zone modal" width="520px">

* Always use system/browser time
  * Mission portal will automatically change your profile timezone when a system/browser timezone is changed.
