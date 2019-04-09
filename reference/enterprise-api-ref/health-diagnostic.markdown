---
layout: default
title: Health diagnostic API
published: true
tags: [reference, enterprise, API, reporting, URI, health]
---

This API provides access to health diagnostic information.

## Get health diagnostic status

**URI:** https://hub.cfengine.com/api/health-diagnostic/status

**Method:** GET

**Example response:**

```
{
    "hostsNeverCollected": 1,
    "hostNotRecentlyCollected": 0,
    "hostsUsingSameIdentity": 0,
    "agentNotRunRecently": 2,
    "lastAgentRunUnsuccessful": 0,
    "totalFailed": 3,
    "total": "50642"
}
```

## List of health diagnostic report categories

**URI:** https://hub.cfengine.com/api/health-diagnostic/report_ids

**Method:** GET

**Example response:**

```
[
    "hostsNeverCollected",
    "notRecentlyCollected",
    "hostsUsingSameIdentity",
    "agentNotRunRecently",
    "lastAgentRunUnsuccessful"
]
```

## Get health diagnostic report data

**URI:** https://hub.cfengine.com/api/health-diagnostic/report/:report_id

**Method:** POST

Execute user SQL query. Accepts SQL compatible with PostgreSQL database. Query is a subject to Role Base Access Control and will include data for hosts that issuing user have permissions to access. Read-only SQL is allowed.

API performance depend on the query result size, to achieve fastest results consider narrowing result set at much as possible.

**Parameters:**

* **report_id** *(string)*
    Report id.
    List of report ids you can obtain through [List of health diagnostic report categories][Health diagnostic API#List of health diagnostic report categories]
* **sortColumn** *(string)*
    Column name on which to sort results. Optional parameter.
* **sortDescending** *(boolean)*
    Sorting order. Optional parameter.
* **skip** *(integer)*
    Number of results to skip for the processed
    query. The Mission Portal uses this for pagination. Optional parameter.
* **limit**  *(integer)*
    Limit the number of results in the query.
* **hostContextInclude** *(array)*
    Includes only results that concern hosts which have all specified CFEngine contexts (class) set. Optional parameter.
* **hostContextExclude** *(array)*
    Excludes results that concern hosts which have specified CFEngine context (class) set. Hosts that have at lest one of the specified contexts set will be excluded from the results. Optional parameter.

**CURL Request Example:**
```
curl -k --user <username>:<password> -X POST \
  https://hub.cfengine.com/api/health-diagnostic/report/agentNotRunRecently \
  -H 'Content-Type: application/json' \
  -d '{"limit": 50}'
```

**Example response:**

```
{
    "data": [
        {
            "header": [
                {
                    "columnName": "key",
                    "columnType": "STRING"
                },
                {
                    "columnName": "Host name",
                    "columnType": "STRING"
                },
                {
                    "columnName": "Last report collected",
                    "columnType": "STRING"
                },
                {
                    "columnName": "Last agent local execution time",
                    "columnType": "STRING"
                }
            ],
            "query": "SELECT h.Hostkey as key,h.hostname as \"Host name\", lastreporttimestamp as \"Last report collected\", agentstatus.lastagentlocalexecutiontimestamp as \"Last agent local execution time\"  \n                            FROM vm_hosts h \n                            LEFT JOIN agentstatus  ON agentstatus.Hostkey = h.Hostkey WHERE h.HostKey IN (SELECT result.hostkey FROM (SELECT agentstatus.HostKey \n                      FROM agentstatus \n                      LEFT JOIN vm_hosts ON vm_hosts.hostkey = agentstatus.hostkey\n                      WHERE  extract(epoch from (lastReportTimeStamp::timestamp - lastagentlocalexecutiontimestamp::timestamp)) > agentexecutioninterval::int  * 1.3) AS result \n                      WHERE hostkey IS NOT NULL  AND HostKey NOT IN (SELECT hostkey FROM hosts_not_reported) AND HostKey NOT IN (SELECT Hosts_view.HostKey \n                      FROM vm_hosts Hosts_view \n                      WHERE Hosts_view.lastreporttimestamp < to_timestamp('1549559891')) AND HostKey NOT IN (SELECT SameHosts.HostKey \n                      FROM (\n                          SELECT remotehostkey as HostKey FROM lastseenhostslogs GROUP BY remotehostkey HAVING COUNT(distinct remotehostip) > 1\n                          ) AS SameHosts))",
            "queryTimeMs": 1408,
            "rowCount": 2,
            "rows": [
                [
                    "SHA=aasdsfdgddswrdfgddfdfgwerdffb86",
                    "SHA=aasdsfdgddswrdfgddfdfgwerdffb86",
                    "2019-02-27 15:16:52.987126+00",
                    "2019-02-27 15:05:56.567979+00"
                ],
                [
                    "SHA=fe7f992547addc96fe167bacd6de37681c188709ce9f01fb995f03124ef2a934",
                    "vagrant-ubuntu-trusty-64",
                    "2019-03-05 10:26:08+00",
                    "2019-03-04 08:38:30+00"
                ]
            ]
        }
    ],
    "meta": {
        "count": 1,
        "page": 1,
        "timestamp": 1551782115,
        "total": 1
    }
}
```
