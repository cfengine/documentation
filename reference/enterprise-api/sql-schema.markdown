---
layout: default
title: SQL Schema
categories: [Reference, Enterprise API, SQL Schema]
published: true
alias: reference-enterprise-api-sql-schema.html
tags: [reference, enterprise, REST, API, reporting, sql, schema]
---

CFEngine allows all standardized SQL `SELECT` constructs to query, with the 
following additions:

* `TIMESTAMP_UNIX()` - seconds elapsed since 1970
* `TIMESTAMP_UNIX_DAYS()` - days elapsed since 1970

These are added to avoid use of non-portable SQL date/time functions.

## Examples

* Group LAST status of promises in bundle "ntp" in hosts matching class 
"ntp_server".

The result should include a list of the promises in the bundle, together with 
counts of the four statuses (kept, repaired, not kept, unknown).

```
    SELECT Status, Count(*)
      FROM PromiseStatusLast
     WHERE Bundle=ntp_server AND Context=ntp_server
     GROUP BY Status
```

* Group all file changes by file name occurred between a from and to 
time-stamp on context "ubuntu".

There should be counters on how many total occurrences and distinct host occurrences found.

```
    SELECT FileName, Count(*), Distinct(Count(HostKey))
      FROM FileChanges
     WHERE ChangeTime < TO AND ChangeTime > FROM AND Context=ubuntu
     GROUP BY FileName
```

* List all package names and versions, with the host ip address and OS that 
has it.

```
    SELECT 
         software.name, 
         software.version, 
         variables.name, 
         variables.value 
    FROM software 
    JOIN variables 
    WHERE 
         variables.name='ipv4' 
         AND variables.value='172.20.10.41' 
         AND variables.value='os' 
         AND variables.value='linux';
```

## Inventory

### Hosts

| HostKey | HostName | IPAddress | ReportTimeStamp | FirstReportTimeStamp |
|--------|---------|----------|----------------|---------------------|
|12377 | stage.cfengine.com  | 10.0.0.19 | 123213 | 123 |
|18843 | dev.test.cfengine.com  | 10.0.0.29 | 2131212 | 123 |

### Contexts

| HostKey | ContextName | DefineTimeStamp |
|----------|----------------|---------------------|
| 12321 | ubuntu  | 123214 |
| 42142 | am_policy_hub  | 123123 |
| 43432 | suse  | 123123 |
| 42343 | cfengine_3  | 2133123 |

### Variables

**Note**: Lists are split into multiple rows.

| HostKey| NameSpace | Bundle | VariableName | VariableValue | VariableType |
|--------|---------|----------|----------------|-----------|----------|
| 12332 |  | sys | hostname | host1  | string |
| 34234 | cfe_system | def | acl | 192.168.122.1/16  | string list |
| 43242 | cfe_system| def | acl | 192.168.121.1/32  | string list |
| 42423 | | sys | os | ubuntu_10  | string |

Possible types: `string`, `int`, `real`, `menu`, `string list`, `int list`, 
`real list`, `menu list`.

## File Changes

### FileChanges

| HostKey | PromiseHandle  | FileName | ChangeTimeStamp | ChangeType | LineNumber | ChangeDetails |
|--------|-----------------|----------|-----------------|------------|----------|------------|
| SHA-... | promise_handle1 | /etc/passwd | 12345| add | 10 | user1:x:2000:2000:User1 Name:/home/user1:/bin/bash |
| SHA-... | promise_handle2 | /etc/passwd | 12345| remove | 19 | user2:x:2000:2000:User2 Name:/home/user2:/bin/bash |

## Promise information

### PromiseStatusLast

**Note**: Only the *last* promise status (not log).

Join from `PromiseDefinitons` to query by other promise attributes.

| HostKey | PromiseHandle | PromiseStatus | CheckTimeStamp |
|---------|--------------|-----------------|----------------|
| 123123 | ntp_pkg_install | kept | 1234 |
| 123123 | copy_file | not_kept | 1235 |

### PromiseDefinitions

**Note**: This uses expanded promise definitions.

Promisees is a list, split into multiple rows. This means that promise handles 
might appear multiple times, if they have multiple promisees, depending on the 
exact query. Use an embedded query with `DISTINCT()` to avoid this.

**example**:

    SELECT Hosts.Name, BundleNTP.PromiseHandle FROM Hosts,
        (SELECT DISTINCT(PromiseHandle)
           FROM PromiseDefinitions
           WHERE Bundle='ntp')
        AS BundleNTP, PromiseStatusLast
        WHERE Hosts.HostKey=PromiseStatusLast.HostKey
          AND BundleNTP.PromiseHandle=PromiseStatusLast.PromiseHandle
          AND PromiseStatusLast.PromiseStatus='notkept'

| NameSpace| PromiseHandle | Promiser | Bundle | Promisee |
|---------|--------------|-------------|-------|---------|
| ntp | ntp_pkg_install | ntp-2.0.0-x86 | service_ntp | time team |
| ntp | ntp_pkg_install | ntp-2.0.0-x86 | service_ntp | epoch |
| | copy_file | /etc/syslog.conf | service_syslog | timer |
| | ntp_pkg_install | cfe_internal_ntp-2.0.0-x86 | service_ntp | time team |
| cfe_system | ntp_pkg_install | ntp-2.0.0-x86 | service_ntp | epoch |


### PromiseLogs

| HostKey | PromiseHandle | PromiseStatus  | PromiseLogReport | TimeStamp |
|---------|---------------|----------------|------------------|-----------|
| SHA-... | promise_handle1 | repaired | promise repaired message| 12345 |
| SHA-... | promise_handle2 | notkept | promise not kept message| 12345 |

Until CFEngine Enterprise v3.0 Promise logs were separated into: Promise 
Repaired log and Promise NotKept log. The SQL Reporting Engine merges these 
reports into one with the introduction of a new field(column): PromiseStatus

### BundleStatus

| HostKey | Bundle  | PercentageCompliance | CheckTimeStamp |
|---------|---------|----------------------|----------------|
| SHA-... | bundle1 | 100.0| 12345 | 
| SHA-... | bundle2 | 80.0| 12345 | 

### Benchmarks

| HostKey | EventName  | TimeTaken | CheckTimeStamp |
|---------|------------|-----------|----------------|
| SHA-... | action1 | 0.1| 12345| 
| SHA-... | action2 | 12| 12345| 

### PolicyStatus

| HostKey | PolicyName  | TotalKept | TotalRepaired | TotalNotKept | CheckTimeStamp | 
|---------|-------------|-----------|---------------|--------------|---------|
| SHA-... | promises.cf ... | 80| 10| 1 | 12345 |
| SHA-... | promises.cf v... | 90| 10| 12 | 12345 |


## Software

### Software

| HostKey | SoftwareName | SoftwareVersion | SoftwareArchitecture |
|---------|--------------|-----------------|----------------------|
| 123123 | apache | 2.2 | i686 |
| 123123 | xterm | 1.2 | default |
| 123123 | sshd | 1.1 | x86_64 |

### SoftwareUpdates

| HostKey | PatchReportType  | PatchName | PatchVersion | PatchArchitecture | 
|---------|------------------|-----------|--------------|-------------------|
| SHA-... | Installed | SuSEfirewall2 | 4330| default |
| SHA-... | Available | MozillaFirefox | 4195| default |


## Database Diagnostics

Diagnostics of the MongoDB database. For detailed documentation, see the
[MongoDB documentation](http://docs.mongodb.org/manual/reference/server-status).

### LastSeenHosts

| HostKey | LastSeenDirection  | RemoteHostKey | LastseenAt | LastseenInterval | 
|---------|--------------------|---------------|------------|----------------|
| SHA-... | Out | SHA-...| 12345| 120 |
| SHA-... | In | SHA-...| 12345| 50 |

### DatabaseServerStatus

| ReportRoundTimeStamp | Host  | Version | Uptime | GlobalLockTotalTime | GlobalLockTime | GlobalLockQuereTotal| GlobalLockQuereReaders| GlobalLockQuereWriters| MemoryResident| MemoryVirtual| MemoryMapped| BackgroundFlushCount| BackgroundFlushTotalTime| BackgroundFlushAverageTime| BackgroundFlushLastTime|
|----------------------|-------|---------|--------|---------------------|----------------|---------------------|-----------------------|-----------------------|---------------|--------------|-------------|---------------------|-------------------------|---------------------------|------------------------|
| 1359378564 | ubuntu | 2.2.2 | 1590.0 | 0.0 | 0.0 | 0 | 0 | 0 | 84 | 358 | 240 | 26 | 1287 | 0 | 0 |
| 1359378624 | ubuntu | 2.2.2 | 1650.0 | 0.0 | 0.0 | 0 | 0 | 0 | 86 | 358 | 240 | 27 | 1333 | 0 | 46 |

Data can be correlated with hub diagnostics by ReportTimeStamp.

### DatabaseStatus

| ReportRoundTimeStamp | Database  | AverageObjectSize | DataSize | StorageSize | FileSize|
|----------------------|-----------|-------------------|----------|-------------|---------|
| 1359378564 | cfreport | 1244.066641 | 3208 | 12296 | 196608 |
| 1359378624 | cfreport | 1283.96972 | 3312 | 12296 | 196608 |

Data can be correlated with hub diagnostics by ReportTimeStamp. 

### DatabaseCollectionStatus

| ReportRoundTimeStamp | Database  | Collection | ObjectCount | DataSize | AverageObjectSize| StorageSize| IndexCount| TotalIndexSize| PaddingFactor|
|----------------------|-----------|------------|-------------|----------|------------------|------------|-----------|---------------|--------------|
| 1359378564 | cfreport | archive | 1 | 0 | 0.0 | 8 | 4 | 31 | 1.009 |
| 1359378564 | cfreport	| hosts | 1 | 142 | 142.0 | 2220 | 4 | 31 | 1.0 |
| 1359378564 | cfreport	| monitoring_mg | 23 | 1836 | 79.826087 | 6388 | 2 | 15 | 1.0 |
| 1359378564 | cfreport	| monitoring_wk	| 23 | 146 | 6.347826 | 528 | 2 | 15 | 1.003 |
| 1359378564 | cfreport	| monitoring_yr	| 17 | 100 | 5.882353 | 488 | 2 | 15 | 1.002 |

Data can be correlated with hub diagnostics by ReportTimeStamp. 

## Hub Diagnostics

Data can be correlated with MongoDB diagnostics by ReportTimeStamp.

Performance is measured in time the operation took, in millisecond. Data sizes are measured in kilobytes.

### HubReportingPerformance

| ReportRoundTimeStamp | ReportsCollected | TotalCollectionPerformance | AverageCollectionPerformanceByHost | LowestCollectionPerformanceByHost | LowestCollectionPerformanceHostKey | AverageDataSizeByHost | LargestDataSizeByHost | LargestDataSizeHostKey | SampleAnalyzePerformance |
|----------------------|------------------|----------------------------|------------------------------------|-----------------------------------|------------------------------------|-----------------------|-----------------------|------------------------|--------------------------|
| 1361959894 | 1 | 3685 | 456 | 456 | 3045bcff2df88b9d737b5303fb97edbb8cad261b9c02ab9230d47a0df4658e43 | 359 | 359 | 3045bcff2df88b9d737b5303fb97edbb8cad261b9c02ab9230d47a0df4658e43 | 1 |
| 1361959894 |0 | 2085 | 0 | 0 | none | 0 | 0 | none | 1 |

### HubConnectionErrors

| ReportRoundTimeStamp | HostKey | Status |
|----------------------|---------|--------|
| 1361969437 | 7d75fc7c0baf36dbdb50f81789d8bc01cd1c297f639d83ed384c216d8058577e | ServerNoReply |
| 1361969737 | 7d75fc7c0baf36dbdb50f81789d8bc01cd1c297f639d83ed384c216d8058577e	| ServerAuthenticationError |
| 1361969137 | 7d75fc7c0baf36dbdb50f81789d8bc01cd1c297f639d83ed384c216d8058577e	| InvalidData |
| 1361959894 | 7d75fc7c0baf36dbdb50f81789d8bc01cd1c297f639d83ed384c216d8058577e	| Unknown |

### HubMaintenancePerformance

| MaintenanceTimeStamp | TotalPerformance | EnsureIndicesPerformance | PurgeHostReportsPerformance | HostCount | PurgeDiagnosticsPerformance |
|----------------------|------------------|--------------------------|-----------------------------|-----------|-----------------------------|
| 1361969437 | 1068 | 752 | 310 | 10 | 1 |
| 1361969433 | 1068 | 752 | 310 | 10 | 1 |

### HubMaintenanceErrors

| MaintenanceTimeStamp | HostKey | Message |
|----------------------|---------|---------|
| 1361969437 | 7d75fc7c0baf36dbdb50f81789d8bc01cd1c297f639d83ed384c216d8058577e | Operation: PurgeTimestampedReports (SHA=484572386e818614af188402f543ee822592e20684ecee1895a672926a2054b2) exited with message: ... |
| 1361969737 | none | Operation: Remove old entries in hub maintenance performance diagnostics () exited with message: "..." |
