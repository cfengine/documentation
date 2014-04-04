---
layout: default
title: Sub-Directories and Logs
published: true
sorting: 30
tags: [overviews, system overview, files, directories, logs]
---

[Directories in /var/cfengine](#)
	[Directories for Policy Files](#)
	[Directories for Output](#)
	[Other Directories in /var/cfengine](#)
[Log Files in /var/cfengine](#)
[Database Files in /var/cfengine](#)
[Process (AKA PID) Files in /var/cfengine](#)
[Sockets in /var/cfengine](#)
[Datafiles in /var/cfengine](#)
[Binary Files in /var/cfengine](#)
[CFEngine Agents and Daemons in /var/cfengine/bin](#)
[git in /var/cfengine/bin](#)
[Misc. in /var/cfengine/bin](#)
[MongoDB in /var/cfengine/bin](#)
[Postgres in /var/cfengine/bin](#)
[Redis in /var/cfengine/bin](#)
	
## Sub-Directories in /var/cfengine ##

### Directories for Policy Files

* `/modules`

Location of scripts used in `commands` promises.

* `/inputs`

Cached policy repository on each CFEngine client. When `cf-agent` is 
invoked by `cf-execd`, it reads only from this directory.

* `/masterfiles`

Policy repository which grants access to local or bootstrapped CFEngine 
clients when they need to update their policies. Policies obtained from 
`/var/cfengine/masterfiles` are then cached in `/var/cfengine/inputs` for 
local policy execution. The `cf-agent` executable does not execute policies 
directly from this repository.

## Output Directories

* `/var/cfengine/outputs`

Directory where `cf-agent` creates its output files. The outputs directory is 
a record of spooled run-reports. These are often mailed to the administrator 
by `cf-execd`, or can be copied to another central location and viewed in an 
alternative browser. However, not all hosts have an email capability or are 
online, so the reports are kept here.

* `/var/cfengine/reports`

Directory used to store reports. Reports are not tidied automatically, so you 
should delete these files after a time to avoid a build up.

* `/var/cfengine/state`

State data such as current process identifiers of running processes, 
persistent classes and other cached data.

* `/var/cfengine/lastseen`

Log data for incoming and outgoing connections.

### Other Sub-directories in /var/cfengine

[/bin](#/var/cfengine/bin)
* `/cfapache`
* `/config`
* `/design-center`
* `/httpd`
* `/lib`

Directory to store shared objects and dependencies that are in the bundled packages. 

* `/lib-twin`
* `/master_software_updates`
* `/plugins`
* `/ppkeys`

Directory used to store encrypted public/private keys for CFEngine
client/server network communications.

* `/share`
* `/software_updates`
* `/ssl`

## Log Files in /var/cfengine ##

On hosts, CFEngine writes numerous logs and records to its private workspace. 

[CFEngine Enterprise][Enterprise Report API] provides solutions 
for centralization and network-wide reporting at an arbitrary scale.

* `cf3.[hostname].runlog`

A time-stamped log of when each lock was released. This shows the last
time each individual promise was verified. 

* `cfagent.[hostname].log`

Although ambiguously named (for historical reasons) this log contains
the current list of setuid/setgid programs observed on the system.
CFEngine warns about new additions to this list. This log has been
deprecated.  

* `cf_notkept.log`

In CFEngine Enterprise, a list of promises, with handles and comments, that 
were not kept.

* `cf_repair.log`

In CFEngine Enterprise, a list of promises, with handles and comments, that were repaired.

* `promise_summary.log`

A time-stamped log of the percentage fraction of promises kept after
each run.  

## Database Files in /var/cfengine ##

* bundles.lmdb
* `cf_classes.lmdb`

A database of classes that have been defined on the current host,
including their relative frequencies, scaled like a probability.  

* `cf_lastseen.lmdb`

A database of hosts that last contacted this host, or were contacted by
this host, and includes the times at which they were last observed.   

* `checksum_digests.lmdb`

The database of hash values used in CFEngine's change management
functions.   

* `nova_agent_execution.lmdb`
* `nova_track.lmdb`
* `performance.lmdb`

A database of last, average and deviation times of jobs recorded by
`cf-agent`. Most promises take an immeasurably short time to check, but
longer tasks such as command execution and file copying are measured by
default. Other checks can be instrumented by setting a
`measurement_class` in the `action` body of a promise.   

## Process (AKA PID) Files in /var/cfengine ##

The CFEngine components keep their current process identifier number in
`pid files' in the work directory. 

* `cf-consumer.pid`
* `cf-execd.pid`
* `cf-hub.pid`
* `cf-monitord.pid`
* `cf-serverd.pid`

## Sockets in /var/cfengine ##

* `cf-hub-local`

## Datafiles in /var/cfengine ##

* `policy_server.dat`

IP address of the policy server?

## Binary Files in /var/cfengine ##

* `randseed`

## CFEngine Agents and Daemons in /var/cfengine/bin ##

* `bin/cf-agent`
* `bin/cf-consumer`
* `bin/cf-execd`
* `bin/cf-hub`
* `bin/cf-key`
* `bin/cf-monitord`
* `bin/cf-promises`
* `bin/cf-runagent`
* `bin/cf-serverd`
* `bin/cf-twin`

## git in /var/cfengine/bin ##

* `bin/git`
* `bin/git-cvsserver`
* `bin/gitk`
* `bin/git-receive-pack`
* `bin/git-shell`
* `bin/git-upload-archive`
* `bin/git-upload-pack`

## Misc. in /var/cfengine/bin ##

* `bin/curl`
* `bin/lmdump`
* `bin/openssl`
* `bin/rpmvercmp`
* `bin/rsync`
* `bin/runalerts.sh`

## MongoDB in /var/cfengine/bin ##

* `bin/bsondump`
* `bin/mdb_copy`
* `bin/mdb_stat`
* `bin/mongo`
* `bin/mongod`
* `bin/mongodump`
* `bin/mongoexport`
* `bin/mongofiles`
* `bin/mongoimport`
* `bin/mongooplog`
* `bin/mongoperf`
* `bin/mongorestore`
* `bin/mongos`
* `bin/mongosniff`
* `bin/mongostat`
* `bin/mongotop`

## Postgres in /var/cfengine/bin ##

* `bin/clusterdb`
* `bin/createdb`
* `bin/createlang`
* `bin/createuser`
* `bin/dropdb`
* `bin/droplang`
* `bin/dropuser`
* `bin/initdb`
* `bin/pg_basebackup`
* `bin/pg_config`
* `bin/pg_controldata`
* `bin/pg_ctl`
* `bin/pg_dump`
* `bin/pg_dumpall`
* `bin/pg_isready`
* `bin/pg_receivexlog`
* `bin/pg_resetxlog`
* `bin/pg_restore`
* `bin/postgres`
* `bin/postmaster`
* `bin/psql`
* `bin/reindexdb`
* `bin/vacuumdb`

## Redis in /var/cfengine/bin ##

* `bin/redis-benchmark`
* `bin/redis-check-aof`
* `bin/redis-check-dump`
* `bin/redis-cli`
* `bin/redis-server`


## Not Verified ##

* `state/cf_lock.lmdb`

A database of active and inactive locks and their expiry times. Deleting
this database will reset all lock protections in CFEngine.   

* `state/history.lmdb`

CFEngine Enterprise maintains this long-term trend database.   

* `state/cf_observations.lmdb`

This database contains the current state of the observational history of
the host as recorded by `cf-monitord`.     

* `state/cf_state.lmdb`

A database of persistent classes active on this current host.   

* `state/nova_measures.lmdb`

CFEngine Enterprise database of custom measurements.

* `state/nova_static.lmdb`

CFEngine Enterprise database of static system discovery data.

* `state/cf_procs`
A cache of the process table. This is useful for `measurement` promises about processes.

* `state/cf_rootprocs`
A cache of the process table of processes owned by the root user. This is useful for `measurement` promises about processes.

* `state/cf_otherprocs`
A cache of the process table for processes not owned by the root user. This is useful for `measurement` promises about processes.

* `state/file_changes.log`

A time-stamped log of which files have experienced content changes since
the last observation, as determined by the hashing algorithms in
CFEngine.   

* `state/*_measure.log`

CFEngine Enterprise maintains user-defined logs based on specifically
promised observations of the system.

* `state/env_data`

This file contains a list of currently discovered classes and variable
values that characterize the anomaly alert environment. They are altered
by the monitor daemon.   

* `/var/logs/CFEngineHub-Install.log`

This file contains logs related to the CFEngine package installation.
