---
layout: default
title: SQLite Database Schema
sorting: 100
published: true
tags: [overviews, mission portal, reports, reporting, database schema]
---

## hosts ##

HostKey VARCHAR(100)
HostName VARCHAR(100)
IPAddress VARCHAR(50)
ReportTimeStamp BIGINT(20)

### contexts ###

HostKey VARCHAR(100)
ContextName VARCHAR(50)
DefineTimeStamp BIGINT(20)

### variables ###

HostKey VARCHAR(100)
NameSpace VARCHAR(50)
Bundle VARCHAR(50)
VariableName VARCHAR(50)
VariableValue VARCHAR(100)
VariableType VARCHAR(20)

### lastseenhosts ###

HostKey VARCHAR(100)
LastSeenDirection VARCHAR(10)
RemoteHostKey VARCHAR(100)
LastSeenAt BIGINT(20)
LastSeenInterval INT(11)

### software ###

HostKey VARCHAR(100)
SoftwareName VARCHAR(50)
SoftwareVersion VARCHAR(50)
SoftwareArchitecture VARCHAR(20)

### softwareupdates ###

HostKey VARCHAR(100)
PatchReportType VARCHAR(8)
PatchName VARCHAR(50)
PatchVersion VARCHAR(50)
PatchArchitecture VARCHAR(20)

### filechanges ###

HostKey VARCHAR(100)
PromiseHandle VARCHAR(50)
FileName VARCHAR(400)
ChangeTimeStamp BIGINT(20)
ChangeType VARCHAR(10)
LineNumber INT(11)
ChangeDetails VARCHAR(2047)

### promisestatuslast ###

HostKey VARCHAR(100)
PromiseHandle VARCHAR(50)
PromiseStatus VARCHAR(10)
CheckTimeStamp BIGINT(20)

#### promisedefinitions ####

NameSpace VARCHAR(50)
PromiseHandle VARCHAR(50)
Promiser VARCHAR(50)
Bundle VARCHAR(50)
Promise VARCHAR(100)

### benchmarks ###

HostKey VARCHAR(100)
EventName VARCHAR(254)
TimeTaken DOUBLE
CheckTimeStamp BIGINT(20)

### bundlestatus ###

HostKey VARCHAR(100)
NameSpace VARCHAR(50)
Bundle VARCHAR(254)
PercentageCompliance DOUBLE
CheckTimeStamp BIGINT(20)

### promiselogs ###

HostKey VARCHAR(100)
PromiseHandle VARCHAR(254)
PromiseStatus VARCHAR(10)
PromiseStatusReport VARCHAR(1024)
Time BIGINT(20)

### policystatus ###

HostKey VARCHAR(100)
PolicyName VARCHAR(254)
TotalKept INT(11)
TotalRepaired INT(11)
TotalNotKept INT(11)
CheckTimeStamp BIGINT(20)


