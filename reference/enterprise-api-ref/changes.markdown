---
layout: default
title: Changes REST API
published: true
tags: [reference, enterprise, REST, API, reporting, changes, repairs]
---

**Changes API** allows to track changes performed by CFEngine agent in the infrastructure.

## Count changes performed by agent

**URI:** https://hub.cfengine.com/api/v2/changes/policy/count

**Method:** GET

Count changes performed by CFEngine to the infrastructure. Count can be narrowed down to specific groups of hosts, period of time or operation characteristics.

**Note:** In the environments with extensive policy and large number of clients it is recommended to narrow down the results as much as possible to achieve more precise results and faster response times. This can be done by specifying filtering parameters listed below.

* **from** *(integer)*
    Include changes performed within interval. Starting **from** unix timestamp. If not specified default value is last 24 hours.
* **to** *(integer)*
    Include changes performed within interval. Ending at **to** unix timestamp. If not specified default value is NOW.
* **include** *(array)*
    Include only nodes that have set specified context (cfengine class). Defaults to include all nodes.
* **exclude** *(array)*
    Exclude only nodes that have set specified context (cfengine class). Defaults to exclude no nodes.
* **hostkey** *(string)*
    Search results for nodes matching specified unique hostkey.
* **stackpath** *(string)*
    Search results matching specified stack path which is execution stack of the promise. Search is key insensitive. Additionally filter supports ending wildcard which can be enabled with placing '%' sign at the end.
* **promisetype** *(string)*
    Search results matching specified promise type - such as *commands*, *processes* etc. Search is key insensitive. Additionally filter supports ending wildcard which can be enabled with placing '%' sign at the end.
* **promisehandle** *(string)*
    Search results matching specified promise handle. Search is key insensitive. Additionally filter supports ending wildcard which can be enabled with placing '%' sign at the end.
* **bundlename** *(string)*
    Search results matching specified bundle name. Search is key insensitive. Additionally filter supports ending wildcard which can be enabled with placing '%' sign at the end.
* **policyfile** *(string)*
    Search results matching specified path for policy file where promise is defined. Search is key insensitive. Additionally filter supports ending wildcard which can be enabled with placing '%' sign at the end.
* **logmessages** *(string)*
    Search results matching any of the messages logged for the promise. Search is key insensitive. Additionally filter supports ending wildcard which can be enabled with placing '%' sign at the end.
* **promisees** *(string)*
    Search results matching any of the promisees specified for promise. Search is key insensitive. Additionally filter supports ending wildcard which can be enabled with placing '%' sign at the end.

**Example response:**

```
{
    "count": 49
}
```

**Output:**

* **count**
    Total count of changes performed by cf-agent that match specified filtering criteria.

**Example usage:** `Example: Count changes`

## List changes performed by agent

**URI:** https://hub.cfengine.com/api/v2/changes/policy

**Method:** GET

List changes performed by CFEngine to the infrastructure. List can be narrowed down to specific groups of hosts, period of time or operation characteristics. In case of checking only for presence of the changes it is recommended to use `Count changes performed by agent` API.

**Note:** In the environments with extensive policy and large number of clients it is recommended to narrow down the results as much as possible to achieve more precise results and faster response times. This can be done by specifying filtering parameters listed below.

**Parameters:**

* **from** *(integer)*
    Include changes performed within interval. Starting **from** unix timestamp. If not specified default value is last 24 hours.
* **to** *(integer)*
    Include changes performed within interval. Ending at **to** unix timestamp. If not specified default value is NOW.
* **include** *(array)*
    Include only nodes that have set specified context (cfengine class). Defaults to include all nodes.
* **exclude** *(array)*
    Exclude only nodes that have set specified context (cfengine class). Defaults to exclude no nodes.
* **hostkey** *(string)*
    Search results for nodes matching specified unique hostkey.
* **stackpath** *(string)*
    Search results matching specified stack path which is execution stack of the promise. Search is key insensitive. Additionally filter supports ending wildcard which can be enabled with placing '%' sign at the end.
* **promisetype** *(string)*
    Search results matching specified promise type - such as *commands*, *processes* etc. Search is key insensitive. Additionally filter supports ending wildcard which can be enabled with placing '%' sign at the end.
* **promisehandle** *(string)*
    Search results matching specified promise handle. Search is key insensitive. Additionally filter supports ending wildcard which can be enabled with placing '%' sign at the end.
* **bundlename** *(string)*
    Search results matching specified bundle name. Search is key insensitive. Additionally filter supports ending wildcard which can be enabled with placing '%' sign at the end.
* **policyfile** *(string)*
    Search results matching specified path for policy file where promise is defined. Search is key insensitive. Additionally filter supports ending wildcard which can be enabled with placing '%' sign at the end.
* **logmessages** *(string)*
    Search results matching any of the messages logged for the promise. Search is key insensitive. Additionally filter supports ending wildcard which can be enabled with placing '%' sign at the end.
* **promisees** *(string)*
    Search results matching any of the promisees specified for promise. Search is key insensitive. Additionally filter supports ending wildcard which can be enabled with placing '%' sign at the end.
* **sort** *(string)*
    Sort results by specified direction and attribute. By default sort direction is ascending, to sort as descending add '-' before attribute name. Result can be sorted by all returned fields. If not specified results are not sorted. Examples: *sort=bundlename* - sort ascending by bundlename, *sort=-promisehandle* - sort descending by promise handle.
* **count** *(integer)*
    Page size. Default 50 items.
* **page** *(integer)*
    Page number. Default 1st page.

**Example response:**

```
{
  "data": [
    {
      "bundlename": "maintain_cfe_hub_process",
      "changetime": 1430127161,
      "hostkey": "SHA=de6ba9f406a2358e9169fb27e5459687d7107a001bb0abd4dd06485a63c2e50b",
      "hostname": "hub",
      "logmessages": [
        "Unable to make file belong to an unknown user",
        "Owner of '/var/log/postgresql.log' was 0, setting to 4294967295",
        "Unknown user 'cfpostgres' in promise",
        "Unable to make file belong to an unknown user",
        "Owner of '/var/log/postgresql.log' was 0, setting to 4294967295"
      ],
      "policyfile": "/var/cfengine/inputs/update/update_processes.cf",
      "promisees": [],
      "promisehandle": "cfe_internal_maintain_cfe_hub_process_files_create_postgresql_log",
      "promiser": "/var/log/postgresql.log",
      "promisetype": "files",
      "stackpath": "/default/cfe_internal_update_processes/methods/'TAKING CARE CFE HUB PROCESSES'/default/maintain_cfe_hub_process/files/'/var/log/postgresql.log'[0]"
    },
    {
      "bundlename": "generate_repairs",
      "changetime": 1437566606,
      "hostkey": "SHA=a5c09762c561f78ee16097c0524e9efc1a2181c910cefae533f9013acd888b9f",
      "hostname": "e63dc85f0e3e",
      "logmessages": [
        "Executing 'no timeout' ... '/bin/echo 123'",
        "Completed execution of '/bin/echo 123'"
      ],
      "policyfile": "/var/cfengine/inputs/promises.cf",
      "promisees": [],
      "promisehandle": "",
      "promiser": "/bin/echo 123",
      "promisetype": "commands",
      "stackpath": "/default/generate_repairs/commands/'/bin/echo 123'[0]"
    }
  ],
  "total": 382723,
  "next": "https://hub.cfengine.com/api/v2/changes/policy/?page=2&count=2",
  "previous": null
}
```

**Output:**

* **total**
    Total number of results.
* **next**
    Link for fetching next page. Set to NULL if current page is last.
* **previous**
    Link for previous page. Set to NULL if the current page if the first.
* **data.bundlename**
    [Bundle][Bundles] name where the promise is executed.
* **data.changetime**
    Time of performing change by cf-agent to the system. Expressed as UNIT TIMESTAMP.
* **data.hostkey**
    Unique host identifier.
* **data.hostname**
    Host name locally detected on the host, configurable as `hostIdentifier` option in [Settings API][Status and Settings REST API#Get settings] and Mission Portal settings UI.
* **data.logmessages**
    List of 5 last messages generated during promise execution. Log messages can be used for tracking specific changes made by CFEngine while repairing or failing promise execution.
* **data.policyfile**
    Path to the file where the promise is located in.
* **data.promisees**
    List of [promisees][Promises] defined for the promise.
* **data.promisehandle**
    A unique id-tag string for referring promise.
* **data.promiser**
    Object affected by a promise.
* **data.promisetype**
    [Type][Promise Types] of the promise.
* **data.stackpath**
    Call stack of the promise.

**Example usage:** `Example: Show vacuum command executions`
