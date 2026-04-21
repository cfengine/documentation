---
layout: default
title: cfmp
published: true
---

This database contains Mission Portal related settings not processed by the API.

## Table: app

Information about Mission Portal applications.

**Columns:**

* **displayindex**  *(integer)*
  The display order of the app in the Mission Portal menu.
* **filepath**      *(text)*
  The path of the app module in the application directory.
* **hascontroller** *(integer)*
  The flag that indicates whether the app has a controller file or not.
* **icon**          *(character varying(50))*
  The name of the app icon file in the images directory.
* **meta**          *(json)*
  The JSON object that stores the app metadata, such as name, description, license, etc.
* **showappslist**  *(integer)*
  The flag that indicates whether the app is visible in the Mission Portal menu or not.
* **state**         *(integer)*
  The state of the app, such as 1 or 0.
* **url**           *(text)*
  The URL of the app in the Mission Portal.
* **id**            *(character varying(100))*
  The unique identifier of the app, used as the primary key.
* **rbac_id**       *(character varying(50))*
  The identifier of the RBAC permission that the app requires, may be null.

## Table: astrolabeprofile

Information about Host trees such as who it was created by, who it is shared with and the definition of the host tree.

**Columns:**

* **id**               *(integer)*
  The unique identifier of the profile, generated from a sequence.
* **username**         *(character varying(50))*
  The username of the user who created or owns the profile.
* **profileid**        *(character varying(50))*
  The name of the profile, such as OS, Services, etc.
* **defaulttree**      *(boolean)*
  The flag that indicates whether the profile is the default one for the user or not.
* **globaltree**       *(boolean)*
  The flag that indicates whether the profile is a global one for all users or not.
* **sharedpermission** *(character varying(50)[])*
  The array of usernames that the profile is shared with, may be empty.
* **sharedby**         *(character varying(50)[])*
  The array of usernames that shared the profile with the user, may be empty.
* **data**             *(json)*
  The JSON object that stores the profile data, such as label, classRegex, children, etc.

## Table: ci_sessions

Information about current sessions.

**Columns:**

* **id**         *(character varying(128))*
  The unique identifier of the session, used as the primary key.
* **ip_address** *(character varying(45))*
  The IP address of the user who initiated the session.
* **timestamp**  *(bigint)*
  The UNIX timestamp of the last activity of the session.
* **data**       *(text)*
  The text data of the session, encoded in base64.

## Table: compliance_score

Compliance reports score.

**Columns:**

* **report_id**   *(integer)*
  The id of the compliance report that the user has generated.
* **username**    *(text)*
  The name of the user who has generated the compliance report.
* **score**       *(integer)*
  The percentage of compliance checks that the user has passed.
* **update_ts**   *(timestamp with time zone)*
  The timestamp of the last update of the compliance report.
* **fail_checks** *(integer)*
  The number of compliance checks that the user has failed.
* **total**       *(integer)*
  The total number of compliance checks that the user has performed.

## Table: customization

Stores Mission Portal UI customization config.

**Columns:**

* **key**    *(character varying)*
  The name of the customization option such as logo_on_login, login_text, header_color, etc.
* **value**  *(text)*
  The value of the customization option.

## Table: dashboard_alerts

User dashboards alerts status.

**Columns:**

* **id**                    *(integer)*
  The primary key of the dashboard alerts table.
* **ruleid**                *(integer)*
  The id of the rule that triggered the alert.
* **failhosts**             *(integer)*
  The number of hosts that failed the rule.
* **lastcheck**             *(integer)*
  The timestamp of the last check of the rule.
* **lasteventtime**         *(integer)*
  The timestamp of the last event that caused the alert status to change.
* **laststatuschange**      *(integer)*
  The timestamp of the last change of the alert status.
* **servertime**            *(integer)*
  The timestamp of the server time when the alert was generated.
* **pause**                 *(integer)*
  The timestamp indicating when the alert was paused.
* **paused**                *(integer)*
  A flag indicating whether the alert was paused by the user or not.
* **name**                  *(character varying(500))*
  The name of the alert.
* **severity**              *(character varying(10))*
  The severity level of the alert, such as high, medium, or low.
* **site_url**              *(text)*
  The URL of the Mission Portal host where the alert is displayed.
* **status**                *(character varying(32))*
  The status of the alert, such as success, fail, or warning.
* **totalhosts**            *(integer)*
  The total number of hosts that are affected by the rule.
* **username**              *(character varying(50))*
  The name of the user who created the alert.
* **widgetname**            *(character varying(100))*
  The name of the widget that shows the alert.
* **emailtonotify**         *(character varying(100))*
  The email address of the user who will be notified of the alert.
* **reminder**              *(integer)*
  The frequency of the reminder email for the alert.
* **widgetid**              *(integer)*
  The id of the widget that shows the alert.
* **hostcontextsprofileid** *(character varying(20))*
  The id of the host contexts profile that defines the scope of the alert.
* **hostcontexts**          *(json)*
  A JSON object containing the host contexts that define the scope of the alert.
* **hostcontextspath**      *(text)*
  The path of the host contexts that define the scope of the alert.
* **excludedhosts**         *(json)*
  A JSON object describing hosts that should be excluded from checking the alert.

## Table: dashboard_alerts_script

Association of script with dashboard alert.

**Columns:**

* **alert_id**  *(integer)*
  The id of the dashboard alert that is associated with a script.
* **script_id** *(integer)*
  The id of the script that is associated with a dashboard alert.

## Table: dashboard_dashboards

User dashboards and configuration.

**Columns:**

* **id**         *(integer)*
  The primary key of the dashboard table.
* **name**       *(character varying(200))*
  The name of the dashboard.
* **username**   *(character varying(20))*
  The name of the user who owns the dashboard.
* **public**     *(integer)*
  A flag indicating whether the dashboard is public or private.
* **widgets**    *(character varying(200))*
  A comma separated list of widget ids that are displayed on the dashboard.
* **sharedwith** *(jsonb)*
  A JSON object containing the roles, users, and sharedWithAll flag that determine the sharing settings of the dashboard.

## Table: dashboard_rules

User-defined dashboard alert rules.

**Columns:**

* **id**                       *(integer)*
  Unique identifier for the dashboard rule.
* **name**                     *(text)*
  Name of the dashboard rule.
* **description**              *(text)*
  Description of the dashboard rule.
* **type**                     *(character varying(20))*
  Type of the dashboard rule (e.g., policy, softwareupdate, inventory).
* **username**                 *(character varying(20))*
  Username of the user who created the dashboard rule.
* **policyconditions**         *(json)*
  Dashboard rule conditions for checks based on promise outcomes such as KEPT, NOT_KEPT, and REPAIRED. (JSON object)
* **inventoryconditions**      *(json)*
  JSON object of conditions for inventory-based dashboard rules.
* **softwareupdateconditions** *(json)*
  JSON object of conditions for software update-based dashboard rules.
* **category**                 *(text)*
  Category assigned to the dashboard rule.
* **severity**                 *(text)*
  Severity level assigned to the dashboard rule such as low, medium, high.
* **hostcontexts**             *(json)*
  JSON object describing the set of hosts the limiting the hosts that should be considered when checking the rule. If not set the condition is checked for against all hosts the user has access to based on RBAC and host reported data.
* **conditionmustbemet**       *(boolean)*
  Flag indicating whether conditions must be met for the dashboard rule.
* **customconditions**         *(json)*
  Custom dashboard conditions (for widgets), which use SQL queries returning hostkeys of affected hosts (JSON object).
* **filechangedconditions**    *(json)*
  File changed conditions for the dashboard rule.
* **export_id**                *(text)*
  Identifier for exporting dashboard rules.

## Table: dashboard_scripts

Table containing scripts available for association with alerts.

**Columns:**

* **id**          *(integer)*
  Unique identifier for the script entry.
* **name**        *(text)*
  Name of the script.
* **description** *(text)*
  Description of the script.
* **script_name** *(text)*
  Name of the actual script file.
* **type**        *(text)*
  Type of the script. (not used)

## Table: dashboard_widgets

User configurations for dashboard widgets.

**Columns:**

* **id**          *(integer)*
  Unique identifier for the dashboard widget.
* **name**        *(character varying(500))*
  Name of the dashboard widget.
* **type**        *(character varying(20))*
  Type of the dashboard widget (e.g., inventory, alerts, hostCount).
* **username**    *(character varying(50))*
  Username of the user who configured the dashboard widget.
* **ordering**    *(integer)*
  Ordering of the dashboard widget in the dashboard.
* **dashboardid** *(integer)*
  Identifier for the associated dashboard.
* **payload**     *(jsonb)*
  JSON payload containing additional configuration for the dashboard widget.
## Table: eventslog

Event logs.

**Columns:**

* **id**        *(integer)*
  Unique identifier for the event log entry.
* **username**  *(character varying(100))*
  Username associated with the event log entry.
* **item_id**   *(character varying(100))*
  Identifier associated with the item triggering the event (e.g., alert id).
* **item_type** *(character varying)*
  Type of the item triggering the event (e.g., host, alerts).
* **item_name** *(character varying(500))*
  Name of the item triggering the event.
* **tags**      *(character varying(500)[])*
  Tags associated with the event log entry.
* **time**      *(timestamp without time zone)*
  Timestamp when the event occurred.
* **severity**  *(character varying(20))*
  Severity level of the event such as low, medium, high. Not all events specify a severity.
* **message**   *(text)*
  Detailed message describing the event.
* **status**    *(character varying(10))*
  Status of the event (e.g., triggered, cleared).

## Table: favourite_reports

Table associating favorited reports with users.

**Columns:**

* **report_id**  *(bigint)*
  Identifier of the favorite report.
* **username**   *(text)*
  Username of the user who marked the report as a favorite.
* **created_at** *(timestamp with time zone)*
  Timestamp indicating when the report was marked as a favorite.

## Table: mail_settings

Global email settings.

**Columns:**

* **key**    *(character varying)*
  Key representing a specific email setting.
* **value**  *(text)*
  Value associated with the email setting key.

## Table: pinned_items

Pinned inventory, class, or variable items.

**Columns:**

* **id**         *(bigint)*
  Unique identifier for the pinned item.
* **username**   *(text)*
  Username of the user who pinned the item.
* **type**       *(pinned_type)*
  Type of the pinned item (e.g., inventory, class, variable).
* **name**       *(text)*
  Name of the pinned item.
* **created_at** *(timestamp with time zone)*
  Timestamp indicating when the item was pinned.

## Table: report

Information about saved reports.

**Columns:**

* **id**                  *(integer)*
  The primary key of the report table.
* **username**            *(character varying(50))*
  The name of the user who saved the report.
* **url**                 *(character varying(500))*
  The URL of the report.
* **reporttype**          *(character varying(50))*
  The type of the report, such as compliance, inventory, or software update.
* **reportcategory**      *(character varying(50))*
  The category of the report, such as security, performance, or other.
* **type**                *(character varying(50))*
  The format of the report, such as pdf or csv.
* **readonly**            *(integer)*
  A flag indicating whether the report is read-only or editable.
* **is_public**           *(integer)*
  A flag indicating whether the report is public or private.
* **can_subscribe**       *(integer)*
  A flag indicating whether the report can be subscribed to or not.
* **is_subscribed**       *(integer)*
  A flag indicating whether the user is subscribed to the report or not.
* **label**               *(character varying(500))*
  The label of the report.
* **date**                *(timestamp without time zone)*
  The date of the report.
* **params**              *(text)*
  The parameters of the report.
* **sharedpermission**    *(character varying(50)[])*
  A list of permissions that the report has been shared with.
* **sharedby**            *(character varying(50)[])*
  A list of users who have shared the report.
* **advancedreportsdata** *(json)*
  A JSON object containing the advanced reports data.
* **export_id**           *(text)*
  The export id of the report, used for importing and exporting reports.
* **meta_data**           *(jsonb)*
  A JSON object containing the meta data of the report.

## Table: report_schedule

Information about scheduled reports.

**Columns:**

* **id**                        *(character varying(500))*
  The unique identifier for the scheduled report.
* **reportid**                  *(integer)*
  The foreign key referencing the associated report.
* **userid**                    *(character varying(50))*
  The user ID associated with the scheduled report.
* **title**                     *(character varying(500))*
  The title of the scheduled report.
* **description**               *(character varying(500))*
  The description of the scheduled report.
* **emailfrom**                 *(character varying(500))*
  The email address from which the report is sent.
* **emailto**                   *(character varying(500))*
  The email address to which the report is sent.
* **enabled**                   *(integer)*
  Flag indicating whether the scheduled report is enabled.
* **query**                     *(text)*
  The SQL query that defines the report for the scheduled task.
* **outputtypes**               *(character varying(50)[])*
  Array of output types for the scheduled report.
* **schedule***                  *(character varying(500))*
  The schedule for running the report.
* **schedulehumanreadabletime** *(character varying(500))*
  Human-readable representation of the schedule time.
* **schedulename**              *(character varying(500))*
  The name associated with the schedule.
* **site_url**                  *(text)*
  The URL associated with the scheduled report.
* **hostcontextsprofileid**     *(character varying(20))*
  The profile ID associated with the host contexts.
* **hostcontextspath**          *(text)*
  The path associated with the host contexts.
* **hostcontexts**              *(json)*
  JSON data representing the subset of hosts that the report should be filtered for. If not defined the scheduled report includes all hosts the userid is allowed to see based on RBAC and data reported by the host.
* **scheduledata**              *(json)*
  JSON data containing details about the schedule.
* **excludedhosts**             *(json)*
  JSON data representing excluded hosts for the scheduled report.
* **skipmailing**               *(boolean)*
  Flag indicating whether mailing is skipped for the scheduled report.

## Table: users

User preferences and information about Mission Portal behavior.

**Columns:**

* **id**                        *(integer)*
  The primary key of the user table.
* **username**                  *(character varying(50))*
  The unique name of the user.
* **source**                    *(character varying(20))*
  The source of the user account, such as internal or external (e.g. LDAP, Active Directory).
* **last_login**                *(timestamp without time zone)*
  The timestamp of the last login of the user.
* **remember_code**             *(character varying(50))*
  The code used to remember the user login session.
* **dashboard**                 *(integer)*
  The id of the default dashboard for the user.
* **seen_tour**                 *(smallint)*
  A flag indicating whether the user has seen the tour of the Mission Portal.
* **seen_wizard**               *(smallint)*
  A flag indicating whether the user has seen the wizard of the Mission Portal.
* **never_ask_timezone_change** *(smallint)*
  A flag indicating whether the user wants to be asked about changing the timezone.
* **use_browser_time**          *(smallint)*
  A flag indicating whether the user wants to use the browser time or the server time.
* **dark_mode**                 *(smallint)*
  A flag indicating whether the user prefers the dark mode or the light mode.
* **pinned_items_version**      *(smallint)*
  This is used to add default pinned items which are added after this version.
* **additional_data**           *(jsonb)*
  A JSON object containing additional data about the user preferences and behavior.

## Table: variables_dictionary

Information about reported inventory attributes.

**Columns:**

* **id**               *(integer)*
  The unique identifier for the variable in the dictionary.
* **attribute_name**   *(character varying(200))*
  The name of the attribute represented by the variable.
* **category**         *(character varying(200))*
  The category to which the attribute belongs.
* **readonly**         *(integer)*
  Flag indicating whether the attribute is read-only.
* **type**             *(character varying(200))*
  The data type of the attribute such as string, slist, int, real.
* **convert_function** *(character varying(200))*
  The conversion function applied to the attribute such as cf_clearslist (if any).
