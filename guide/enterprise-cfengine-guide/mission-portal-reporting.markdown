---
layout: default
title: Reporting in Mission Portal
published: true
sorting: 3
---

## Ensure the report collection is working

* the reporting bundle must be in `promises.cf`. For example, the
following defines the attribute `Role` which is set to
`database_server`. You need to add it to the top-level
`bundlesequence` or in a bundle that it calls.

```
bundle agent myreport
{
  vars:
      "myrole"
      string => "database_server",
      meta => { "inventory", "attribute_name=Role" };
}
```

* the hub must be able to collect the reports from the client. TCP
port 5308 must be open and, because 3.6.0 uses TLS, should not be
proxied or otherwise intercepted. Note that bootstrapping and other
standalone client operations go from the client to the server, so the
ability to bootstrap and copy policies from the server doesn't
necessarily mean the reverse connection will work.

* ensure that `inventory` and `report` variables and classes are not
filtered by `controls/cf_serverd.cf` in your infrastructure. The
standard configuration from the stock CFEngine packages should work.

* test with `???`

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
