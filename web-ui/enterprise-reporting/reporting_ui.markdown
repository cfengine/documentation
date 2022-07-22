---
layout: default
title: Reporting UI
sorting: 50
published: true
tags: [cfengine enterprise, user interface, mission portal]
---

CFEngine collects a large amount of data. To inspect it, you can run and schedule pre-defined reports or use the [query builder][Reporting UI#Query Builder] for your own custom reports. You can save these queries for later use, and schedule reports for specified times.

If you are familiar with SQL syntax, you can input your query into the interface directly. Make sure to take a look at the database schema. Please note: manual entries in the query field at the bottom of the [query builder][Reporting UI#Query Builder] will invalidate all field selections and filters above, and vice-versa.

You can share the report with other users - either by using "Save" button, or by base64-encoding the report query into a URL. You can also provide an optional title by adding `title` parameter to the URL, like this:

```console
  HUB_URL="https://hub"
  API="/index.php/advancedreports/#/report/run?sql="
  SQL_QUERY="SELECT Hosts.HostName AS 'Host Name' FROM Hosts"
  REPORT_TITLE="Example Report"
  LINK="${HUB_URL}${API}$(echo ${SQL_QUERY} | base64)&title=$(/usr/bin/urlencode ${REPORT_TITLE})"
  echo "${LINK}"
```

```
https://hub/index.php/advancedreports/#/report/run?sql=U0VMRUNUIEhvc3RzLkhvc3ROYW1lIEFTICdIb3N0IE5hbWUnIEZST00gSG9zdHMK&title=Example%20Report
```

You can query fewer hosts with the help of filters above the displayed table. These filters are based on the same categorization you can find in the other apps.

You can also filter on the type of promise: user defined, system defined, or all.

See also:

* [Reporting Architecture][Reporting Architecture]
* [SQL Queries Using the Enterprise API][SQL Queries Using the Enterprise API]

## Query Builder ##

Users not familiar with SQL syntax can easily create their own custom reports in this interface. Please note that query builder can be [extended with your custom data][Extending Query Builder in Mission portal#How to add new table to Query builder].

* Tables - Select the data tables you want include in your report first.
    * When more than one table is selected the Query builder opens modal window to select the ([join strategy  between tables](https://www.postgresql.org/docs/current/tutorial-join.html)):
        * Main table - the main data source, other tables will be connected to it.
        * Extend main table (left join) - returns all records from the main table, and the matched records from the joined table.
        * Include only common rows (inner join) - returns records from the main table that intersect the joined table. 
        Useful for filtering, in the case where you have custom views that have pre-filtered hosts. For example, web_servers - a custom view that contains hostkeys of hosts that are web servers.
* Fields - Define your table columns based on your selection above.
* Filters - Filter your results.  Remember that unless you filter, you may be querying large data sets, so think about what you absolutely need in your report.
* Group - Group your results.  May be expensive with large data sets.
* Sort - Sort your results.  May be expensive with large data sets.
* Limit - Limit the number of entries in your report. This is a recommended practice for testing your query, and even in production it may be helpful if you don't need to see every entry.
* Show me the query - View and edit the SQL query directly. Please note, that editing the query directly here will invalidate your choices in the query builder interface, and changing your selections there will override your SQL query.

<img src="Report-Builder-3.18.0.png" alt="Report Builder" width="700px">

### Ensure the report collection is working ###

* The reporting bundle must be called from `promises.cf`. For example,
the following defines the attribute `Role` which is set to
`database_server`. You need to add it to the top-level
`bundlesequence` in `promises.cf` or in a bundle that it calls.

	```cf3
	bundle agent myreport
	{
	  vars:
		  "myrole"
		  string => "database_server",
		  meta => { "inventory", "attribute_name=Role" };
	}
	```

* note the [`meta`][Promise Types#meta] tag `inventory`

* The hub must be able to collect the reports from the client. TCP
port 5308 must be open and, because 3.6 uses TLS, should not be
proxied or otherwise intercepted. Note that bootstrapping and other
standalone client operations go from the client to the server, so the
ability to bootstrap and copy policies from the server doesn't
necessarily mean the reverse connection will work.

* Ensure that variables and classes tagged as `inventory` or `report`
are not filtered by `controls/cf_serverd.cf` in your infrastructure.
The standard configuration from the stock CFEngine packages allows
them and should work.

**Note:** The CFEngine report collection model accounts for long periods of
time when the hub is unable to collect data from remote agents. This model
preserves data recorded until it can be collected. Data (promise outcomes, etc
...) recorded by the agent during normal agent runs is stored locally until it
is collected from by the cf-hub process. At the time of collection the local
data stored on the client is cleaned up and only the last hours worth of data
remains client. It is important to understand that the time between hub
collection and number of clients that are unable to be collected from grows the
amount of data to transfer and store in the central database also grows. A
large number of clinets that have not been collected from that become available
at once can cause increased load on the hub collector and affect its
performance until it has been able to collect from all hosts.

## Define a New Single Table Report ##

1. In *Mission Portal* select the *Report* application icon on the left hand side of the screen.
2. This will bring you to the *Report builder* screen.
3. The default for what hosts to report on is *All hosts*. The hosts can be filtered under the *Filters* section at the top of the page.
4. For this tutorial leave it as *All hosts*.
5. Set which tables' data we want reports for.
6. For this tutorial select *Hosts*.
7. Select the columns from the *Hosts* table for the report.
8. For this tutorial click the *Select all* link below the column lables.
9. Leave *Filters*, *Sort*, and *Limit* at the default settings.
10. Click the orange *Run* button in the bottom right hand corner.

## Check Report Results ##

1. The report generated will show each of the selected columns across the report table's header row.
2. In this tutorial the columns being reported back should be: *Host key*, *Last report time*, *Host name*, *IP address*, *First report-time*.
3. Each row will contain the information for an individual data record, in this case one row for each host.
4. Some of the cells in the report may provide links to drill down into more detailed information (e.g. *Host name* will provide a link to a *Host information* page).
5. It is possible to also export the report to a file.
6. Click the orange *Export* button.
7. You will then see a *Report Download* dialog.
8. *Report type* can be either *csv* or *pdf format*.
9. Leave other fields at the default values.
10. If the server's mail configuration is working properly, it is possible to email the report by checking the *Send in email* box.
11. Click *OK* to download or email the *csv* or *pdf* version of the report.
12. Once the report is generated it will be available for download or will be emailed.

## Inventory Management ##

Inventory allows you to define the set of hosts to report on.

The main Inventory screen shows the current set of hosts, together with relevant information such as operating system type, kernel and memory size.

<img src="Reports-Inventory-1.png" alt="Inventory Management" width="590px">

To begin filtering, one would first select the *Filters* drop down, and then select an attribute to filter on (e.g. OS type = linux)

<img src="Reports-Inventory-2.png" alt="Inventory Management" width="590px">

After applying the filter, it may be convenient to add the attribute as one of the table columns.

<img src="Reports-Inventory-4.png" alt="Inventory Management" width="590px">

Changing the filter, or adding additional attributes for filtering, is just as easy.

<img src="Reports-Inventory-5.png" alt="Inventory Management" width="590px">

We can see here that there are no Windows machines bootstrapped to this hub.

<img src="Reports-Inventory-6.png" alt="Inventory Management" width="650px">
