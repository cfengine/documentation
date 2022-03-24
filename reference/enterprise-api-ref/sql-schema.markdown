---
layout: default
title: SQL Schema
published: true
tags: [reference, enterprise, REST, API, reporting, sql, schema]
---

CFEngine allows standardized SQL `SELECT` queries to be used with [REST API][Query REST API#Execute SQL query].
Queries can be used with following database schema.

```bash
curl -k --user admin:admin https://hub.cfengine.com/api/query -X POST -d "{ \"query\": \"SELECT Hosts.HostName, Hosts.IPAddress FROM Hosts WHERE hostname = 'hub'\"}"
```

## Table: AgentStatus

Agent status contains information about last cf-agent execution.

**Columns:**

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect data concerning same hosts.

* **AgentExecutionInterval** *(integer)*
    Estimated interval in which cf-agent is being executed, as cf-agent execution interval is expressed in cfengine context expressions (Min00_05 etc.) it can be not regular, this interval is discovered by analyzing last few cf-agent execution timestamps. Expressed in seconds.

* **LastAgentLocalExecutionTimeStamp** *(timestamp)*
    Timestamp of last cf-agent execution on the host.

* **LastAgentExecutionStatus** *(`OK`/`FAIL`)*
    cf-agent execution status. In case cf-agent will not execute within 3x `AgentExecutionInterval` from last execution, status will be set to `FAIL`. Failure may indicate cf-execd issues, or cf-agent crashes.

**Example query:**

```sql
SELECT hostkey,
       agentexecutioninterval,
       lastagentlocalexecutiontimestamp,
       lastagentexecutionstatus
FROM   agentstatus;
```

**Output:**

```
-[ RECORD 1 ]--------------------|-----------------------
hostkey                          | SHA=3b94d...
agentexecutioninterval           | 277
lastagentlocalexecutiontimestamp | 2015-03-11 12:37:39+00
lastagentexecutionstatus         | OK
-[ RECORD 2 ]--------------------|-----------------------
hostkey                          | SHA=a4dd5...
agentexecutioninterval           | 275
lastagentlocalexecutiontimestamp | 2015-03-11 12:36:36+00
lastagentexecutionstatus         | OK
-[ RECORD 3 ]--------------------|-----------------------
hostkey                          | SHA=2aab8...
agentexecutioninterval           | 284
lastagentlocalexecutiontimestamp | 2015-03-11 12:36:51+00
lastagentexecutionstatus         | OK
```

## Table: BenchmarksLog

Data from internal cf-agent monitoring as also [measurements promises][measurements].

**Columns:**

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect data concerning same hosts.

* **EventName** *(text)*
    Name of measured event.

* **StandardDeviation** *(numeric)*
    Dispersion of a set of data from its mean.

* **AverageValue** *(numeric)*
    Average value.

* **LastValue** *(numeric)*
    Last measured value.

* **CheckTimeStamp** *(timestamp)*
    Measurement time.

**Example query:**

```sql
SELECT hostkey,
       eventname,
       standarddeviation,
       averagevalue,
       lastvalue,
       checktimestamp
FROM   benchmarkslog;
```

**Output:**

```
-[ RECORD 1 ]-----|--------------------------------------------------------
hostkey           | SHA=3b94d...
eventname         | CFEngine Execution ('/var/cfengine/inputs/promises.cf')
standarddeviation | 7.659365
averagevalue      | 3.569665
lastvalue         | 1.170841
checktimestamp    | 2015-03-10 14:08:12+00
-[ RECORD 2 ]---=-|--------------------------------------------------------
hostkey           | SHA=3b94d...
eventname         | CFEngine Execution ('/var/cfengine/inputs/update.cf')
standarddeviation | 0.131094
averagevalue      | 0.422757
lastvalue         | 0.370686
checktimestamp    | 2015-03-10 14:08:11+00
-[ RECORD 3 ]-----|--------------------------------------------------------
hostkey           | SHA=3b94d...
eventname         | DBReportCollectAll
standarddeviation | 0.041025
averagevalue      | 1.001964
lastvalue         | 1.002346
checktimestamp    | 2015-03-10 14:05:20+00
```

## Table: Contexts

CFEngine contexts present on hosts at their last reported cf-agent execution.

**Columns:**

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect data concerning same hosts.

* **ContextName** *(text)*
    CFEngine [context][Classes and Decisions] set by cf-agent.

* **MetaTags** *(text[])*
    List of [meta tags][Tags for variables, classes, and bundles] set for the context.

* **ChangeTimeStamp** *(timestamp)*
    Timestamp since when context is set in its current form.
    **Note:** If any of the context attributes change, the timestamp will be updated.

**Example query:**

```sql
SELECT hostkey,
       contextname,
       metatags,
       changetimestamp
FROM   contexts;
```

**Output:**

```
-[ RECORD 1 ]---|-------------------------------------------------------
hostkey         | SHA=a4dd5...
contextname     | enterprise_3_6_5
metatags        | {inventory,attribute_name=none,source=agent,hardclass}
changetimestamp | 2015-03-11 09:50:11+00
-[ RECORD 2 ]---|-------------------------------------------------------
hostkey         | SHA=a4dd5...
contextname     | production
metatags        | {report,"Production environment"}
changetimestamp | 2015-03-11 09:50:11+00
-[ RECORD 3 ]---|-------------------------------------------------------
hostkey         | SHA=a4dd5...
contextname     | enterprise_edition
metatags        | {inventory,attribute_name=none,source=agent,hardclass}
changetimestamp | 2015-03-11 09:50:11+00
```

## Table: ContextsLog

CFEngine contexts set on hosts by CFEngine over period of time.

**Columns:**

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect data concerning same hosts.

* **ChangeTimeStamp** *(timestamp)*
    Timestamp since when context is set in its current form.
    **Note:** The statement if true till present time or newer entry claims otherwise.

* **ChangeOperation** *(`ADD`,`CHANGE`,`REMOVE`,`UNTRACKED`)*
    CFEngine uses incremental diffs to report it's state. `ChangeOperation` is a diff state describing current entry.
    * `ADD` - stands for introducing a new entry which did not exist before. In this case, new CFEngine context have been introduced.
    * `CHANGE` - stands for changing value or attribute such as `MetaTags` have changed.
    * `REMOVE` - Context have not been set.
    * `UNTRACKED` - CFEngine provides a mechanism for filtering unwanted data from being reported. `UNTRACKED` marker states that information about this context is being filtered and will not report any future information about it.

* **ContextName** *(text)*
    CFEngine [context][Classes and Decisions] set by cf-agent.

* **MetaTags** *(text[])*
    List of [meta tags][Tags for variables, classes, and bundles] set for the context.


**Example query:**

```sql
SELECT hostkey,
       changetimestamp,
       changeoperation,
       contextname,
       metatags
FROM   contextslog;
```

**Output:**

```
-[ RECORD 1 ]---|-------------------------------------------------------
hostkey         | SHA=a4dd5...
changetimestamp | 2015-03-10 13:40:20+00
changeoperation | ADD
contextname     | debian
metatags        | {inventory,attribute_name=none,source=agent,hardclass}
-[ RECORD 2 ]---|-------------------------------------------------------
hostkey         | SHA=a4dd5...
changetimestamp | 2015-03-10 14:40:20+00
changeoperation | ADD
contextname     | ipv4_192_168
metatags        | {inventory,attribute_name=none,source=agent,hardclass}
-[ RECORD 3 ]---|-------------------------------------------------------
hostkey         | SHA=a4dd5...
changetimestamp | 2015-03-10 15:40:20+00
changeoperation | ADD
contextname     | nova_3_6_5
metatags        | {inventory,attribute_name=none,source=agent,hardclass}
```

## Table: FileChangesLog

Log of changes detected to files that are set to be [monitored][files#changes] by cf-agent.

**Columns:**

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect data concerning same hosts.

* **PromiseHandle** *(text)*
    A Uniqueue id-tag string for referring promise.

* **FileName** *(text)*
    Name of the file that have changed.

* **ChangeTimeStamp** *(timestamp)*
    Timestamp when CFEngine have detected the change to the file.

* **ChangeType** *(text)*
    Type of change detected on the monitored file.
    * DIFF - change in content (with file diff)
    * S - change in file stats
    * C - change in content (based on file hash)

* **ChangeDetails** *(text[])*
    Information about changes detected to the file. Such as file stats information, file diff etc.

**Example query:**

```sql
SELECT hostkey,
       promisehandle,
       filename,
       changetimestamp,
       changetype,
       changedetails
FROM   filechangeslog;
```

**Output:**

```
-[ RECORD 1 ]---|------------------------------------------------------------
hostkey         | SHA=3b94d...
promisehandle   | my_test_promise
filename        | /tmp/app.conf
changetimestamp | 2015-03-13 13:16:10+00
changetype      | C
changedetails   | {"Content changed"}
-[ RECORD 2 ]---|------------------------------------------------------------
hostkey         | SHA=3b94d...
promisehandle   | my_test_promise
filename        | /tmp/app.conf
changetimestamp | 2015-03-13 13:16:10+00
changetype      | DIFF
changedetails   | {"-,1,loglevel = info","+,1,loglevel = debug"}
-[ RECORD 3 ]---|------------------------------------------------------------
hostkey         | SHA=3b94d...
promisehandle   | my_test_promise
filename        | /tmp/app.conf
changetimestamp | 2015-03-09 11:46:36+00
changetype      | S
changedetails   | {"Modified time: Mon Mar 9 11:37:50 -> Mon Mar 9 11:42:27"}
```

## Table: Hosts

Hosts table contains basic information about hosts managed by CFEngine.

**Columns:**

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect
    data concerning same hosts.

* **HostName** *(text)*
    Host name locally detected on the host, configurable as `hostIdentifier`
    option in [Settings API][Status and Settings REST API#Get settings] and
    Mission Portal settings UI.

* **IPAddress** *(text)*
    IP address of the host derived from the lastseen database (this is expected
    to be the IP address from which connections come from, beware NAT will cause
    multiple hosts to appear to have the same IP address).

* **LastReportTimeStamp** *(timestamp)*
    Timestamp of the most recent successful report collection.

* **FirstReportTimeStamp** *(timestamp)*
    Timestamp when the host reported to the hub for the first time, which
    indicate when the host was bootstrapped to the hub.

**Example query:**

```sql
SELECT hostkey,
       hostname,
       ipaddress,
       lastreporttimestamp,
       firstreporttimestamp
FROM   hosts;
```

**Output:**

```
-[ RECORD 1 ]--------|-----------------------
hostkey              | SHA=a4dd...
hostname             | host001
ipaddress            | 192.168.56.151
lastreporttimestamp  | 2015-03-10 14:20:20+00
firstreporttimestamp | 2015-03-10 13:40:20+00
-[ RECORD 2 ]--------|-----------------------
hostkey              | SHA=3b94...
hostname             | hub
ipaddress            | 192.168.56.65
lastreporttimestamp  | 2015-03-10 14:20:20+00
firstreporttimestamp | 2015-03-10 13:34:20+00
-[ RECORD 3 ]--------|-----------------------
hostkey              | SHA=2aab...
hostname             | host002
ipaddress            | 192.168.56.152
lastreporttimestamp  | 2015-03-10 14:20:20+00
firstreporttimestamp | 2015-03-10 13:40:20+00
```

## Table: Hosts_not_reported

Hosts_not_reported table contains information about not reported hosts.

**Columns:**

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect
    data concerning same hosts.

* **iscallcollected** *(boolean)*
    Is host call collected

* **LastReportTimeStamp** *(timestamp)*
    Timestamp of the most recent successful report collection.

* **FirstReportTimeStamp** *(timestamp)*
    Timestamp when the host reported to the hub for the first time, which
    indicate when the host was bootstrapped to the hub.

**Example query:**

```sql
SELECT hostkey,
       iscallcollected,
       lastreporttimestamp,
       firstreporttimestamp
FROM   hosts;
```

**Output:**

```
-[ RECORD 1 ]--------|-----------------------
hostkey              | SHA=a4dd...
iscallcollected      | t
lastreporttimestamp  | 2015-03-10 14:20:20+00
firstreporttimestamp | 2015-03-10 13:40:20+00
-[ RECORD 2 ]--------|-----------------------
hostkey              | SHA=3b94...
iscallcollected      | f
lastreporttimestamp  | 2015-03-10 14:20:20+00
firstreporttimestamp | 2015-03-10 13:34:20+00
-[ RECORD 3 ]--------|-----------------------
hostkey              | SHA=2aab...
iscallcollected      | f
lastreporttimestamp  | 2015-03-10 14:20:20+00
firstreporttimestamp | 2015-03-10 13:40:20+00
```

## Table: HubConnectionErrors

Networking errors encountered by cf-hub during its operation.

**Columns:**

* **HostKey** *(text)*
    Unique identifier of the host that cf-hub was connecting to.

* **CheckTimeStamp** *(timestamp)*
    Timestamp when the error occurred.

* **Message** *(text)*
    Error type / message.

* **QueryType** *(text)*
    Type of query that was intended to be sent by hub during failed connection attempt.

**Example query:**

```sql
SELECT hostkey,
       checktimestamp,
       message,
       querytype,
FROM   hubconnectionErrors;
```

**Output:**

```
-[ RECORD 1 ]--|--------------------------
hostkey        | SHA=3b94d...
checktimestamp | 2015-03-13 13:16:10+00
message        | ServerNoReply
querytype      | delta
-[ RECORD 2 ]--|--------------------------
hostkey        | SHA=3b94d...
checktimestamp | 2015-03-13 14:16:10+00
message        | InvalidData
querytype      | rebase
-[ RECORD 3 ]--|--------------------------
hostkey        | SHA=3b94d...
checktimestamp | 2015-03-13 15:16:10+00
message        | ServerAuthenticationError
querytype      | delta
```

## Table: Inventory

Inventory data

**Columns:**

* **HostKey** *(text)*
    Unique identifier of the host.

* **keyname** *(text)*
    Name of the key.
    
* **type** *(text)*
    Type of the variable. [List][Variables] of supported variable types.

* **metatags** *(text[])*
    List of [meta tags][Tags for variables, classes, and bundles] set for the variable.

* **value** *(text)*
    Variable value serialized to string.
        * List types such as: `slist`, `ilist`, `rlist` are serialized with CFEngine list format: {'value','value'}.
        * `Data` type is serialized as JSON string.

**Example query:**

```sql
SELECT hostkey,
       keyname,
       type,
       metatags,
       value
FROM   Inventory;
```

**Output:**

```
-[ RECORD 1 ]--|--------------------------
hostkey        | SHA=3b94d...
keyname        | default.sys.fqhost
type           | string
metatags       | {inventory,source=agent,"attribute_name=Host name"}
value          | host name
-[ RECORD 2 ]--|--------------------------
hostkey        | SHA=3b94d...
keyname        | default.sys.uptime
type           | int
metatags       | {inventory,source=agent,"attribute_name=Uptime minutes"}
value          | 4543
```

## Table: Inventory_new

Inventory data grouped by host

**Columns:**

* **HostKey** *(text)*
    Unique identifier of the host.

* **values** *(jsonb)*
    Inventory values presented in JSON format
    

**Example query:**

```sql
SELECT hostkey,
       values
FROM   Inventory_new;
```

**Output:**

```
-[ RECORD 1 ]--|--------------------------
hostkey        | SHA=3b94d...
values         | {"OS": "ubuntu", "OS type": "linux", "CPU model": "CPU model A10", "Host name": "SHA=aa11bb1", "OS kernel": "14.4.0-53-generic", "Interfaces": "pop, imap", "BIOS vendor": "BIOS vendor", "CFEngine ID": "SHA=aa11bb1", "CPU sockets": "229", "New OS type": "linux", "Architecture": "x86_64"}
-[ RECORD 2 ]--|--------------------------
hostkey        | SHA=5rt43...
values         | {"OS": "ubuntu", "OS type": "linux", "CPU model": "CPU model A10", "Host name": "SHA=aa11bb1", "OS kernel": "14.4.0-53-generic", "Interfaces": "pop, imap", "BIOS vendor": "BIOS vendor", "CFEngine ID": "SHA=aa11bb1", "CPU sockets": "229", "New OS type": "linux", "Architecture": "x86_64"}
```

## Table: LastSeenHosts

Information about communication between CFEngine clients. Effectively a snapshot
of each hosts lastseen database (`cf_lastseen.lmdb`, `cf-key -s`) at the time of
their last reported `cf-agent` execution.

**Columns:**

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect data concerning same hosts.

* **LastSeenDirection** *(`INCOMING`/`OUTGOING`)*
    Direction within which the connection was established.
    * `INCOMING` - host received incoming connection.
    * `OUTGOING` - host opened connection to remote host.

* **RemoteHostKey** *(text)*
    `HostKey` of the remote host.

* **RemoteHostIP** *(text)*
    IP address of the remote host.

* **LastSeenTimeStamp** *(timestamp)*
    Time when the connection was established.

* **LastSeenInterval** *(real)*
    Average time period (seconds) between connections for the given `LastSeenDirection` with the host.

**Example query:**

```sql
SELECT hostkey,
       lastseendirection,
       remotehostkey,
       remotehostip,
       lastseentimestamp,
       lastseeninterval
FROM   lastseenhosts;
```

**Output:**

```
-[ RECORD 1 ]-----|-----------------------
hostkey           | SHA=3b94d...
lastseendirection | OUTGOING
remotehostkey     | SHA=2aab8...
remotehostip      | 192.168.56.152
lastseentimestamp | 2015-03-13 12:20:45+00
lastseeninterval  | 299
-[ RECORD 2 ]-----|------------------------
hostkey           | SHA=3b94d...
lastseendirection | INCOMING
remotehostkey     | SHA=a4dd5...
remotehostip      | 192.168.56.151
lastseentimestamp | 2015-03-13 12:22:06+00
lastseeninterval  | 298
-[ RECORD 3 ]-----|------------------------
hostkey           | SHA=2aab8...
lastseendirection | INCOMING
remotehostkey     | SHA=3b94d...
remotehostip      | 192.168.56.65
lastseentimestamp | 2015-03-13 12:20:45+00
lastseeninterval  | 299
```

## Table: LastSeenHostsLogs

History of LastSeenHosts table

**Columns:**

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect data concerning same hosts.

* **LastSeenDirection** *(`INCOMING`/`OUTGOING`)*
    Direction within which the connection was established.
    * `INCOMING` - host received incoming connection.
    * `OUTGOING` - host opened connection to remote host.

* **RemoteHostKey** *(text)*
    `HostKey` of the remote host.

* **RemoteHostIP** *(text)*
    IP address of the remote host.

* **LastSeenTimeStamp** *(timestamp)*
    Time when the connection was established.

* **LastSeenInterval** *(real)*
    Average time period (seconds) between connections for the given `LastSeenDirection` with the host.

**Example query:**

```sql
SELECT hostkey,
       lastseendirection,
       remotehostkey,
       remotehostip,
       lastseentimestamp,
       lastseeninterval
FROM   LastSeenHostsLogs;
```

**Output:**

```
-[ RECORD 1 ]-----|-----------------------
hostkey           | SHA=3b94d...
lastseendirection | OUTGOING
remotehostkey     | SHA=2aab8...
remotehostip      | 192.168.56.152
lastseentimestamp | 2015-03-13 12:20:45+00
lastseeninterval  | 299
-[ RECORD 2 ]-----|------------------------
hostkey           | SHA=3b94d...
lastseendirection | INCOMING
remotehostkey     | SHA=a4dd5...
remotehostip      | 192.168.56.151
lastseentimestamp | 2015-03-13 12:22:06+00
lastseeninterval  | 298
-[ RECORD 3 ]-----|------------------------
hostkey           | SHA=2aab8...
lastseendirection | INCOMING
remotehostkey     | SHA=3b94d...
remotehostip      | 192.168.56.65
lastseentimestamp | 2015-03-13 12:20:45+00
lastseeninterval  | 299
```

## Table: MonitoringHg

Stores 1 record for each observable per host.

**Columns:**

* **host** *(text)*
    Unique host identifier. Referred to in other tables as `HostKey` to connect
    data concerning same hosts.

* **id** *(text)*
    Name of monitored metric. The handle of the measurement promise.

* **ar1** *(real)*
    Average across 66 observations.

## Table: MonitoringMgMeta

Stores 1 record for each observable per host.

**Columns:**

* **id** *(integer)*
    Unique identifier for host observable.

* **hostkey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect
    data concerning same hosts.

* **observable** *(text)*
    Name of monitored metric. The handle of the measurement promise.

* **global** *(boolean)*

* **expected_min** *(real)*
    Minimum expected value.

* **expected_max** *(real)*
    Maximum expected value.

* **unit** *(text)*
    Unit of measurement.

* **description** *(text)*
    Description of unit of measurement.

* **updatedtimestamp** *(timestamp with time zone)*
    Time when measurement sampled.

* **lastupdatedsample** *(integer)*
    Value of most recently collected measurement.

## Table: MonitoringYrMeta

Stores 1 record for each observable per host.

**Columns:**

* **id** *(integer)*
    Unique identifier for host observable.

* **hostkey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect
    data concerning same hosts.

* **observable** *(text)*
    Name of monitored metric. The handle of the measurement promise.

* **global** *(boolean)*

* **expected_min** *(real)*
    Minimum expected value.

* **expected_max** *(real)*
    Maximum expected value.

* **unit** *(text)*
    Unit of measurement.

* **description** *(text)*
    Description of unit of measurement.

* **lastupdatedsample** *(integer)*
    Value of most recently collected measurement.

## Table: PromiseExecutions

Promises executed on hosts during their last reported cf-agent run.

**Columns:**

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect data concerning same hosts.

* **PolicyFile** *(text)*
    Path to the file where the promise is located in.

* **ReleaseId** *(text)*
    Unique identifier of masterfiles version that is executed on the host.

* **PromiseHash** *(text)*
    Unique identifier of a promise. It is a hash of all promise attributes and their values.

* **NameSpace** *(text)*
    [Namespace][Namespaces] within which the promise is executed. If no namespace is set then it is set as: `default`.

* **BundleName** *(text)*
    [Bundle][Bundles] name where the promise is executed.

* **PromiseType** *(text)*
    [Type][Promise Types] of the promise.

* **Promiser** *(text)*
    Object affected by a promise.

* **StackPath** *(text)*
    Call stack of the promise.

* **PromiseHandle** *(text)*
    A unique id-tag string for referring promise.

* **PromiseOutcome** *(`KEPT`/`NOTKEPT`/`REPAIRED`)*
    Promise execution result.
    * `KEPT` - System has been found in the state as desired by the promise. CFEngine did not have to do any action to correct the state.
    * `REPAIRED` - State of the system differed from the desired state. CFEngine took successful action to correct it according to promise specification.
    * `NOTKEPT` - CFEngine has failed to converge the system according to the promise specification.

* **LogMessages** *(text[])*
    List of 5 last messages generated during promise execution. If the promise is `KEPT` the messages are not reported. Log messages can be used for tracking specific changes made by CFEngine while repairing or failing promise execution.

* **Promisees** *(text[])*
    List of [promisees][Promises] defined for the promise.

* **ChangeTimeStamp** *(timestamp)*
    Timestamp since when the promise is continuously executed by cf-agent in its current configuration and provides the same output.
    **Note:** If any of the promise dynamic attributes change, like promise outcome, log messages or the new policy version will be rolled out. This timestamp will be changed.

**Example query:**

```sql
SELECT hostkey,
       policyfile,
       releaseid,
       promisehash,
       namespace,
       bundlename,
       promisetype,
       promiser,
       stackpath,
       promisehandle,
       promiseoutcome,
       logmessages,
       promisees,
       changetimestamp
FROM   softwareupdates;
```

**Output:**

```
-[ RECORD 1 ]---|---------------------------------------------------------
hostkey         | SHA=a4dd5...
policyfile      | /var/cfengine/inputs/inventory/any.cf
releaseid       | 05c0cc909d6709d816521d6cedbc4508894cc497
promisehash     | fd6d5e40b734e35d9e8b2ed071dfe390f23148053adaae3dbb936...
namespace       | default
bundlename      | inventory_autorun
promisetype     | methods
promiser        | mtab
stackpath       | /default/inventory_autorun/methods/'mtab'[0]
promisehandle   | cfe_internal_autorun_inventory_mtab
promiseoutcome  | KEPT
logmessages     | {}
promisees       | {}
changetimestamp | 2015-03-12 10:20:18+00
-[ RECORD 2 ]---|---------------------------------------------------------
hostkey         | SHA=a4dd5...
policyfile      | /var/cfengine/inputs/promises.cf
releaseid       | 05c0cc909d6709d816521d6cedbc4508894cc497
promisehash     | 925b04453ef86ff2e43228a5ca5d56dc4d69ddf12378d6fdba28b...
namespace       | default
bundlename      | service_catalogue
promisetype     | methods
promiser        | security
stackpath       | /default/service_catalogue/methods/'security'[0]
promisehandle   | service_catalogue_change_management
promiseoutcome  | KEPT
logmessages     | {}
promisees       | {goal_infosec,goal_compliance}
changetimestamp | 2015-03-12 10:20:18+00
-[ RECORD 3 ]---|---------------------------------------------------------
hostkey         | SHA=3b94d...
policyfile      | /var/cfengine/inputs/lib/3.6/bundles.cf
releaseid       | 05c0cc909d6709d816521d6cedbc4508894cc497
promisehash     | 47f64d43f21bc6162b4f21bf385e715535617eebc649b259ebaca...
namespace       | default
bundlename      | logrotate
promisetype     | files
promiser        | /var/cfengine/cf3.hub.runlog
stackpath       | /default/cfe_internal_management/files/'any'/default/...
promisehandle   |
promiseoutcome  | REPAIRED
logmessages     | {"Rotating files '/var/cfengine/cf3.hub.runlog'"}
promisees       | {}
changetimestamp | 2015-03-12 14:52:36+00
```

## Table: PromiseExecutionsLog

**This table was deprecated in 3.7.0. It is no longer used.**

Promise status / outcome changes over period of time.

**Columns:**

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect data concerning same hosts.

* **ChangeTimeStamp** *(timestamp)*
    Timestamp when the promise state or outcome changed.
    **Note:** The statement if true till present time or newer entry claims otherwise.

* **ChangeOperation** *(`ADD`,`CHANGE`,`REMOVE`,`UNTRACKED`)*
    CFEngine uses incremental diffs to report it's state. `ChangeOperation` is a diff state describing current entry.
    * `ADD` - stands for introducing a new entry which did not exist at last execution. In this case, new promise executed, or the promise was not executed at previous cf-agent run.
    * `CHANGE` - stands for changing value or attribute such as `PromiseOutcome`, `LogMessages` or `ReleaseId` in case of new policy rollout.
    * `REMOVE` - Promise was not executed last time, but it was executed previously. This is a common report for promises that have been removed from policy at some point, or they are executed only periodically (like once a hour, day etc.).
    * `UNTRACKED` - CFEngine provides a mechanism for filtering unwanted data from being reported. `UNTRACKED` marker states that information is being filtered and will not report any future information about it.

* **PolicyFile** *(text)*
    Path to the file where the promise is located in.

* **ReleaseId** *(text)*
    Unique identifier of masterfiles version that is executed in the host.

* **PromiseHash** *(text)*
    Unique identifier of a promise. It is a hash of all promise attributes and their values.

* **NameSpace** *(text)*
    [Namespace][Namespaces] within which the promise is executed. If no namespace is set then it is set as: `default`.

* **BundleName** *(text)*
    [Bundle][Bundles] name where the promise is executed.

* **PromiseType** *(text)*
    [Type][Promise Types] of the promise.

* **Promiser** *(text)*
    Object affected by a promise.

* **StackPath** *(text)*
    Call stack of the promise.

* **PromiseHandle** *(text)*
    A unique id-tag string for referring promise.

* **PromiseOutcome** *(`KEPT`/`NOTKEPT`/`REPAIRED`)*
    Promise execution result.
    * `KEPT` - System has been found in the state as desired by the promise. CFEngine did not have to do any action to correct the state.
    * `REPAIRED` - State of the system differed from the desired state. CFEngine took successful action to correct it according to promise specification.
    * `NOTKEPT` - CFEngine has failed to converge the system according to the promise specification.

* **LogMessages** *(text[])*
    List of 5 last messages generated during promise execution. If the promise is `KEPT` the messages are not reported. Log messages can be used for tracking specific changes made by CFEngine while repairing or failing promise execution.

* **Promisees** *(text[])*
    List of [promisees][Promises] defined for the promise.

**Example query:**

```sql
SELECT hostkey,
       changetimestamp,
       changeoperation,
       policyfile,
       releaseid,
       promisehash,
       namespace,
       bundlename,
       promisetype,
       promiser,
       stackpath,
       promisehandle,
       promiseoutcome,
       logmessages,
       promisees
FROM   promiseexecutionslog;
```

**Output:**

```
-[ RECORD 1 ]---|--------------------------------------------------
hostkey         | SHA=a4dd5...
changetimestamp | 2015-03-11 09:50:11+00
changeoperation | ADD
policyfile      | /var/cfengine/inputs/sketches/meta/api-runfile.cf
releaseid       | 05c0cc909d6709d816521d6cedbc4508894cc497
promisehash     | 48bc...
namespace       | default
bundlename      | cfsketch_run
promisetype     | methods
promiser        | cfsketch_g
stackpath       | /default/cfsketch_run/methods/'cfsketch_g'[0]
promisehandle   |
promiseoutcome  | KEPT
logmessages     | {}
promisees       | {}
-[ RECORD 2 ]---|--------------------------------------------------
hostkey         | SHA=3b94d...
changetimestamp | 2015-03-17 08:55:38+00
changeoperation | ADD
policyfile      | /var/cfengine/inputs/inventory/any.cf
releaseid       | 05c0cc909d6709d816521d6cedbc4508894cc497
promisehash     | 6eef8...
namespace       | default
bundlename      | inventory_autorun
promisetype     | methods
promiser        | disk
stackpath       | /default/inventory_autorun/methods/'disk'[0]
promisehandle   | cfe_internal_autorun_disk
promiseoutcome  | KEPT
logmessages     | {}
promisees       | {}
-[ RECORD 3 ]---|--------------------------------------------------
hostkey         | SHA=3b94d...
changetimestamp | 2015-03-10 13:43:28+00
changeoperation | CHANGE
policyfile      | /var/cfengine/inputs/inventory/any.cf
releaseid       | 05c0cc909d6709d816521d6cedbc4508894cc497
promisehash     | fd6d5...
namespace       | default
bundlename      | inventory_autorun
promisetype     | methods
promiser        | mtab
stackpath       | /default/inventory_autorun/methods/'mtab'[0]
promisehandle   | cfe_internal_autorun_inventory_mtab
promiseoutcome  | KEPT
logmessages     | {}
promisees       | {}
```



## Table: PromiseLog

History of promises executed on hosts.

**Columns:**

* **id** *(integer)*

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect data concerning same hosts.

* **ChangeTimeStamp** *(timestamp)*
    The GMT time on the host when this state was first perceived.

    **Note causes of change:**
    - A change in the promise signature/hash for example, altering the promise
      handle, promisees, or moving the promise to a different bundle
    - A change in the policy releaseId (cf_promises_release_id)
    - A change in promise outcome

* **PolicyFile** *(text)*
    Path to the file where the promise is located in.

* **ReleaseId** *(text)*
    Unique identifier of masterfiles version that is executed on the host.

* **PromiseHash** *(text)*
    Unique identifier of a promise. It is a hash of all promise attributes and their values.

* **NameSpace** *(text)*
    [Namespace][Namespaces] within which the promise is executed. If no namespace is set then it is set as: `default`.

* **BundleName** *(text)*
    [Bundle][Bundles] name where the promise is executed.

* **PromiseType** *(text)*
    [Type][Promise Types] of the promise.

* **Promiser** *(text)*
    Object affected by a promise.

* **StackPath** *(text)*
    Call stack of the promise.

* **PromiseHandle** *(text)*
    A unique id-tag string for referring promise.

* **PromiseOutcome** *(`KEPT`/`NOTKEPT`/`REPAIRED`)*
    Promise execution result.
    * `KEPT` - System has been found in the state as desired by the promise. CFEngine did not have to do any action to correct the state.
    * `REPAIRED` - State of the system differed from the desired state. CFEngine took successful action to correct it according to promise specification.
    * `NOTKEPT` - CFEngine has failed to converge the system according to the promise specification.

* **LogMessages** *(text[])*
    List of 5 last messages generated during promise execution. If the promise is `KEPT` the messages are not reported. Log messages can be used for tracking specific changes made by CFEngine while repairing or failing promise execution.

* **Promisees** *(text[])*
    List of [promisees][Promises] defined for the promise.

**Example query:**

```sql
SELECT hostkey,
       policyfile,
       releaseid,
       promisehash,
       namespace,
       bundlename,
       promisetype,
       promiser,
       stackpath,
       promisehandle,
       promiseoutcome,
       logmessages,
       promisees,
       changetimestamp
FROM   promiselog;
```

**Output:**

```
-[ RECORD 1 ]---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
hostkey         | SHA=70138d580b9fd292ff856746df2fe7f9ded29db9ffca0c4d83acbbb97cde4d42
policyfile      | /var/cfengine/inputs/lib/bundles.cf
releaseid       | f90866033a826aa05cf10fdc8d34a532a9cd465b
promisehash     | 04659a0501f471eb1794cead6cd7a3291b78dcb195063821a7dcb4dbe7f7f804
namespace       | default
bundlename      | prunedir
promisetype     | files
promiser        | /var/cfengine/outputs
stackpath       | /default/cfe_internal_management/methods/'CFEngine_Internals'/default/cfe_internal_core_main/methods/'any'/default/cfe_internal_log_rotation/methods/'Prune old log files'/default/prunedir/files/'/var/cfengine/output
s'[1]
promisehandle   |
promiseoutcome  | REPAIRED
logmessages     | {"Deleted file '/var/cfengine/outputs/cf_demohub_a10042_cfengine_com__1535846669_Sun_Sep__2_00_04_29_2018_0x7f4da3549700'"}
promisees       | {}
changetimestamp | 2018-10-02 00:04:52+00
```

## Table: Software

Software packages installed (according to local package manager) on the hosts.
More information about CFEngine and package management can be found [here][packages].

**Columns:**

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect data concerning same hosts.

* **SoftwareName** *(text)*
    Name of installed software package.

* **SoftwareVersion** *(text)*
    Software package version.

* **SoftwareArchitecture** *(text)*
    Architecture.

* **ChangeTimeStamp** *(timestamp)*
    Timestamp when the package was discovered / installed on the host.

**Example query:**

```sql
SELECT hostkey,
       softwarename,
       softwareversion,
       softwarearchitecture,
       changetimestamp
FROM   software;
```

**Output:**

```
-[ RECORD 1 ]--------|-----------------------
hostkey              | SHA=a4dd5...
softwarename         | libgssapi-krb5-2
softwareversion      | 1.12+dfsg-2ubuntu4.2
softwarearchitecture | default
changetimestamp      | 2015-03-12 10:20:18+00
-[ RECORD 2 ]--------|-----------------------
hostkey              | SHA=a4dd5...
softwarename         | whiptail
softwareversion      | 0.52.15-2ubuntu5
softwarearchitecture | default
changetimestamp      | 2015-03-12 10:20:18+00
-[ RECORD 3 ]--------|-----------------------
hostkey              | SHA=a4dd5...
softwarename         | libruby1.9.1
softwareversion      | 1.9.3.484-2ubuntu1.2
softwarearchitecture | default
changetimestamp      | 2015-03-12 10:20:18+00
```

## Table: SoftwareUpdates

Patches available for installed packages on the hosts (as reported by local package manager).
The most up to date patch will be listed.

**Columns:**

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect data concerning same hosts.

* **PatchName** *(text)*
    Name of the software.

* **PatchVersion** *(text)*
    Patch version.

* **PatchArchitecture** *(text)*
    Architecture of the patch.

* **PatchReportType** *(`INSTALLED`/`AVAILABLE`)*
    Patch status (`INSTALLED` status is specific only to SUSE Linux).

* **ChangeTimeStamp** *(timestamp)*
    Timestamp when the new patch / version was discovered as available on the host.

**Example query:**

```sql
SELECT hostkey,
       patchname,
       patchversion,
       patcharchitecture,
       patchreporttype,
       changetimestamp
FROM   softwareupdates;
```

**Output:**

```
-[ RECORD 1 ]-----|------------------------
hostkey           | SHA=a4dd5...
patchname         | libelf1
patchversion      | 0.158-0ubuntu5.2
patcharchitecture | default
patchreporttype   | AVAILABLE
changetimestamp   | 2015-03-12 10:20:18+00
-[ RECORD 2 ]-----|------------------------
hostkey           | SHA=a4dd5...
patchname         | libisccfg90
patchversion      | 1:9.9.5.dfsg-3ubuntu0.2
patcharchitecture | default
patchreporttype   | AVAILABLE
changetimestamp   | 2015-03-12 10:20:18+00
-[ RECORD 3 ]-----|------------------------
hostkey           | SHA=a4dd5...
patchname         | libc6-dev
patchversion      | 2.19-0ubuntu6.6
patcharchitecture | default
patchreporttype   | AVAILABLE
changetimestamp   | 2015-03-12 10:20:18+00
```

## Table: SoftwareLog
Software packages installed / deleted over period of time.
More information about CFEngine and package management can be found [here][packages].

**Columns:**

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect data concerning same hosts.

* **ChangeTimeStamp** *(timestamp)*
    Timestamp when the package state was discovered on the host.
    **Note:** The statement if true till present time or newer entry claims otherwise.

* **ChangeOperation** *(`ADD`,`REMOVE`)*
    CFEngine uses incremental diffs to report it's state. `ChangeOperation` is a diff state describing current entry.
    * `ADD` - New package have been detected / installed. Package upgrate is considered as installing a new package with a different version.
    * `REMOVE` - Package have been detected to be removed / uninstalled. During upgrate older version of the package is removed and reported as so.

* **SoftwareName** *(text)*
    Name of installed software package.

* **SoftwareVersion** *(text)*
    Software package version.

* **SoftwareArchitecture** *(text)*
    Architecture.

**Example query:**

```sql
SELECT hostkey,
       changetimestamp,
       changeoperation,
       softwarename,
       softwareversion,
       softwarearchitecture
FROM   softwarelog;
```

**Output:**

```
-[ RECORD 1 ]--------|-----------------------
hostkey              | SHA=3b94d...
changetimestamp      | 2015-03-10 13:38:14+00
changeoperation      | ADD
softwarename         | libgssapi-krb5-2
softwareversion      | 1.12+dfsg-2ubuntu4.2
softwarearchitecture | default
-[ RECORD 2 ]--------|-----------------------
hostkey              | SHA=3b94d...
changetimestamp      | 2015-03-10 13:38:14+00
changeoperation      | ADD
softwarename         | whiptail
softwareversion      | 0.52.15-2ubuntu5
softwarearchitecture | default
-[ RECORD 3 ]--------|-----------------------
hostkey              | SHA=3b94d...
changetimestamp      | 2015-03-10 13:38:14+00
changeoperation      | ADD
softwarename         | libruby1.9.1
softwareversion      | 1.9.3.484-2ubuntu1.2
softwarearchitecture | default
```

## Table: SoftwareUpdatesLog

**This table was deprecated in 3.7.0. It is no longer used.**

Patches available for installed packages on the hosts (as reported by local package manager) over period of time.

**Columns:**

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect data concerning same hosts.

* **ChangeTimeStamp** *(timestamp)*
    Timestamp when the patch state was discovered on the host.
    **Note:** The statement if true till present time or newer entry claims otherwise.

* **ChangeOperation** *(`ADD`,`REMOVE`)*
    CFEngine uses incremental diffs to report it's state. `ChangeOperation` is a diff state describing current entry.
    * `ADD` - New patch have been detected. This is a common in case of release of new patch version or new package was installed that have an upgrate available.
    * `REMOVE` - Patch is not longer available. Patch may be replaced with newer version, or installed package have been upgrated.
    **Note:** CFEngine reports only the most up to date version available.

* **PatchName** *(text)*
    Name of the software.

* **PatchVersion** *(text)*
    Patch version.

* **PatchArchitecture** *(text)*
    Architecture of the patch.

* **PatchReportType** *(`INSTALLED`/`AVAILABLE`)*
    Patch status (`INSTALLED` status is specific only to SUSE Linux).

**Example query:**

```sql
SELECT hostkey,
       changetimestamp,
       changeoperation,
       patchname,
       patchversion,
       patcharchitecture,
       patchreporttype
FROM   softwareupdateslog;
```

**Output:**

```
-[ RECORD 1 ]-----|------------------------
hostkey           | SHA=3b94d...
changetimestamp   | 2015-03-10 13:38:14+00
changeoperation   | ADD
patchname         | libelf1
patchversion      | 0.158-0ubuntu5.2
patcharchitecture | default
patchreporttype   | AVAILABLE
-[ RECORD 2 ]-----|------------------------
hostkey           | SHA=3b94d...
changetimestamp   | 2015-03-10 13:38:14+00
changeoperation   | ADD
patchname         | libisccfg90
patchversion      | 1:9.9.5.dfsg-3ubuntu0.2
patcharchitecture | default
patchreporttype   | AVAILABLE
-[ RECORD 3 ]-----|------------------------
hostkey           | SHA=3b94d...
changetimestamp   | 2015-03-10 13:38:14+00
changeoperation   | ADD
patchname         | libc6-dev
patchversion      | 2.19-0ubuntu6.6
patcharchitecture | default
patchreporttype   | AVAILABLE
```

## Table: Status

Statuses of report collection. cf-hub records all collection attempts and whether they are FAILEDC or CONSUMED. CONSUMED means next one will be delta. FAILEDC means next one will be REBASE.

**Columns:**

* **host** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect data concerning same hosts.

* **ts** *(timestamp)*
    Timestamp of last data provided by client during report collection. This is used by delta queries to request a start time.

* **status** *(`FAILEDC`,`CONSUMED`)*
    CFEngine uses incremental diffs to report it's state. `ChangeOperation` is a diff state describing current entry.
    * `FAILEDC` - New patch have been detected. This is a common in case of release of new patch version or new package was installed that have an upgrate available.
    * `CONSUMED` - Patch is not longer available. Patch may be replaced with newer version, or installed package have been upgrated.
    **Note:** CFEngine reports only the most up to date version available.

* **lstatus** *(text)*
    Deprecated

* **type** *(text)*
    Deprecated

* **who** *(integer)*
    Deprecated

* **whr** *integer*
    Deprecated

**Example query:**

```sql
SELECT hostkey,
       changetimestamp,
       changeoperation,
       patchname,
       patchversion,
       patcharchitecture,
       patchreporttype
FROM   softwareupdateslog;
```

**Output:**

```
-[ RECORD 1 ]-----|------------------------
hostkey           | SHA=3b94d...
changetimestamp   | 2015-03-10 13:38:14+00
changeoperation   | ADD
patchname         | libelf1
patchversion      | 0.158-0ubuntu5.2
patcharchitecture | default
patchreporttype   | AVAILABLE
-[ RECORD 2 ]-----|------------------------
hostkey           | SHA=3b94d...
changetimestamp   | 2015-03-10 13:38:14+00
changeoperation   | ADD
patchname         | libisccfg90
patchversion      | 1:9.9.5.dfsg-3ubuntu0.2
patcharchitecture | default
patchreporttype   | AVAILABLE
-[ RECORD 3 ]-----|------------------------
hostkey           | SHA=3b94d...
changetimestamp   | 2015-03-10 13:38:14+00
changeoperation   | ADD
patchname         | libc6-dev
patchversion      | 2.19-0ubuntu6.6
patcharchitecture | default
patchreporttype   | AVAILABLE
```


## Table: Variables

Variables and their values set on hosts at their last reported cf-agent execution.

**Columns:**

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect data concerning same hosts.

* **NameSpace** *(text)*
    [Namespace][Namespaces] within which the variable is set. If no namespace is set then it is set as: `default`.

* **Bundle** *(text)*
    [Bundle][Bundles] name where the variable is set.

* **VariableName** *(text)*
    Name of the variable.

* **VariableValue** *(text)*
    Variable value serialized to string.
    * List types such as: `slist`, `ilist`, `rlist` are serialized with CFEngine list format: {'value','value'}.
    * `Data` type is serialized as JSON string.

* **VariableType** *(text)*
    Type of the variable. [List][Variables] of supported variable types.

* **MetaTags** *(text[])*
    List of [meta tags][Tags for variables, classes, and bundles] set for the variable.

* **ChangeTimeStamp** *(timestamp)*
    Timestamp since when variable is set in its current form.
    **Note:** If any of variable attributes change such as its `VariableValue` or `Bundle`, the timestamp will be updated.

**Example query:**

```sql
SELECT hostkey,
       namespace,
       bundle,
       variablename,
       variablevalue,
       variabletype,
       metatags,
       changetimestamp
FROM   variables;
```

**Output:**

```
-[ RECORD 1 ]---|-------------------------------------------------------------
hostkey         | SHA=a4dd5...
namespace       | default
bundle          | cfe_autorun_inventory_memory
variablename    | total
variablevalue   | 490.00
variabletype    | string
metatags        | {source=promise,inventory,"attribute_name=Memory size (MB)"}
changetimestamp | 2015-03-11 09:51:41+00
-[ RECORD 2 ]---|-------------------------------------------------------------
hostkey         | SHA=a4dd5...
namespace       | default
bundle          | cfe_autorun_inventory_listening_ports
variablename    | ports
variablevalue   | {'22','111','5308','38854','50241'}
variabletype    | slist
metatags        | {source=promise,inventory,"attribute_name=Ports listening"}
changetimestamp | 2015-03-11 09:51:41+00
-[ RECORD 3 ]---|-------------------------------------------------------------
hostkey         | SHA=a4dd5...
namespace       | default
bundle          | cfe_autorun_inventory_memory
variablename    | free
variablevalue   | 69.66
variabletype    | string
metatags        | {source=promise,report}
changetimestamp | 2015-03-11 14:27:12+00
```

## Table: Variables_dictionary

Inventory attributes, these data are using in [List of inventory attributes API][Inventory API#List of inventory attributes]

**Columns:**

* **Id** *(integer)*	
    Auto incremental ID	 
* **Attribute_name** *(text)*
    Attribute name
* **Category** *(text)* *(`Hardware`,`Software`,`Network`, `Security`, `User defined`)*
    Attribute category
* **Readonly** *(integer)* *(`0`,`1`)*
    Is attribute readonly
* **Type** *(text)*
    Type of the attribute. [List][Variables] of supported variable types.
* **convert_function** *(text)*
    Convert function. Emp.: `cf_clearSlist` - to transform string like `{"1", "2"}` to `1, 2`
* **keyname** *(text)*
    Key name
* **Enabled** *(integer)* *(`0`,`1`)*
    Is attribute enabled for the API   

**Example query:**

```sql
SELECT attribute_name,
       category,
       readonly,
       type,
       convert_function,
       enabled
FROM   variables_dictionary;
```

**Output:**

```
-[ RECORD 1 ]---|-----------------------------------------------------
attribute_name  | Architecture
category        | Software
readonly        | 1
type            | string
convert_function| 
enabled         | 1
-[ RECORD 2 ]---|-----------------------------------------------------
attribute_name  | IPv4 addresses
category        | Network
readonly        | 1
type            | slist
convert_function| cf_clearSlist
enabled         | 1
```

## Table: VariablesLog

CFEngine variables set on hosts by CFEngine over period of time.

**Columns:**

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect data concerning same hosts.

* **ChangeTimeStamp** *(timestamp)*
    Timestamp since when variable is set in its current form.
    **Note:** The statement if true till present time or newer entry claims otherwise.

* **ChangeOperation** *(`ADD`,`CHANGE`,`REMOVE`,`UNTRACKED`)*
    CFEngine uses incremental diffs to report it's state. `ChangeOperation` is a diff state describing current entry.
    * `ADD` - stands for introducing a new entry which did not exist before. In this case, new CFEngine variable have been introduced.
    * `CHANGE` - stands for changing value or attribute such as `VariableValue` or `MetaTags` have changed.
    * `REMOVE` - Variable have not been set.
    * `UNTRACKED` - CFEngine provides a mechanism for filtering unwanted data from being reported. `UNTRACKED` marker states that information is being filtered and will not report any future information about it.

* **NameSpace** *(text)*
    [Namespace][Namespaces] within which the variable is set. If no namespace is set then it is set as: `default`.

* **Bundle** *(text)*
    [Bundle][Bundles] name where the variable is set.

* **VariableName** *(text)*
    Name of the variable.

* **VariableValue** *(text)*
    Variable value serialized to string.
    * List types such as: `slist`, `ilist`, `rlist` are serialized with CFEngine list format: {'value','value'}.
    * `Data` type is serialized as JSON string.

* **VariableType** *(text)*
    Type of the variable. [List][Variables] of supported variable types.

* **MetaTags** *(text[])*
    List of [meta tags][Tags for variables, classes, and bundles] set for the variable.

**Example query:**

```sql
SELECT hostkey,
       changetimestamp,
       changeoperation,
       namespace,
       bundle,
       variablename,
       variablevalue,
       variabletype,
       metatags
FROM   variableslog;
```

**Output:**

```
-[ RECORD 1 ]---|-----------------------------------------------------
hostkey         | SHA=2aab8...
changetimestamp | 2015-03-10 13:43:00+00
changeoperation | CHANGE
namespace       | default
bundle          | mon
variablename    | av_cpu
variablevalue   | 0.06
variabletype    | string
metatags        | {monitoring,source=environment}
-[ RECORD 2 ]---|-----------------------------------------------------
hostkey         | SHA=2aab8...
changetimestamp | 2015-03-10 13:40:20+00
changeoperation | ADD
namespace       | default
bundle          | sys
variablename    | arch
variablevalue   | x86_64
variabletype    | string
metatags        | {inventory,source=agent,attribute_name=Architecture}
-[ RECORD 3 ]---|-----------------------------------------------------
hostkey         | SHA=2aab8...
changetimestamp | 2015-03-10 13:43:00+00
changeoperation | CHANGE
namespace       | default
bundle          | mon
variablename    | av_diskfree
variablevalue   | 67.01
variabletype    | string
metatags        | {monitoring,source=environment}
```
## Table: v_hosts

V_hosts table contains information about hosts.

**Columns:**

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect
    data concerning same hosts.

* **iscallcollected** *(boolean)*
    Is host call collected

* **LastReportTimeStamp** *(timestamp)*
    Timestamp of the most recent successful report collection.

* **FirstReportTimeStamp** *(timestamp)*
    Timestamp when the host reported to the hub for the first time, which
    indicate when the host was bootstrapped to the hub.

**Example query:**

```sql
SELECT hostkey,
       iscallcollected,
       lastreporttimestamp,
       firstreporttimestamp
FROM   hosts;
```

**Output:**

```
-[ RECORD 1 ]--------|-----------------------
hostkey              | SHA=a4dd...
iscallcollected      | t
lastreporttimestamp  | 2015-03-10 14:20:20+00
firstreporttimestamp | 2015-03-10 13:40:20+00
-[ RECORD 2 ]--------|-----------------------
hostkey              | SHA=3b94...
iscallcollected      | f
lastreporttimestamp  | 2015-03-10 14:20:20+00
firstreporttimestamp | 2015-03-10 13:34:20+00
-[ RECORD 3 ]--------|-----------------------
hostkey              | SHA=2aab...
iscallcollected      | f
lastreporttimestamp  | 2015-03-10 14:20:20+00
firstreporttimestamp | 2015-03-10 13:40:20+00
```

## Table: vm_hosts

vm_hosts table contains basic information about hosts managed by CFEngine. 
In this table data are cached what gives a better query performance

**Columns:**

* **HostKey** *(text)*
    Unique host identifier. All tables can be joined by `HostKey` to connect
    data concerning same hosts.

* **HostName** *(text)*
    Host name locally detected on the host, configurable as `hostIdentifier`
    option in [Settings API][Status and Settings REST API#Get settings] and
    Mission Portal settings UI.

* **IPAddress** *(text)*
    IP address of the host derived from the lastseen database (this is expected
    to be the IP address from which connections come from, beware NAT will cause
    multiple hosts to appear to have the same IP address).

* **LastReportTimeStamp** *(timestamp)*
    Timestamp of the most recent successful report collection.

* **FirstReportTimeStamp** *(timestamp)*
    Timestamp when the host reported to the hub for the first time, which
    indicate when the host was bootstrapped to the hub.

**Example query:**

```sql
SELECT hostkey,
       hostname,
       ipaddress,
       lastreporttimestamp,
       firstreporttimestamp
FROM   hosts;
```

**Output:**

```
-[ RECORD 1 ]--------|-----------------------
hostkey              | SHA=a4dd...
hostname             | host001
ipaddress            | 192.168.56.151
lastreporttimestamp  | 2015-03-10 14:20:20+00
firstreporttimestamp | 2015-03-10 13:40:20+00
-[ RECORD 2 ]--------|-----------------------
hostkey              | SHA=3b94...
hostname             | hub
ipaddress            | 192.168.56.65
lastreporttimestamp  | 2015-03-10 14:20:20+00
firstreporttimestamp | 2015-03-10 13:34:20+00
-[ RECORD 3 ]--------|-----------------------
hostkey              | SHA=2aab...
hostname             | host002
ipaddress            | 192.168.56.152
lastreporttimestamp  | 2015-03-10 14:20:20+00
firstreporttimestamp | 2015-03-10 13:40:20+00
```
