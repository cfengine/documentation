---
layout: default
title: cfmp
aliases:
  - "/api-enterprise-api-ref-sql-schema-cfmp.html"
---

This database contains Mission Portal related settings not processed by the API.

## Table: app

Information about Mission Portal applications.

**Columns:**

- **displayindex** _(integer)_
  The display order of the app in the Mission Portal menu.
- **filepath** _(text)_
  The path of the app module in the application directory.
- **hascontroller** _(integer)_
  The flag that indicates whether the app has a controller file or not.
- **icon** _(character varying(50))_
  The name of the app icon file in the images directory.
- **meta** _(json)_
  The JSON object that stores the app metadata, such as name, description, license, etc.
- **showappslist** _(integer)_
  The flag that indicates whether the app is visible in the Mission Portal menu or not.
- **state** _(integer)_
  The state of the app, such as 1 or 0.
- **url** _(text)_
  The URL of the app in the Mission Portal.
- **id** _(character varying(100))_
  The unique identifier of the app, used as the primary key.
- **rbac_id** _(character varying(50))_
  The identifier of the RBAC permission that the app requires, may be null.

## Table: astrolabeprofile

Information about Host trees such as who it was created by, who it is shared with and the definition of the host tree.

**Columns:**

- **id** _(integer)_
  The unique identifier of the profile, generated from a sequence.
- **username** _(character varying(50))_
  The username of the user who created or owns the profile.
- **profileid** _(character varying(50))_
  The name of the profile, such as OS, Services, etc.
- **defaulttree** _(boolean)_
  The flag that indicates whether the profile is the default one for the user or not.
- **globaltree** _(boolean)_
  The flag that indicates whether the profile is a global one for all users or not.
- **sharedpermission** _(character varying(50)[])_
  The array of usernames that the profile is shared with, may be empty.
- **sharedby** _(character varying(50)[])_
  The array of usernames that shared the profile with the user, may be empty.
- **data** _(json)_
  The JSON object that stores the profile data, such as label, classRegex, children, etc.

## Table: ci_sessions

Information about current sessions.

**Columns:**

- **id** _(character varying(128))_
  The unique identifier of the session, used as the primary key.
- **ip_address** _(character varying(45))_
  The IP address of the user who initiated the session.
- **timestamp** _(bigint)_
  The UNIX timestamp of the last activity of the session.
- **data** _(text)_
  The text data of the session, encoded in base64.

## Table: compliance_score

Compliance reports score.

**Columns:**

- **report_id** _(integer)_
  The id of the compliance report that the user has generated.
- **username** _(text)_
  The name of the user who has generated the compliance report.
- **score** _(integer)_
  The percentage of compliance checks that the user has passed.
- **update_ts** _(timestamp with time zone)_
  The timestamp of the last update of the compliance report.
- **fail_checks** _(integer)_
  The number of compliance checks that the user has failed.
- **total** _(integer)_
  The total number of compliance checks that the user has performed.

## Table: customization

Stores Mission Portal UI customization config.

**Columns:**

- **key** _(character varying)_
  The name of the customization option such as logo_on_login, login_text, header_color, etc.
- **value** _(text)_
  The value of the customization option.

## Table: dashboard_alerts

User dashboards alerts status.

**Columns:**

- **id** _(integer)_
  The primary key of the dashboard alerts table.
- **ruleid** _(integer)_
  The id of the rule that triggered the alert.
- **failhosts** _(integer)_
  The number of hosts that failed the rule.
- **lastcheck** _(integer)_
  The timestamp of the last check of the rule.
- **lasteventtime** _(integer)_
  The timestamp of the last event that caused the alert status to change.
- **laststatuschange** _(integer)_
  The timestamp of the last change of the alert status.
- **servertime** _(integer)_
  The timestamp of the server time when the alert was generated.
- **pause** _(integer)_
  The timestamp indicating when the alert was paused.
- **paused** _(integer)_
  A flag indicating whether the alert was paused by the user or not.
- **name** _(character varying(500))_
  The name of the alert.
- **severity** _(character varying(10))_
  The severity level of the alert, such as high, medium, or low.
- **site_url** _(text)_
  The URL of the Mission Portal host where the alert is displayed.
- **status** _(character varying(32))_
  The status of the alert, such as success, fail, or warning.
- **totalhosts** _(integer)_
  The total number of hosts that are affected by the rule.
- **username** _(character varying(50))_
  The name of the user who created the alert.
- **widgetname** _(character varying(100))_
  The name of the widget that shows the alert.
- **emailtonotify** _(character varying(100))_
  The email address of the user who will be notified of the alert.
- **reminder** _(integer)_
  The frequency of the reminder email for the alert.
- **widgetid** _(integer)_
  The id of the widget that shows the alert.
- **hostcontextsprofileid** _(character varying(20))_
  The id of the host contexts profile that defines the scope of the alert.
- **hostcontexts** _(json)_
  A JSON object containing the host contexts that define the scope of the alert.
- **hostcontextspath** _(text)_
  The path of the host contexts that define the scope of the alert.
- **excludedhosts** _(json)_
  A JSON object describing hosts that should be excluded from checking the alert.

## Table: dashboard_alerts_script

Association of script with dashboard alert.

**Columns:**

- **alert_id** _(integer)_
  The id of the dashboard alert that is associated with a script.
- **script_id** _(integer)_
  The id of the script that is associated with a dashboard alert.

## Table: dashboard_dashboards

User dashboards and configuration.

**Columns:**

- **id** _(integer)_
  The primary key of the dashboard table.
- **name** _(character varying(200))_
  The name of the dashboard.
- **username** _(character varying(20))_
  The name of the user who owns the dashboard.
- **public** _(integer)_
  A flag indicating whether the dashboard is public or private.
- **widgets** _(character varying(200))_
  A comma separated list of widget ids that are displayed on the dashboard.
- **sharedwith** _(jsonb)_
  A JSON object containing the roles, users, and sharedWithAll flag that determine the sharing settings of the dashboard.

## Table: dashboard_rules

User-defined dashboard alert rules.

**Columns:**

- **id** _(integer)_
  Unique identifier for the dashboard rule.
- **name** _(text)_
  Name of the dashboard rule.
- **description** _(text)_
  Description of the dashboard rule.
- **type** _(character varying(20))_
  Type of the dashboard rule (e.g., policy, softwareupdate, inventory).
- **username** _(character varying(20))_
  Username of the user who created the dashboard rule.
- **policyconditions** _(json)_
  Dashboard rule conditions for checks based on promise outcomes such as KEPT, NOT_KEPT, and REPAIRED. (JSON object)
- **inventoryconditions** _(json)_
  JSON object of conditions for inventory-based dashboard rules.
- **softwareupdateconditions** _(json)_
  JSON object of conditions for software update-based dashboard rules.
- **category** _(text)_
  Category assigned to the dashboard rule.
- **severity** _(text)_
  Severity level assigned to the dashboard rule such as low, medium, high.
- **hostcontexts** _(json)_
  JSON object describing the set of hosts the limiting the hosts that should be considered when checking the rule. If not set the condition is checked for against all hosts the user has access to based on RBAC and host reported data.
- **conditionmustbemet** _(boolean)_
  Flag indicating whether conditions must be met for the dashboard rule.
- **customconditions** _(json)_
  Custom dashboard conditions (for widgets), which use SQL queries returning hostkeys of affected hosts (JSON object).
- **filechangedconditions** _(json)_
  File changed conditions for the dashboard rule.
- **export_id** _(text)_
  Identifier for exporting dashboard rules.

## Table: dashboard_scripts

Table containing scripts available for association with alerts.

**Columns:**

- **id** _(integer)_
  Unique identifier for the script entry.
- **name** _(text)_
  Name of the script.
- **description** _(text)_
  Description of the script.
- **script_name** _(text)_
  Name of the actual script file.
- **type** _(text)_
  Type of the script. (not used)

## Table: dashboard_widgets

User configurations for dashboard widgets.

**Columns:**

- **id** _(integer)_
  Unique identifier for the dashboard widget.
- **name** _(character varying(500))_
  Name of the dashboard widget.
- **type** _(character varying(20))_
  Type of the dashboard widget (e.g., inventory, alerts, hostCount).
- **username** _(character varying(50))_
  Username of the user who configured the dashboard widget.
- **ordering** _(integer)_
  Ordering of the dashboard widget in the dashboard.
- **dashboardid** _(integer)_
  Identifier for the associated dashboard.
- **payload** _(jsonb)_
  JSON payload containing additional configuration for the dashboard widget.

## Table: eventslog

Event logs.

**Columns:**

- **id** _(integer)_
  Unique identifier for the event log entry.
- **username** _(character varying(100))_
  Username associated with the event log entry.
- **item_id** _(character varying(100))_
  Identifier associated with the item triggering the event (e.g., alert id).
- **item_type** _(character varying)_
  Type of the item triggering the event (e.g., host, alerts).
- **item_name** _(character varying(500))_
  Name of the item triggering the event.
- **tags** _(character varying(500)[])_
  Tags associated with the event log entry.
- **time** _(timestamp without time zone)_
  Timestamp when the event occurred.
- **severity** _(character varying(20))_
  Severity level of the event such as low, medium, high. Not all events specify a severity.
- **message** _(text)_
  Detailed message describing the event.
- **status** _(character varying(10))_
  Status of the event (e.g., triggered, cleared).

## Table: favourite_reports

Table associating favorited reports with users.

**Columns:**

- **report_id** _(bigint)_
  Identifier of the favorite report.
- **username** _(text)_
  Username of the user who marked the report as a favorite.
- **created_at** _(timestamp with time zone)_
  Timestamp indicating when the report was marked as a favorite.

## Table: mail_settings

Global email settings.

**Columns:**

- **key** _(character varying)_
  Key representing a specific email setting.
- **value** _(text)_
  Value associated with the email setting key.

## Table: pinned_items

Pinned inventory, class, or variable items.

**Columns:**

- **id** _(bigint)_
  Unique identifier for the pinned item.
- **username** _(text)_
  Username of the user who pinned the item.
- **type** _(pinned_type)_
  Type of the pinned item (e.g., inventory, class, variable).
- **name** _(text)_
  Name of the pinned item.
- **created_at** _(timestamp with time zone)_
  Timestamp indicating when the item was pinned.

## Table: report

Information about saved reports.

**Columns:**

- **id** _(integer)_
  The primary key of the report table.
- **username** _(character varying(50))_
  The name of the user who saved the report.
- **url** _(character varying(500))_
  The URL of the report.
- **reporttype** _(character varying(50))_
  The type of the report, such as compliance, inventory, or software update.
- **reportcategory** _(character varying(50))_
  The category of the report, such as security, performance, or other.
- **type** _(character varying(50))_
  The format of the report, such as pdf or csv.
- **readonly** _(integer)_
  A flag indicating whether the report is read-only or editable.
- **is_public** _(integer)_
  A flag indicating whether the report is public or private.
- **can_subscribe** _(integer)_
  A flag indicating whether the report can be subscribed to or not.
- **is_subscribed** _(integer)_
  A flag indicating whether the user is subscribed to the report or not.
- **label** _(character varying(500))_
  The label of the report.
- **date** _(timestamp without time zone)_
  The date of the report.
- **params** _(text)_
  The parameters of the report.
- **sharedpermission** _(character varying(50)[])_
  A list of permissions that the report has been shared with.
- **sharedby** _(character varying(50)[])_
  A list of users who have shared the report.
- **advancedreportsdata** _(json)_
  A JSON object containing the advanced reports data.
- **export_id** _(text)_
  The export id of the report, used for importing and exporting reports.
- **meta_data** _(jsonb)_
  A JSON object containing the meta data of the report.

## Table: report_schedule

Information about scheduled reports.

**Columns:**

- **id** _(character varying(500))_
  The unique identifier for the scheduled report.
- **reportid** _(integer)_
  The foreign key referencing the associated report.
- **userid** _(character varying(50))_
  The user ID associated with the scheduled report.
- **title** _(character varying(500))_
  The title of the scheduled report.
- **description** _(character varying(500))_
  The description of the scheduled report.
- **emailfrom** _(character varying(500))_
  The email address from which the report is sent.
- **emailto** _(character varying(500))_
  The email address to which the report is sent.
- **enabled** _(integer)_
  Flag indicating whether the scheduled report is enabled.
- **query** _(text)_
  The SQL query that defines the report for the scheduled task.
- **outputtypes** _(character varying(50)[])_
  Array of output types for the scheduled report.
- **schedule\*** _(character varying(500))_
  The schedule for running the report.
- **schedulehumanreadabletime** _(character varying(500))_
  Human-readable representation of the schedule time.
- **schedulename** _(character varying(500))_
  The name associated with the schedule.
- **site_url** _(text)_
  The URL associated with the scheduled report.
- **hostcontextsprofileid** _(character varying(20))_
  The profile ID associated with the host contexts.
- **hostcontextspath** _(text)_
  The path associated with the host contexts.
- **hostcontexts** _(json)_
  JSON data representing the subset of hosts that the report should be filtered for. If not defined the scheduled report includes all hosts the userid is allowed to see based on RBAC and data reported by the host.
- **scheduledata** _(json)_
  JSON data containing details about the schedule.
- **excludedhosts** _(json)_
  JSON data representing excluded hosts for the scheduled report.
- **skipmailing** _(boolean)_
  Flag indicating whether mailing is skipped for the scheduled report.

## Table: users

User preferences and information about Mission Portal behavior.

**Columns:**

- **id** _(integer)_
  The primary key of the user table.
- **username** _(character varying(50))_
  The unique name of the user.
- **source** _(character varying(20))_
  The source of the user account, such as internal or external (e.g. LDAP, Active Directory).
- **last_login** _(timestamp without time zone)_
  The timestamp of the last login of the user.
- **remember_code** _(character varying(50))_
  The code used to remember the user login session.
- **dashboard** _(integer)_
  The id of the default dashboard for the user.
- **seen_tour** _(smallint)_
  A flag indicating whether the user has seen the tour of the Mission Portal.
- **seen_wizard** _(smallint)_
  A flag indicating whether the user has seen the wizard of the Mission Portal.
- **never_ask_timezone_change** _(smallint)_
  A flag indicating whether the user wants to be asked about changing the timezone.
- **use_browser_time** _(smallint)_
  A flag indicating whether the user wants to use the browser time or the server time.
- **dark_mode** _(smallint)_
  A flag indicating whether the user prefers the dark mode or the light mode.
- **pinned_items_version** _(smallint)_
  This is used to add default pinned items which are added after this version.
- **additional_data** _(jsonb)_
  A JSON object containing additional data about the user preferences and behavior.

## Table: variables_dictionary

Information about reported inventory attributes.

**Columns:**

- **id** _(integer)_
  The unique identifier for the variable in the dictionary.
- **attribute_name** _(character varying(200))_
  The name of the attribute represented by the variable.
- **category** _(character varying(200))_
  The category to which the attribute belongs.
- **readonly** _(integer)_
  Flag indicating whether the attribute is read-only.
- **type** _(character varying(200))_
  The data type of the attribute such as string, slist, int, real.
- **convert_function** _(character varying(200))_
  The conversion function applied to the attribute such as cf_clearslist (if any).
