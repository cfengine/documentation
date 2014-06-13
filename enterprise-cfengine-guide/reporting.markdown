---
layout: default
title: Reporting
sorting: 50
published: true
tags: [cfengine enterprise, user interface, mission portal]
---

CFEngine collects a large amount of data. You can run and schedule pre-defined reports or use the [query builder][Reporting#Query Builder] for your own custom reports. You can save these queries for later use, and schedule reports for specified times.

If you are familiar with SQL syntax you have the option to input your query into the interface directly. Make sure to take a look at the database schema. Please note: manual entries in the query field at the bottom of the [query builder][Reporting#Query Builder] will invalidate all field selections and filters above, and vice-versa.
Results

You can narrow the amount of `hosts` to be queried with the help of filters above the displayed table. These filters are based on the same categorization you can find in the other apps.

You are also able to filter on the type of promise: user defined, system defined, or all.

See also:

* [Reporting Architecture][Reporting Architecture]
* [SQL Queries Using the Enterprise API][SQL Queries Using the Enterprise API]
* [SQL Schema Diagram][SQL Schema Diagram]

## Query Builder ##

Users not familiar with SQL syntax can easily create their own custom reports in this interface.

* Tables - Select the data tables you want include in your report first.
* Fields - Define your table columns based on your selection above.
* Filters - Filter your results.
* Group - Group your results.
* Sort - Sort your results.
* Limit - Limit the number of entries in your report. This is a recommended practice for testing your query.
* Show me the query - View and edit the SQL query directly. Please note, that editing the query directly here will invalidate your choices in the query builder interface, and changing your selections there will override your SQL query.

### Ensure the report collection is working ###

* The reporting bundle must be in `promises.cf`. For example, the
following defines the attribute `Role` which is set to
`database_server`. You need to add it to the top-level
`bundlesequence` or in a bundle that it calls.

	```cf3
	bundle agent myreport
	{
	  vars:
		  "myrole"
		  string => "database_server",
		  meta => { "inventory", "attribute_name=Role" };
	}
	```

* The hub must be able to collect the reports from the client. TCP
port 5308 must be open and, because 3.6.0 uses TLS, should not be
proxied or otherwise intercepted. Note that bootstrapping and other
standalone client operations go from the client to the server, so the
ability to bootstrap and copy policies from the server doesn't
necessarily mean the reverse connection will work.

* Ensure that `inventory` and `report` variables and classes are not
filtered by `controls/cf_serverd.cf` in your infrastructure. The
standard configuration from the stock CFEngine packages should work.

## Define a New Single Table Report ##

1. In `Mission Portal` select the `Report` application icon on the left hand side of the screen.
2. This will bring you to the `Report builder` screen.
3. The default for what hosts to report on is `All hosts`. The hosts can be filtered under the `Filters` section at the top of the page.
4. For this tutorial leave it as `All hosts`.
5. Set which tables' data we want reports for.
6. For this tutorial select `Hosts`.
7. Select the columns from the `Hosts` table for the report.
8. For this tutorial click the `Select all` link below the column lables.
9. Leave `Filters`, `Sort`, and `Limit` at the default settings.
10. Click the orange `Run` button in the bottom right hand corner.

## Check Report Results ##

1. The report generated will show each of the selected columns across the report table's header row.
2. In this tutorial the columns being reported back should be: `Host key`, `Last report time`, `Host name`, `IP address`, `First report-time`. 
3. Each row will contain the information for an individual data record, in this case one row for each host.
4. Some of the cells in the report may provide links to drill down into more detailed information (e.g. `Host name` will provide a link to a `Host information` page).
5. It is possible to also export the report to a file.
6. Click the orange `Export` button.
7. You will then see a `Report Download` dialog.
8. `Report type` can be either `csv` or `pdf format`.
9. Leave other fields at the default values.
10. If the server's mail configuration is working properly, it is possible to email the report by checking the `Send in email` box.
11. Click `OK` to download or email the `csv` or `pdf` version of the report.
12. Once the report is generated it will be available for download or will be emailed.