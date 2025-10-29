---
layout: default
title: CFEngine directory structure
published: true
sorting: 20
---

The CFEngine application is fully contained within the /var/cfengine directory tree. Here is a quick breakdown of the directory structure and some of the files and functions associated with each subdirectory.

## /var/cfengine/bin

### Agents

* `cf-agent`: Executes the promises.cf file; ensures that all promises are being kept
* `cf-key`
* `cf-promises`: Verifies CFEngine's configuration syntax
* `cf-runagent`: Contacts a remote system to run cf-agent

### Daemons

* `cf-execd`: Starts the cf-agent process at a specified time interval.
* `cf-monitord`: Collects system statistics
* `cf-serverd`: Provides network services; used to distribute policy and data files
* `runalerts.sh`: Updates Mission Portal status and activates alert actions (Enterprise only)
* `cf-hub`: Responsible for collecting reports from remote agents. (CFEngine Enterprise only)

See also: [CFEngine component applications and daemons][Overview#CFEngine component applications and daemons]

## Directories for policy files

### /var/cfengine/modules

Location of scripts used in `commands` promises.

### /var/cfengine/inputs

Cached policy repository on each CFEngine client. When `cf-agent` is
invoked by `cf-execd`, it reads only from this directory.

### /var/cfengine/masterfiles

Policy repository which grants access to local or bootstrapped CFEngine
clients when they need to update their policies. Policies obtained from
`/var/cfengine/masterfiles` are then cached in `/var/cfengine/inputs` for
local policy execution. The `cf-agent` executable does not execute policies
directly from this repository.

## Output directories

### /var/cfengine/outputs

Directory where `cf-agent` creates its output files. The outputs directory is
a record of spooled run-reports. These are often mailed to the administrator
by `cf-execd`, or can be copied to another central location and viewed in an
alternative browser. However, not all hosts have an email capability or are
online, so the reports are kept here.

### /var/cfengine/reports

Directory used to store reports. Reports are not tidied automatically, so you
should delete these files after a time to avoid a build up.

### /var/cfengine/state

State data such as current process identifiers of running processes,
persistent classes and other cached data.

* `/var/cfengine/state/promise_execution.log`: In CFEngine Enterprise `cf-agent` writes promise execution results to this temporary file during execution. When `cf-agent` exits this data is stored for use by the reporting subsystem and the file is purged.

* `/var/cfengine/state/variable.cache.tmp`: In CFEngine Enterprise as `cf-agent` executes information about variables are stored in this file. When `cf-agent` exits this data is stored for use by the reporting subsystem and the file is purged.

* `/var/cfengine/state/context.cache.tmp`: In CFEngine Enterprise as `cf-agent` executes, information about classes that are defined are stored in this file. When `cf-agent` exits this data is stored for use by the reporting subsystem and the file is purged.

### /var/cfengine/lastseen

Log data for incoming and outgoing connections.

### /var/cfengine/cfapache

### /var/cfengine/config

### /var/cfengine/httpd

### /var/cfengine/lib

Directory to store shared objects and dependencies that are in the bundled packages.

### /var/cfengine/master_software_updates

### /var/cfengine/plugins

### /var/cfengine/ppkeys

Directory used to store encrypted public/private keys for CFEngine
client/server network communications.

### /var/cfengine/share

### /var/cfengine/software_updates

### /var/cfengine/ssl

## Log Files in /var/cfengine

On hosts, CFEngine writes numerous logs and records to its private workspace.

[CFEngine Enterprise](https://cfengine.com/product-overview/) provides solutions
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

## Database files in /var/cfengine

### state/cf_classes.lmdb

A database of classes that have been defined on the current host, including
their relative frequencies, scaled like a probability.

### state/cf_lastseen.lmdb

A database of hosts that last contacted this host, or were contacted by this
host, and includes the times at which they were last observed.

### state/cf_lock.lmdb

A database of active and inactive promise locks and their expiry times. Deleting
this database will reset all lock protections in CFEngine.

**Note:** Locks are purged in order to maintain the integrity and health of the
underlying lock database. When the lock database utilization grows to 25%
locks 4 weeks or older are purged. At 50% locks 2 weeks or older are purged
and at 75% locks older than 1 week are purged.

### state/cf_changes.lmdb

The database of hash values used in CFEngine's change management
functions.

### state/nova_agent_execution.lmdb
### state/nova_track.lmdb
### state/performance.lmdb

A database of last, average and deviation times of jobs recorded by
`cf-agent`. Most promises take an immeasurably short time to check, but
longer tasks such as command execution and file copying are measured by
default. Other checks can be instrumented by setting a
`measurement_class` in the `action` body of a promise.

## Process (AKA PID) files in /var/cfengine

The CFEngine components keep their current process identifier number in
_pid files_ in the work directory.

* `cf-execd.pid`
* `cf-hub.pid`
* `cf-monitord.pid`
* `cf-serverd.pid`

## Sockets in /var/cfengine

* `cf-hub-local`

## Datafiles in /var/cfengine

### `policy_server.dat`

Specifies the host's primary policy server in the format `(<IP>|<Hostname>)[:<Port>]`. This file's contents are used to define the `default:sys.policy_hub` and `default:sys.policy_hub_port` variables.

**See also:** [`default:sys.policy_hub`](/reference-special-variables/sys-syspolicy_hub), [`default:sys.policy_hub_port`](/reference-special-variables-sys-syspolicy_hub_port)

**History:**

- Added in CFEngine 3.2.0
- Support hostname and port added in CFEngine 3.10.0

### `ignore_interfaces.rx`

CFEngine will ignore interfaces for interfaces that match one of the regular expressions listed in this file (one regular expression per line).

If an interface matches a regular expression in the file then various classes and variables will not be populated with related information. For example, but not limited to:

**Classes:**

* `ipv4_` prefixed classes
* `mac_` prefixed classes

**Variables:**

* `sys.ipv4_N[iface]`
* `sys.ip2iface`
* `sys.ipaddresses`
* `sys.interface_flags`
* `sys.inet`
* `sys.inet6`
* `sys.hardware_mac[iface]`
* `sys.hardware_addresses`

**History:**

* Introduced in CFEngine 3.10.0
* Preferred location moved from `$(sys.inputdir)` to `$(sys.workdir)` in CFEngine 3.23.0

## Binary files in /var/cfengine

* `randseed`

## git in /var/cfengine/bin

* `bin/git`
* `bin/git-cvsserver`
* `bin/gitk`
* `bin/git-receive-pack`
* `bin/git-shell`
* `bin/git-upload-archive`
* `bin/git-upload-pack`

## Misc. in /var/cfengine/bin

* `bin/curl`
* `bin/lmdump`
* `bin/openssl`
* `bin/rpmvercmp`
* `bin/rsync`
* `bin/runalerts.sh`

## Postgres in /var/cfengine/bin

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


## Not verified

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

* `/var/logs/CFEngine-Install.log`

This file contains logs related to the CFEngine package installation.
