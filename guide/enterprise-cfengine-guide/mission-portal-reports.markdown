---
layout: default
title: Mission Portal Reports
sorting: 100
published: true
tags: [overviews, mission portal, reports, reporting]
---

## Reports App ##

CFEngine collects a large amount of data. You can run and schedule pre-defined reports or use the [query builder](#query-builder) for your own custom reports. You can save these queries for later use, and schedule reports for specified times.

If you are familiar with SQL syntax you have the option to input your query into the interface directly. Make sure to take a look at the database schema. Please note: manual entries in the query field at the bottom of the [query builder](#query-builder) will invalidate all field selections and filters above, and vice-versa.
Results

You can narrow the amount of `hosts` to be queried with the help of filters above the displayed table. These filters are based on the same categorization you can find in the other apps.

You are also able to filter on the type of promise: user defined, system defined, or all.

#### Query Builder ####

Users not familiar with SQL syntax can easily create their own custom reports in this interface.

* Tables - Select the data tables you want include in your report first.
* Fields - Define your table columns based on your selection above.
* Filters - Filter your results.
* Group - Group your results.
* Sort - Sort your results.
* Limit - Limit the number of entries in your report. This is a recommended practice for testing your query.
* Show me the query - View and edit the SQL query directly. Please note, that editing the query directly here will invalidate your choices in the query builder interface, and changing your selections there will override your SQL query.

Please note that any queries containing the `PromiseDefinitions` table in combination with any other table in the schema will produce erroneous output without an intermediate join to the `PromiseStatusLast` table. See [SQLite Database Schema][SQLite Database Schema].

